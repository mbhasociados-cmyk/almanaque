// Núcleo de sincronización, independiente del navegador para poder probarlo.
// db:     { pendingForUser(uid), all(), get(id), put(ev), putMany(evs), setMeta(k,v), getMeta(k) }
// remote: { insertIgnore(rows) -> {error}, fetchPage(from, to) -> {data, error} }
// Estados locales: local (sin cuenta) | pending | awaiting_confirmation | synced | conflict | invalid

export const WIRE_FIELDS = ["id", "user_id", "device_id", "device_seq", "run_id", "type", "lesson_id", "lesson_revision", "payload", "client_ts"];
const PAGE = 1000;
const BATCH = 100;

export function toWire(ev) {
  const o = {};
  for (const f of WIRE_FIELDS) o[f] = ev[f] ?? null;
  return o;
}

function stable(v) { // JSON con claves ordenadas para comparar contenido
  if (v === null || typeof v !== "object") return JSON.stringify(v);
  if (Array.isArray(v)) return "[" + v.map(stable).join(",") + "]";
  return "{" + Object.keys(v).sort().map(k => JSON.stringify(k) + ":" + stable(v[k])).join(",") + "}";
}
export function sameContent(local, remote) {
  for (const f of WIRE_FIELDS) {
    if (f === "client_ts") { if (Date.parse(local[f]) !== Date.parse(remote[f])) return false; continue; }
    if (f === "payload") { if (stable(local[f]) !== stable(remote[f])) return false; continue; }
    if ((local[f] ?? null) !== (remote[f] ?? null)) return false;
  }
  return true;
}

export function classifyError(err) {
  if (!err) return null;
  const status = err.status ?? err.statusCode;
  const code = err.code || "";
  const msg = String(err.message || err);
  if (err.name === "TypeError" || /Failed to fetch|NetworkError|network|fetch/i.test(msg) && !status) return "network";
  if (status === 401 || /JWT|token/i.test(msg) || code === "PGRST301") return "auth";
  if (status === 403 || code === "42501") return "permission";
  if (code.startsWith("23") || code === "22P02" || status === 400 || status === 409) return "validation";
  if (status >= 500) return "server";
  return "unknown";
}

// Un ciclo completo: envío de pendientes y reconciliación total paginada.
export async function syncOnce({ db, remote, uid, log = () => {} }) {
  const t0 = Date.now();
  const metrics = { sent: 0, received: 0, bytesOut: 0, bytesIn: 0, invalid: 0, conflicts: 0 };

  // 1. Envío por lotes
  const pending = await db.pendingForUser(uid);
  for (let i = 0; i < pending.length; i += BATCH) {
    const batch = pending.slice(i, i + BATCH);
    const rows = batch.map(toWire);
    metrics.bytesOut += JSON.stringify(rows).length;
    const { error } = await remote.insertIgnore(rows);
    if (error) {
      const kind = classifyError(error);
      if (kind !== "validation") return { ok: false, kind, error, metrics };
      // Aislar el o los eventos inválidos sin bloquear la cola
      for (const ev of batch) {
        const r = await remote.insertIgnore([toWire(ev)]);
        if (r.error) {
          const k2 = classifyError(r.error);
          if (k2 !== "validation") return { ok: false, kind: k2, error: r.error, metrics };
          await db.put({ ...ev, sync: "invalid", sync_error: String(r.error.message || r.error.code || "inválido") });
          metrics.invalid++;
        } else {
          await db.put({ ...ev, sync: "awaiting_confirmation" });
          metrics.sent++;
        }
      }
      continue;
    }
    // Lote sin error = envío exitoso; se confirma en la reconciliación
    await db.putMany(batch.map(ev => ({ ...ev, sync: "awaiting_confirmation" })));
    metrics.sent += batch.length;
  }

  // 2. Reconciliación completa, paginada por seq, cursor temporal
  const remoteAll = [];
  for (let from = 0; ; from += PAGE) {
    const { data, error } = await remote.fetchPage(from, from + PAGE - 1);
    if (error) return { ok: false, kind: classifyError(error), error, metrics };
    metrics.bytesIn += JSON.stringify(data).length;
    remoteAll.push(...data);
    if (data.length < PAGE) break;
  }
  metrics.received = remoteAll.length;

  // 3. Fusión por id
  const updates = [];
  for (const r of remoteAll) {
    const l = await db.get(r.id);
    if (!l) { updates.push({ ...r, sync: "synced" }); continue; }
    if (l.sync === "conflict") continue;
    if (sameContent(l, r)) {
      if (l.sync !== "synced" || l.seq !== r.seq) updates.push({ ...l, seq: r.seq, server_ts: r.server_ts, sync: "synced" });
    } else {
      updates.push({ ...l, sync: "conflict", remote_copy: r });
      metrics.conflicts++;
    }
  }
  if (updates.length) await db.putMany(updates);

  metrics.ms = Date.now() - t0;
  log(metrics);
  return { ok: true, metrics };
}

export function backoffDelay(attempt, base = 2000, max = 300000, rand = Math.random) {
  const exp = Math.min(max, base * 2 ** attempt);
  return Math.round(exp / 2 + rand() * exp / 2); // espera creciente con variación aleatoria
}
