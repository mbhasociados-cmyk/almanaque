// Conexión con Supabase: sesión por código de correo y ciclo de sincronización.
import { CONFIG } from "./config.js";
import { syncOnce, backoffDelay } from "./synccore.js";
import * as db from "./db.js";

const enabled = Boolean(CONFIG.SUPABASE_URL && CONFIG.SUPABASE_ANON_KEY && window.supabase);
let client = null;
let user = null;
let running = false, again = false, timer = null, failures = 0;
const listeners = new Set();
export const status = { mode: enabled ? "cloud" : "local", state: enabled ? "idle" : "local", pending: 0, lastOk: null, lastError: null, kind: null, metrics: null, email: null, otherOwner: null };

function emit() { for (const f of listeners) f({ ...status }); }
export function onStatus(f) { listeners.add(f); f({ ...status }); return () => listeners.delete(f); }

async function countPending() {
  const all = await db.allEvents();
  status.pending = all.filter(e => e.sync === "pending" || e.sync === "awaiting_confirmation" || e.sync === "local").length;
  status.conflicts = all.filter(e => e.sync === "conflict").length;
  status.invalid = all.filter(e => e.sync === "invalid").length;
}

export function makeRemote(c) { return {
  async insertIgnore(rows) {
    try {
      const { error } = await c.from("events").upsert(rows, { onConflict: "id", ignoreDuplicates: true });
      return { error };
    } catch (e) { return { error: e }; }
  },
  async fetchPage(from, to) {
    try {
      const { data, error } = await c.from("events").select("*").order("seq", { ascending: true }).range(from, to);
      return { data: data || [], error };
    } catch (e) { return { data: [], error: e }; }
  },
}; }
let remote = null;

export async function init() {
  await countPending();
  if (!enabled) { status.state = "local"; emit(); return; }
  client = window.supabase.createClient(CONFIG.SUPABASE_URL, CONFIG.SUPABASE_ANON_KEY, {
    auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: false, storageKey: "almanaque-auth" },
  });
  remote = makeRemote(client);
  const { data } = await client.auth.getSession();
  await setUser(data.session?.user || null);
  client.auth.onAuthStateChange((_ev, session) => { setUser(session?.user || null); });
  window.addEventListener("online", () => schedule(0));
  window.addEventListener("offline", () => { status.state = "offline"; emit(); });
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "visible") schedule(0); });
  schedule(0);
}

async function setUser(u) {
  const changed = (u?.id || null) !== (user?.id || null);
  user = u;
  status.email = u?.email || null;
  if (u) {
    const r = await db.adoptLocalEvents(u.id);
    status.otherOwner = r.otherOwner || null;
  }
  await countPending();
  if (!u) status.state = "needs_login";
  emit();
  if (changed && u) schedule(0);
}

export function isEnabled() { return enabled; }
export function currentUser() { return user; }

export async function requestCode(email) {
  const { error } = await client.auth.signInWithOtp({ email, options: { shouldCreateUser: false } });
  return error ? (error.message || "No pude enviar el código") : null;
}
export async function verifyCode(email, token) {
  const { error } = await client.auth.verifyOtp({ email, token, type: "email" });
  return error ? (error.message || "Código no válido") : null;
}
export async function signOut() { await client.auth.signOut(); }

// Programa una sincronización (debounce); una sola a la vez.
export function schedule(delay = 2000) {
  if (!enabled) { countPending().then(emit); return; }
  clearTimeout(timer);
  timer = setTimeout(run, delay);
}

async function run() {
  if (running) { again = true; return; }
  if (!user) { status.state = "needs_login"; await countPending(); emit(); return; }
  if (status.otherOwner) { status.state = "other_owner"; emit(); return; }
  if (!navigator.onLine) { status.state = "offline"; await countPending(); emit(); return; }
  running = true; status.state = "syncing"; emit();
  try {
    const res = await syncOnce({ db: db.syncDb, remote, uid: user.id });
    if (res.ok) {
      failures = 0; status.lastOk = new Date().toISOString(); status.lastError = null; status.kind = null; status.metrics = res.metrics;
    } else {
      failures++; status.kind = res.kind; status.lastError = String(res.error?.message || res.error || "");
      if (res.kind === "auth") { /* se conservan los pendientes; se pedirá autenticación */ }
      clearTimeout(timer);
      if (res.kind === "network" || res.kind === "server" || res.kind === "unknown") timer = setTimeout(run, backoffDelay(failures));
    }
  } finally {
    running = false;
    await countPending();
    status.state = status.kind ? (status.kind === "network" ? (navigator.onLine ? "unreachable" : "offline") : status.kind) : (status.pending ? "pending" : "synced");
    emit();
    window.dispatchEvent(new CustomEvent("almanaque:synced"));
    if (again) { again = false; schedule(500); }
  }
}
