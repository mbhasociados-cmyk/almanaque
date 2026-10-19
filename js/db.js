// IndexedDB: copia operativa local. Almacenes: lessons, events, meta.
const DB_NAME = "almanaque-v1";
let dbp = null;

function open() {
  if (dbp) return dbp;
  dbp = new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = () => {
      const db = req.result;
      db.createObjectStore("lessons", { keyPath: "key" });
      const ev = db.createObjectStore("events", { keyPath: "id" });
      ev.createIndex("sync", "sync");
      db.createObjectStore("meta", { keyPath: "k" });
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
  return dbp;
}

const done = (tx) => new Promise((res, rej) => { tx.oncomplete = () => res(); tx.onerror = () => rej(tx.error); tx.onabort = () => rej(tx.error); });
const reqp = (r) => new Promise((res, rej) => { r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); });

export async function getMeta(k) { const db = await open(); const v = await reqp(db.transaction("meta").objectStore("meta").get(k)); return v ? v.v : undefined; }
export async function setMeta(k, v) { const db = await open(); const tx = db.transaction("meta", "readwrite"); tx.objectStore("meta").put({ k, v }); return done(tx); }

export async function getLesson(id, rev) { const db = await open(); const v = await reqp(db.transaction("lessons").objectStore("lessons").get(`${id}@${rev}`)); return v ? v.data : null; }
export async function putLesson(data, sha256) { const db = await open(); const tx = db.transaction("lessons", "readwrite"); tx.objectStore("lessons").put({ key: `${data.id}@${data.revision}`, data, sha256, stored_at: new Date().toISOString() }); return done(tx); }
export async function allLessons() { const db = await open(); return reqp(db.transaction("lessons").objectStore("lessons").getAll()); }

export async function allEvents() { const db = await open(); return reqp(db.transaction("events").objectStore("events").getAll()); }
export async function getEvent(id) { const db = await open(); return (await reqp(db.transaction("events").objectStore("events").get(id))) || null; }
export async function putEvent(ev) { const db = await open(); const tx = db.transaction("events", "readwrite"); tx.objectStore("events").put(ev); return done(tx); }
export async function putEvents(evs) { const db = await open(); const tx = db.transaction("events", "readwrite"); const s = tx.objectStore("events"); for (const e of evs) s.put(e); return done(tx); }

export async function pendingForUser(uid) {
  const all = await allEvents();
  return all.filter(e => e.user_id === uid && (e.sync === "pending" || e.sync === "awaiting_confirmation"))
    .sort((a, b) => (a.device_id < b.device_id ? -1 : a.device_id > b.device_id ? 1 : a.device_seq - b.device_seq));
}

// Crea un evento asignando device_id y device_seq en la MISMA transacción.
export async function addEvent(partial) {
  const db = await open();
  const tx = db.transaction(["events", "meta"], "readwrite");
  const meta = tx.objectStore("meta");
  const evs = tx.objectStore("events");
  let result;
  const rDev = meta.get("device");
  rDev.onsuccess = () => {
    let dev = rDev.result ? rDev.result.v : null;
    if (!dev) dev = { device_id: crypto.randomUUID(), device_seq: 0 };
    const rOwner = meta.get("owner");
    rOwner.onsuccess = () => {
      const owner = rOwner.result ? rOwner.result.v : null;
      dev.device_seq += 1;
      result = {
        id: crypto.randomUUID(),
        user_id: owner || null,
        device_id: dev.device_id,
        device_seq: dev.device_seq,
        run_id: partial.run_id || null,
        type: partial.type,
        lesson_id: partial.lesson_id,
        lesson_revision: partial.lesson_revision,
        payload: partial.payload || {},
        client_ts: new Date().toISOString(),
        seq: null, server_ts: null,
        sync: owner ? "pending" : "local",
      };
      evs.put(result);
      meta.put({ k: "device", v: dev });
    };
  };
  await done(tx);
  return result;
}

// Asocia a la cuenta los eventos creados sin sesión, solo si el dispositivo no tiene otro dueño.
export async function adoptLocalEvents(uid) {
  const owner = await getMeta("owner");
  if (owner && owner !== uid) return { adopted: 0, otherOwner: owner };
  await setMeta("owner", uid);
  const all = await allEvents();
  const loose = all.filter(e => !e.user_id).map(e => ({ ...e, user_id: uid, sync: "pending" }));
  if (loose.length) await putEvents(loose);
  return { adopted: loose.length };
}

export const syncDb = { pendingForUser, get: getEvent, put: putEvent, putMany: putEvents, all: allEvents };
