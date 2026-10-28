// Almanaque del Saber — interfaz v3: tarjetas visuales, en línea, con colección de lo aprendido.
import { CONFIG } from "./config.js";
import * as db from "./db.js";
import * as sync from "./sync.js";
import { deriveState, chileDate, questionsOf } from "./state.js";
import { sanitizeSvg } from "./sanitize.js";

const $ = (s, el = document) => el.querySelector(s);
const view = $("#view");
const player = $("#player");
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const ROUTES = ["hoy", "explorar", "aprendido", "cuenta"];

const app = { catalog: null, calendar: null, approvals: null, lessons: new Map(), state: null, route: "hoy", filter: "Todos", play: null, syncStatus: null, preview: null, open: null };

// ------------------------------------------------------------ datos (siempre desde la red)
async function fetchJson(url) {
  const r = await fetch(url + (url.includes("?") ? "&" : "?") + "t=" + Date.now(), { cache: "no-store" });
  if (!r.ok) throw new Error("HTTP " + r.status);
  return r.json();
}
async function loadIndex(name) {
  try { const j = await fetchJson(`data/${name}`); await db.setMeta("idx:" + name, j); return j; }
  catch { return (await db.getMeta("idx:" + name)) || null; } // solo ante un corte momentáneo
}
async function sha256Hex(buf) {
  const h = await crypto.subtle.digest("SHA-256", buf);
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, "0")).join("");
}
// Descarga la lección y verifica su SHA-256 contra el catálogo antes de mostrarla.
async function ensureLesson(entry) {
  const k = `${entry.id}@${entry.revision}`;
  if (app.lessons.has(k)) return app.lessons.get(k);
  try {
    const r = await fetch(entry.archivo + "?t=" + Date.now(), { cache: "no-store" });
    if (!r.ok) throw new Error("HTTP " + r.status);
    const buf = await r.arrayBuffer();
    if (entry.sha256 && (await sha256Hex(buf)) !== entry.sha256) throw new Error("hash");
    const data = JSON.parse(new TextDecoder().decode(buf));
    app.lessons.set(k, data);
    await db.putLesson(data, entry.sha256);
    return data;
  } catch {
    const stored = await db.getLesson(entry.id, entry.revision);
    if (stored) app.lessons.set(k, stored);
    return stored;
  }
}

// ------------------------------------------------------------ autoridad editorial (data/aprobaciones.v1.json)
const catEntry = (id, rev) => app.catalog?.lecciones.find(l => l.id === id && (rev == null || l.revision === rev));
const REVIEW_MODE = CONFIG.MODO_REVISION === true;
function editorialState(entry) {
  if (!entry) return "excluido";
  const regs = (app.approvals?.registros || []).filter(r => r.id === entry.id && r.revision === entry.revision);
  if (!regs.length) return "borrador";
  if (regs.length > 1 || regs.some(r => r.sha256 !== entry.sha256)) return "excluido";
  const r = regs[0];
  // Opción A (delegación general de Max del 20-10-2026): autoverificación de Claude + publicación autorizada por delegación, sin V°B° individual.
  const optA = r.modalidad === "opcion-A" && r.estadoRevision === "AUTOVERIFICADA_POR_CLAUDE" && r.publicacion === "AUTORIZADA_POR_DELEGACION_GENERAL_DE_MAX" && r.delegacion && r.delegacion.por && r.delegacion.fecha;
  const verified = optA || (r.verificacion && (r.verificacion.resultado === "aprobado" || r.verificacion.estado === "verificado") && r.verificacion.revisor && r.verificacion.fecha);
  if (!verified) return "borrador";
  return optA || (r.vb && r.vb.por && r.vb.fecha) ? "publicado" : "verificado";
}
const isPreview = (e) => Boolean(app.preview && e && e.id === app.preview.id && e.revision === app.preview.rev);
const isCards = (e) => e?.schemaVersion === "2.0"; // la interfaz v3 muestra solo lecciones en tarjetas
function visible(e) { const st = editorialState(e); return isCards(e) && (st === "publicado" || (st !== "excluido" && (REVIEW_MODE || isPreview(e)))); }
// Si una lección tiene varias revisiones publicadas (por ejemplo, una nueva con ilustraciones), se muestra solo la más reciente.
const latestById = (list, prefer = () => false) => { const m = new Map(); for (const e of list) { const p = m.get(e.id); if (!p || (prefer(e) && !prefer(p)) || (prefer(e) === prefer(p) && e.revision > p.revision)) m.set(e.id, e); } return [...m.values()]; };
const visibleEntries = () => latestById((app.catalog?.lecciones || []).filter(e => visible(e) && (!isPreview(e) || REVIEW_MODE || editorialState(e) === "publicado")));
function todayIso() { return chileDate(new Date()); }
function todayEntry() {
  if (app.preview) { const p = catEntry(app.preview.id, app.preview.rev); if (p && visible(p) && editorialState(p) !== "publicado") return p; }
  const c = app.calendar?.entradas.find(x => x.fecha === todayIso());
  const e = c ? catEntry(c.id, c.revision) : null;
  return e && visible(e) ? e : null; // solo la lección programada para hoy
}
// Fecha programada de una lección; si es futura, la lección se muestra como "Anticipada".
const scheduled = (e) => app.calendar?.entradas.find(x => x.id === e.id && x.revision === e.revision)?.fecha || null;
const isEarly = (e) => { const f = scheduled(e); return Boolean(f && f > todayIso()); };
const shortDate = (iso) => { const [, m, d] = iso.split("-").map(Number); return `${d} de ${MESES[m - 1]}`; };
const nextScheduled = () => (app.calendar?.entradas || []).filter(x => x.fecha > todayIso()).map(x => ({ x, e: catEntry(x.id, x.revision) })).filter(o => o.e && visible(o.e)).sort((a, b) => a.x.fecha.localeCompare(b.x.fecha))[0] || null;

// ------------------------------------------------------------ estado y eventos
async function refresh() {
  for (const row of await db.allLessons()) if (!app.lessons.has(row.key)) app.lessons.set(row.key, row.data);
  app.state = deriveState(await db.allEvents(), app.lessons, todayIso());
}
async function record(type, L, extra = {}) {
  await db.addEvent({ type, lesson_id: L.id, lesson_revision: L.revision, ...extra });
  sync.schedule(2000);
  await refresh();
}
const lessonState = (L) => app.state?.perLesson.get(`${L.id}@${L.revision}`) || { activeRunId: null, maxStep: -1, attempts: [], openAttempt: null, completed: false, revealed: [] };
const learned = () => visibleOrLearned().filter(e => lessonState(e).completed);
// Lo aprendido se conserva aunque la lección deje de estar en el calendario; se excluye solo si su registro es contradictorio.
const visibleOrLearned = () => latestById((app.catalog?.lecciones || []).filter(e => isCards(e) && editorialState(e) !== "excluido" && (visible(e) || lessonState(e).completed)), e => lessonState(e).completed);

// ------------------------------------------------------------ cabecera y navegación
const SYNC_LABEL = {
  local: () => "Solo en este equipo", needs_login: () => "Inicia sesión", idle: () => "Conectando…", syncing: () => "Guardando…",
  synced: () => "Al día", pending: () => "Guardando…", offline: () => "Sin internet", unreachable: () => "Sin conexión con el servidor",
  server: () => "Sin conexión con el servidor", unknown: () => "Sin conexión con el servidor", auth: () => "Vuelve a iniciar sesión",
  permission: () => "Cuenta no habilitada", other_owner: () => "Equipo de otra cuenta",
};
const SYNC_TONE = { synced: "ok", syncing: "neutral", idle: "neutral", pending: "neutral", needs_login: "warn", offline: "warn" };
function renderHeader() {
  const s = app.syncStatus || sync.status;
  const pill = $("#sync-pill");
  pill.textContent = (SYNC_LABEL[s.state] || (() => s.state))(s);
  pill.dataset.tone = SYNC_TONE[s.state] || "bad";
  for (const t of ROUTES) $("#tab-" + t).setAttribute("aria-current", app.route === t ? "page" : "false");
  const n = learned().length;
  $("#tab-aprendido .n").textContent = n ? String(n) : "";
  const pe = app.preview ? catEntry(app.preview.id, app.preview.rev) : null;
  const draftPreview = Boolean(pe && editorialState(pe) !== "publicado");
  $("#review-bar").hidden = !REVIEW_MODE && !draftPreview;
  $("#review-bar").innerHTML = draftPreview ? `Vista previa de un borrador: no se publica hasta tener verificación y V°B°. <a href="./">Salir</a>` : "Modo revisión: se muestran borradores.";
}
function go(route) {
  app.route = ROUTES.includes(route) ? route : "hoy"; app.open = null;
  if (location.hash !== "#" + app.route) history.replaceState(null, "", location.search + "#" + app.route);
  render();
}
function render() {
  renderHeader();
  ({ hoy: renderHoy, explorar: renderExplorar, aprendido: renderAprendido, cuenta: renderCuenta }[app.route])();
}

// ------------------------------------------------------------ piezas visuales
function visualHtml(L, svgText, cls = "") {
  const clean = svgText ? sanitizeSvg(svgText, L.id) : null;
  return clean ? `<div class="visual ${cls}">${clean}</div>` : "";
}
// Portada por tema cuando la lección aún no tiene ilustración (no forma parte del contenido aprobado).
const GLYPH = { fisica: "☀", astronomia: "☾", quimica: "⚗", cocina: "⚗", geografia: "▲", economia: "$", sociedad: "$", literatura: "✎", tecnologia: "⌖", historia: "⌛", arte: "✿", biologia: "❦", salud: "❦", matematica: "∑" };
const placeholder = (fam, cls = "cover-visual") => `<div class="visual ${cls} placeholder" aria-hidden="true"><span class="glyph">${(GLYPH[fam] || "✦") + "\uFE0E"}</span></div>`;
function coverSvg(entry) { // portada de la lección (desde el contenido, si ya está cargado)
  const L = app.lessons.get(`${entry.id}@${entry.revision}`);
  const t = L?.tarjetas?.find(x => x.tipo === "portada");
  return L && t?.visual ? visualHtml(L, t.visual, "cover-visual") : placeholder(entry.familia);
}
function tile(entry, big = false) {
  const st = lessonState(entry);
  const L = app.lessons.get(`${entry.id}@${entry.revision}`);
  const action = st.completed ? "Aprendida ✓ · ver de nuevo" : st.maxStep >= 0 ? "Continuar" : "Empezar";
  return `<button class="tile ${big ? "big" : ""}" data-fam="${esc(entry.familia)}" data-open="${esc(entry.id)}@${entry.revision}">
    ${coverSvg(entry)}
    <span class="tile-body"><span class="kicker">${esc(entry.disciplina)}${isEarly(entry) && !isPreview(entry) ? ` · Anticipada, del ${esc(shortDate(scheduled(entry)))}` : ""}</span><span class="tile-title">${esc(entry.titulo)}</span>
    ${big && L?.subtitulo ? `<span class="tile-sub">${esc(L.subtitulo)}</span>` : ""}
    <span class="tile-foot"><span>${entry.minutosEstimados} min</span><span class="cta">${action}</span></span></span></button>`;
}
function bindTiles() {
  view.querySelectorAll("[data-open]").forEach(b => b.onclick = () => { const [id, rev] = b.dataset.open.split("@"); openLesson(catEntry(id, Number(rev))); });
  view.querySelectorAll("[data-go]").forEach(b => b.onclick = () => go(b.dataset.go));
}
async function loadAll(entries) { // carga en paralelo lo que falta y vuelve a dibujar
  const miss = entries.filter(e => !app.lessons.has(`${e.id}@${e.revision}`));
  if (!miss.length) return;
  await Promise.all(miss.map(ensureLesson));
  await refresh(); if (!app.play) render();
}

// ------------------------------------------------------------ Hoy
function renderHoy() {
  const hoy = todayIso();
  const [y, m, d] = hoy.split("-").map(Number);
  const dow = new Date(Date.UTC(y, m - 1, d)).getUTCDay();
  const e = todayEntry();
  const n = learned().length;
  const others = e ? visibleEntries().filter(x => x !== e && !lessonState(x).completed && !isEarly(x)).slice(0, 4) : [];
  const proximas = visibleEntries().filter(x => x !== e && isEarly(x) && !lessonState(x).completed).sort((a, b) => scheduled(a).localeCompare(scheduled(b))).slice(0, 6);
  view.innerHTML = `<section class="hello"><p class="date">${DIAS[dow]} ${d} de ${MESES[m - 1]}</p>
      <h1>${app.preview && e && isPreview(e) ? "Vista previa" : "Tu idea de hoy"}</h1></section>
    ${e ? tile(e, true) : (() => { const nx = nextScheduled(); return `<div class="empty"><h2>Hoy no hay una idea programada</h2><p>${nx ? `La próxima llega el ${esc(shortDate(nx.x.fecha))}. Si no quieres esperar, puedes verla anticipada en Explorar.` : "Estamos preparando y verificando las próximas lecciones."}</p>${nx ? `<button class="btn" data-go="explorar">Ir a Explorar</button>` : ""}</div>`; })()}
    <div class="stat"><b>${n}</b> ${n === 1 ? "idea aprendida" : "ideas aprendidas"} <button class="link" data-go="aprendido">Ver mi colección</button></div>
    ${others.length ? `<h2 class="section">Sigue explorando</h2><div class="grid">${others.map(x => tile(x)).join("")}</div>` : ""}
    ${proximas.length ? `<h2 class="section">Próximas lecciones</h2><p class="date">Puedes verlas antes de su fecha.</p><div class="grid">${proximas.map(x => tile(x)).join("")}</div>` : ""}`;
  bindTiles();
  loadAll([e, ...others, ...proximas].filter(Boolean));
}

// ------------------------------------------------------------ Explorar
function renderExplorar() {
  const all = visibleEntries();
  const temas = ["Todos", ...new Set(all.map(e => e.disciplina))];
  if (!temas.includes(app.filter)) app.filter = "Todos";
  const list = all.filter(e => app.filter === "Todos" || e.disciplina === app.filter);
  view.innerHTML = `<section class="hello"><h1>Explorar</h1><p class="date">Aprende algo de cualquier tema, en pocos minutos.</p></section>
    <div class="chips">${temas.map(t => `<button class="chip" aria-pressed="${t === app.filter}" data-f="${esc(t)}">${esc(t)}</button>`).join("")}</div>
    ${list.length ? `<div class="grid">${list.map(x => tile(x)).join("")}</div>` : `<div class="empty"><p>Aún no hay lecciones publicadas en este tema.</p></div>`}`;
  view.querySelectorAll("[data-f]").forEach(b => b.onclick = () => { app.filter = b.dataset.f; renderExplorar(); });
  bindTiles();
  loadAll(list);
}

// ------------------------------------------------------------ Aprendido: la colección de resúmenes
function summaryCard(e, L) {
  const R = L?.resumen;
  const when = lessonState(e).firstCompletedAt ? new Date(lessonState(e).firstCompletedAt).toLocaleDateString("es-CL", { day: "numeric", month: "long" }) : "";
  return `<article class="summary" data-fam="${esc(e.familia)}">
    <header><span class="kicker">${esc(e.disciplina)}${when ? " · " + esc(when) : ""}</span><h3>${esc(R?.titulo || e.titulo)}</h3></header>
    ${R ? `<ul>${R.puntos.map(p => `<li>${esc(p)}</li>`).join("")}</ul>` : `<p class="small">Cargando resumen…</p>`}
    <button class="link" data-open="${esc(e.id)}@${e.revision}">Ver la lección de nuevo</button></article>`;
}
function renderAprendido() {
  const list = learned().sort((a, b) => (lessonState(b).firstCompletedAt || "").localeCompare(lessonState(a).firstCompletedAt || ""));
  view.innerHTML = `<section class="hello"><h1>Aprendido</h1><p class="date">${list.length ? `Tu colección: ${list.length} ${list.length === 1 ? "idea" : "ideas"}. Cada lección que terminas deja aquí su resumen.` : "Aquí se guardará el resumen de cada lección que termines."}</p></section>
    ${list.length ? `<div class="summaries">${list.map(e => summaryCard(e, app.lessons.get(`${e.id}@${e.revision}`))).join("")}</div>`
      : `<div class="empty"><h2>Tu colección está vacía</h2><p>Termina tu primera lección y su resumen aparecerá aquí.</p><button class="btn" data-go="hoy">Ir a la idea de hoy</button></div>`}`;
  bindTiles();
  loadAll(list);
}

// ------------------------------------------------------------ Cuenta (inicio de sesión por código)
const AUTH_KEY = "almanaque-auth-draft", AUTH_TTL = 60 * 60 * 1000;
let authMem = null;
function authDraft() {
  const empty = { email: "", code: "", codeSent: false, msg: "", t: 0 };
  if (!authMem) { try { authMem = JSON.parse(localStorage.getItem(AUTH_KEY) || "null"); } catch { authMem = null; } }
  if (!authMem || Date.now() - (authMem.t || 0) > AUTH_TTL) authMem = { ...empty };
  return { ...empty, ...authMem };
}
function saveAuthDraft(patch) {
  authMem = { ...authDraft(), ...patch, t: Date.now() };
  try { const { code, ...keep } = authMem; localStorage.setItem(AUTH_KEY, JSON.stringify(keep)); } catch { /* queda en memoria */ }
}
function clearAuthDraft() { authMem = null; try { localStorage.removeItem(AUTH_KEY); } catch { /* nada */ } }

function renderCuenta() {
  const s = app.syncStatus || sync.status;
  let acct;
  if (!sync.isEnabled()) acct = `<p>La conexión con el servidor no está configurada.</p>`;
  else if (!sync.currentUser()) {
    const a = authDraft();
    acct = `<p>Entra con tu correo para que tu avance y tu colección se vean igual en el PC y en el celular.</p>
      <form id="f-email" class="form"><label for="email">Correo</label><input id="email" type="email" autocomplete="email" required placeholder="tu@correo.cl" value="${esc(a.email)}">
      <button class="btn" type="submit">${a.codeSent ? "Enviar otro código" : "Enviar código"}</button></form>
      <form id="f-code" class="form"${a.codeSent ? "" : " hidden"}><label for="code">Código de 6 dígitos que llegó a tu correo</label><input id="code" inputmode="numeric" autocomplete="one-time-code" pattern="[0-9]{6}" maxlength="6" required value="${esc(a.code)}">
      <button class="btn" type="submit">Entrar</button></form><p id="auth-msg" class="small">${esc(a.msg)}</p>`;
  } else {
    acct = `<p>Sesión iniciada como <b>${esc(s.email)}</b>.</p>
      <div class="row"><button class="btn ghost" id="sync-now">Actualizar ahora</button><button class="btn ghost" id="logout">Cerrar sesión</button></div>
      ${s.otherOwner ? `<p class="small">Este equipo tiene avance de otra cuenta; no se enviará con esta sesión.</p>` : ""}`;
  }
  view.innerHTML = `<section class="hello"><h1>Cuenta</h1></section>
    <section class="panel"><p class="small">La aplicación es gratuita y puedes usarla sin cuenta: tu avance se guarda en este equipo. La cuenta, por ahora disponible solo para usuarios invitados, sirve para ver el mismo avance en varios equipos.</p>${acct}
      <dl class="kv"><dt>Estado</dt><dd>${esc((SYNC_LABEL[s.state] || (() => s.state))(s))}</dd>
      <dt>Última actualización</dt><dd>${s.lastOk ? new Date(s.lastOk).toLocaleString("es-CL") : "—"}</dd>
      ${s.pending ? `<dt>Por guardar</dt><dd>${s.pending}</dd>` : ""}
      ${s.lastError ? `<dt>Detalle</dt><dd class="small">${esc(s.lastError)}</dd>` : ""}</dl>
    </section>
    <p class="small"><a href="https://almanaquedelsaber.cl/privacidad.html" target="_blank" rel="noopener">Privacidad</a> · <a href="https://almanaquedelsaber.cl/privacidad.html#eliminar" target="_blank" rel="noopener">Eliminar mis datos</a> · <a href="https://almanaquedelsaber.cl/empresa.html" target="_blank" rel="noopener">Quiénes somos</a></p>`;
  const fe = $("#f-email");
  if (fe) {
    $("#email").oninput = (ev) => saveAuthDraft({ email: ev.target.value });
    $("#code").oninput = (ev) => saveAuthDraft({ code: ev.target.value });
    fe.onsubmit = async (ev) => {
      ev.preventDefault(); const email = $("#email").value.trim();
      saveAuthDraft({ email, msg: "Enviando…" }); $("#auth-msg").textContent = "Enviando…";
      const err = await sync.requestCode(email);
      const msg = err ? `No pude enviar el código: ${err}` : "Revisa tu correo y escribe el código aquí.";
      saveAuthDraft(err ? { msg } : { msg, codeSent: true, code: "" });
      if ($("#auth-msg")) $("#auth-msg").textContent = msg;
      if (!err && $("#f-code")) { $("#f-code").hidden = false; $("#code").focus(); }
    };
    $("#f-code").onsubmit = async (ev) => {
      ev.preventDefault();
      const err = await sync.verifyCode($("#email").value.trim(), $("#code").value.trim());
      if (err) { const msg = `No pude verificar el código: ${err}`; saveAuthDraft({ msg }); if ($("#auth-msg")) $("#auth-msg").textContent = msg; }
      else { clearAuthDraft(); if ($("#auth-msg")) $("#auth-msg").textContent = "Listo, sesión iniciada."; }
    };
  }
  const sn = $("#sync-now"); if (sn) sn.onclick = () => sync.schedule(0);
  const lo = $("#logout"); if (lo) lo.onclick = () => sync.signOut();
}

// ------------------------------------------------------------ Reproductor de tarjetas
async function openLesson(entry) {
  if (!entry) return;
  const L = await ensureLesson(entry);
  if (!L || !L.tarjetas) { toast("No pude abrir la lección. Revisa tu conexión."); return; }
  let st = lessonState(L);
  if (!st.activeRunId) { await record("lesson_opened", L, { run_id: crypto.randomUUID() }); st = lessonState(L); }
  let attemptId = st.openAttempt?.attempt_id || null;
  if (!attemptId) { attemptId = crypto.randomUUID(); await record("attempt_started", L, { run_id: st.activeRunId, payload: { attempt_id: attemptId } }); }
  const n = L.tarjetas.length;
  const start = !st.completed && st.maxStep > 0 ? Math.min(st.maxStep, n - 1) : 0;
  app.play = { L, entry, i: start, attemptId, startedAt: Date.now(), revealed: new Set() };
  document.body.classList.add("playing");
  player.hidden = false;
  player.dataset.fam = entry.familia;
  renderCard();
}
function closePlayer() {
  app.play = null; player.hidden = true; player.innerHTML = ""; document.body.classList.remove("playing");
  render();
}
const curAttempt = () => lessonState(app.play.L).attempts.find(a => a.attempt_id === app.play.attemptId) || { answers: {}, completed: false };

async function renderCard() {
  const P = app.play; const { L } = P;
  const n = L.tarjetas.length; // la tarjeta n es el resumen
  const st = lessonState(L);
  if (P.i < n) {
    const T = L.tarjetas[P.i];
    if (P.i > st.maxStep) await record("step_reached", L, { run_id: st.activeRunId, payload: { step_id: T.id } });
  } else {
    const a = curAttempt();
    if (!a.completed) {
      const dur = Math.min(86400, Math.max(0, Math.round((Date.now() - P.startedAt) / 1000)));
      await record("lesson_completed", L, { run_id: lessonState(L).activeRunId, payload: { attempt_id: P.attemptId, duration_s: dur } });
      P.justLearned = true;
    }
  }
  const T = P.i < n ? L.tarjetas[P.i] : null;
  const ans = curAttempt().answers || {};
  const blocked = T && T.tipo === "pregunta" && !ans[T.id];
  const bars = Array.from({ length: n + 1 }, (_, k) => `<i class="${k < P.i ? "done" : k === P.i ? "now" : ""}"></i>`).join("");
  player.innerHTML = `<div class="pl-top"><div class="bars">${bars}</div>
      <div class="pl-head"><span class="kicker">${esc(L.disciplina)}</span><button class="x" id="pl-close" aria-label="Cerrar">✕</button></div></div>
    <div class="pl-card ${T ? "t-" + T.tipo : "t-resumen"}" id="pl-card">${T ? cardHtml(L, T, ans) : summaryHtml(L)}</div>
    <div class="pl-nav">${P.i > 0 ? `<button class="btn ghost" id="pl-prev">Atrás</button>` : `<span></span>`}
      ${T ? `<button class="btn" id="pl-next" ${blocked ? "disabled" : ""}>${blocked ? "Elige una respuesta" : P.i === n - 1 ? "Ver resumen" : "Siguiente"}</button>`
          : `<button class="btn" id="pl-done">Terminar</button>`}</div>`;
  $("#pl-close").onclick = closePlayer;
  const pv = $("#pl-prev"); if (pv) pv.onclick = () => step(-1);
  const nx = $("#pl-next"); if (nx) nx.onclick = () => step(1);
  const dn = $("#pl-done"); if (dn) dn.onclick = () => { const first = P.justLearned; closePlayer(); if (first) go("aprendido"); };
  if (T?.tipo === "pregunta") player.querySelectorAll(".opt:not([disabled])").forEach(b => b.onclick = async () => {
    player.querySelectorAll(".opt").forEach(x => x.disabled = true);
    await record("quiz_answered", L, { run_id: lessonState(L).activeRunId, payload: { attempt_id: P.attemptId, question_id: T.id, option_id: b.dataset.o } });
    renderCard();
  });
  if (T?.tipo === "revelar") { const r = $("#reveal"); if (r) r.onclick = () => { P.revealed.add(T.id); renderCard(); }; }
  bindSwipe($("#pl-card"));
}
function step(d) {
  const P = app.play; if (!P) return;
  const n = P.L.tarjetas.length;
  const T = P.i < n ? P.L.tarjetas[P.i] : null;
  if (d > 0 && T?.tipo === "pregunta" && !(curAttempt().answers || {})[T.id]) return;
  P.i = Math.max(0, Math.min(n, P.i + d));
  renderCard();
}
function cardHtml(L, T, ans) {
  const src = T.fuenteIds?.length ? `<p class="src">Fuente: ${T.fuenteIds.map(id => esc(L.fuentes.find(f => f.id === id)?.entidad || id)).join(" · ")}</p>` : "";
  if (T.tipo === "portada") return `${T.visual ? visualHtml(L, T.visual, "hero") : placeholder(L.familia, "hero")}<h1>${esc(T.titulo)}</h1>${T.texto ? `<p class="lead">${esc(T.texto)}</p>` : ""}<p class="hint">Toca Siguiente o desliza para avanzar</p>`;
  if (T.tipo === "idea") return `${visualHtml(L, T.visual)}<h2>${esc(T.titulo)}</h2><p class="lead">${esc(T.texto)}</p>${src}`;
  if (T.tipo === "dato") return `${visualHtml(L, T.visual)}<span class="badge">Dato curioso</span><p class="lead">${esc(T.texto)}</p>${src}`;
  if (T.tipo === "revelar") {
    const open = app.play.revealed.has(T.id);
    return `${visualHtml(L, T.visual)}<h2>${esc(T.titulo)}</h2><p class="lead">${esc(T.texto)}</p>
      ${open ? `<div class="revealed"><p>${esc(T.revelado)}</p></div>${src}` : `<button class="btn reveal" id="reveal">Toca para descubrir</button>`}`;
  }
  if (T.tipo === "pregunta") {
    const chosen = ans[T.id];
    return `<span class="badge">¿Qué crees?</span><h2>${esc(T.pregunta)}</h2><div class="opts">
      ${T.opciones.map(o => { const cls = chosen ? (o.id === T.correctaId ? "right" : o.id === chosen ? "wrong" : "") : ""; return `<button class="opt ${cls}" data-o="${esc(o.id)}" ${chosen ? "disabled" : ""}>${esc(o.texto)}</button>`; }).join("")}</div>
      ${chosen ? `<p class="feedback ${chosen === T.correctaId ? "ok" : "bad"}">${esc(T.opciones.find(o => o.id === chosen)?.retro)}</p>` : `<p class="hint">No hay nota: elige y descubre la respuesta.</p>`}`;
  }
  return `<p>${esc(T.texto || "")}</p>`;
}
function summaryHtml(L) {
  const R = L.resumen;
  return `<span class="badge">Lo que aprendiste</span><h2>${esc(R.titulo)}</h2>
    <ol class="points">${R.puntos.map(p => `<li>${esc(p)}</li>`).join("")}</ol>
    <p class="saved">✓ Guardado en tu colección Aprendido</p>
    <details class="sources"><summary>Fuentes de esta lección</summary><ul>${L.fuentes.map(f => `<li><b>${esc(f.entidad)}</b>, ${esc(f.titulo)}. <a href="${esc(f.url)}" target="_blank" rel="noopener">Abrir fuente</a></li>`).join("")}</ul></details>`;
}
function bindSwipe(el) {
  if (!el) return;
  let x0 = null, y0 = null;
  el.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  el.addEventListener("touchend", (e) => {
    if (x0 == null) return;
    const dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) step(dx < 0 ? 1 : -1);
  }, { passive: true });
}
document.addEventListener("keydown", (e) => {
  if (!app.play) return;
  if (e.key === "ArrowRight") step(1); else if (e.key === "ArrowLeft") step(-1); else if (e.key === "Escape") closePlayer();
});

// ------------------------------------------------------------ utilidades
function toast(t) { const el = $("#toast"); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => el.hidden = true, 2600); }
function setupServiceWorker() {
  if (!("serviceWorker" in navigator)) return;
  navigator.serviceWorker.register("./sw.js").catch(() => {});
  let reloading = false; // la versión nueva toma el control sola; se recarga solo si no hay una lección abierta
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloading && !app.play) { reloading = true; location.reload(); } });
}

// ------------------------------------------------------------ arranque
async function main() {
  for (const t of ROUTES) $("#tab-" + t).onclick = () => go(t);
  $("#sync-pill").onclick = () => go("cuenta");
  const vista = new URLSearchParams(location.search).get("vista");
  if (vista && /^[a-z0-9-]+@[0-9]+$/.test(vista)) { const [id, rev] = vista.split("@"); app.preview = { id, rev: Number(rev) }; }
  const h = location.hash.slice(1);
  if (ROUTES.includes(h)) app.route = h;
  setupServiceWorker();
  [app.catalog, app.calendar, app.approvals] = await Promise.all([loadIndex("catalog.v1.json"), loadIndex("calendar.v1.json"), loadIndex("aprobaciones.v1.json")]);
  await refresh();
  render();
  sync.onStatus(s => { app.syncStatus = s; renderHeader(); const typing = ["email", "code"].includes(document.activeElement?.id); if (app.route === "cuenta" && !app.play && !typing) renderCuenta(); });
  window.addEventListener("almanaque:synced", async () => { await refresh(); if (!app.play) render(); else renderHeader(); });
  document.addEventListener("visibilitychange", async () => { // al volver a la app, trae el contenido nuevo
    if (document.visibilityState !== "visible" || app.play) return;
    [app.catalog, app.calendar, app.approvals] = await Promise.all([loadIndex("catalog.v1.json"), loadIndex("calendar.v1.json"), loadIndex("aprobaciones.v1.json")]);
    render();
  });
  await sync.init();
}
main();
