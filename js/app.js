// Almanaque del Saber — interfaz
import { CONFIG } from "./config.js";
import * as db from "./db.js";
import * as sync from "./sync.js";
import { deriveState, chileDate } from "./state.js";
import { sanitizeSvg } from "./sanitize.js";

const $ = (s, el = document) => el.querySelector(s);
const view = $("#view");
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const app = {
  catalog: null, calendar: null, lessons: new Map(), state: null,
  route: "hoy", filter: "Todas", session: null, reviewSession: null,
  syncStatus: null, swReg: null, updateWaiting: false, downloading: new Set(), importPreview: null,
};

// ------------------------------------------------------------ datos
async function fetchJson(url, ms = 4000) {
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), ms);
  try {
    const r = await fetch(url, { signal: ctl.signal, cache: "no-cache" });
    if (!r.ok) throw new Error("HTTP " + r.status);
    return { json: await r.json(), bytes: null };
  } finally { clearTimeout(t); }
}

async function loadIndex(name, metaKey) {
  try {
    const { json } = await fetchJson(`data/${name}`);
    await db.setMeta(metaKey, json);
    return json;
  } catch {
    return (await db.getMeta(metaKey)) || null; // última versión válida guardada
  }
}

async function sha256Hex(buf) {
  const h = await crypto.subtle.digest("SHA-256", buf);
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, "0")).join("");
}

// Descarga una lección, verifica su hash contra el catálogo y la guarda. Solo entonces queda "disponible sin conexión".
async function ensureLesson(entry) {
  const k = `${entry.id}@${entry.revision}`;
  if (app.lessons.has(k)) return app.lessons.get(k);
  const stored = await db.getLesson(entry.id, entry.revision);
  if (stored) { app.lessons.set(k, stored); return stored; }
  if (app.downloading.has(k)) return null;
  app.downloading.add(k);
  try {
    const r = await fetch(entry.archivo, { cache: "no-cache" });
    if (!r.ok) throw new Error("HTTP " + r.status);
    const buf = await r.arrayBuffer();
    const hash = await sha256Hex(buf);
    if (entry.sha256 && hash !== entry.sha256) throw new Error("La lección descargada no coincide con el catálogo");
    const data = JSON.parse(new TextDecoder().decode(buf));
    await db.putLesson(data, hash);
    app.lessons.set(k, data);
    requestPersistence();
    return data;
  } catch (e) {
    return null;
  } finally { app.downloading.delete(k); }
}

async function requestPersistence() {
  if (!navigator.storage?.persist) return;
  if ((await db.getMeta("persist")) === true) return;
  try { await db.setMeta("persist", await navigator.storage.persist()); } catch { /* sin soporte */ }
}

const catEntry = (id, rev) => app.catalog?.lecciones.find(l => l.id === id && (rev == null || l.revision === rev));
const REVIEW_MODE = CONFIG.MODO_REVISION === true; // por defecto false: solo lecciones publicadas
// Autoridad editorial: data/aprobaciones.v1.json. Se recalcula aquí, sin confiar en el estado del catálogo.
// Publicado solo si hay un único registro coherente para (id, revisión), con el mismo SHA-256 del catálogo
// (que a su vez se comprueba contra el archivo descargado), verificación "aprobado" y V°B°.
function editorialState(entry) {
  if (!entry) return "excluido";
  const regs = (app.approvals?.registros || []).filter(r => r.id === entry.id && r.revision === entry.revision);
  if (!regs.length) return "borrador";
  if (regs.length > 1 || regs.some(r => r.sha256 !== entry.sha256)) return "excluido";
  const r = regs[0];
  const verified = r.verificacion && r.verificacion.resultado === "aprobado" && r.verificacion.revisor && r.verificacion.fecha;
  if (!verified) return "borrador";
  if (r.vb && r.vb.por && r.vb.fecha) return "publicado";
  return "verificado";
}
function visible(entry) { const st = editorialState(entry); return st === "publicado" || (REVIEW_MODE && st !== "excluido"); }
function todayIso() { return chileDate(new Date()); }
function todayEntry() {
  const e = app.calendar?.entradas.find(x => x.fecha === todayIso());
  return e ? catEntry(e.id, e.revision) : null;
}

async function prefetch() {
  if (!app.catalog) return;
  const today = todayIso();
  const want = new Set();
  for (const e of app.calendar?.entradas || []) if (e.fecha >= today && e.fecha <= addDaysIso(today, 7)) want.add(`${e.id}@${e.revision}`);
  for (const [id, v] of app.state?.library || []) if (v.saved) want.add(`${id}@${v.revision}`);
  for (const k of want) { const [id, rev] = k.split("@"); const c = catEntry(id, Number(rev)); if (c && visible(c)) await ensureLesson(c); }
}
function addDaysIso(iso, n) { const [y, m, d] = iso.split("-").map(Number); return new Date(Date.UTC(y, m - 1, d + n)).toISOString().slice(0, 10); }

async function refresh() {
  for (const row of await db.allLessons()) app.lessons.set(row.key, row.data);
  app.state = deriveState(await db.allEvents(), app.lessons, todayIso());
}

async function record(type, lesson, extra = {}) {
  await db.addEvent({ type, lesson_id: lesson.id ?? lesson.lesson_id, lesson_revision: lesson.revision, ...extra });
  sync.schedule(2000);
  await refresh();
}

const lessonState = (L) => app.state?.perLesson.get(`${L.id}@${L.revision}`) || { activeRunId: null, maxStep: -1, attempts: [], openAttempt: null, completed: false, revealed: [] };
const isOffline = (id, rev) => app.lessons.has(`${id}@${rev}`);

// ------------------------------------------------------------ cabecera
const SYNC_LABEL = {
  local: () => "Guardado en este dispositivo",
  needs_login: () => "Inicia sesión para sincronizar",
  idle: () => "Preparando…",
  syncing: () => "Sincronizando…",
  synced: () => "Avance sincronizado",
  pending: (s) => `Pendiente de sincronizar (${s.pending})`,
  offline: (s) => s.pending ? `Sin conexión · ${s.pending} pendientes` : "Sin conexión",
  unreachable: () => "No pude conectar",
  server: () => "No pude conectar",
  unknown: () => "No pude conectar",
  auth: () => "Vuelve a iniciar sesión",
  permission: () => "Cuenta no habilitada",
  other_owner: () => "Equipo asociado a otra cuenta",
};
const SYNC_TONE = { synced: "ok", local: "neutral", syncing: "neutral", idle: "neutral", pending: "warn", offline: "warn", needs_login: "warn" };

function renderHeader() {
  const s = app.syncStatus || sync.status;
  const pill = $("#sync-pill");
  pill.textContent = (SYNC_LABEL[s.state] || (() => s.state))(s);
  pill.dataset.tone = SYNC_TONE[s.state] || "bad";
  const due = app.state?.dueCards.length || 0;
  $("#tab-repasar").textContent = due ? `Repasar · ${due}` : "Repasar";
  for (const t of ["hoy", "repasar", "explorar", "biblioteca", "cuenta"]) $("#tab-" + t).setAttribute("aria-current", app.route === t ? "page" : "false");
  $("#update-bar").hidden = !app.updateWaiting;
  $("#review-bar").hidden = !REVIEW_MODE;
}

function go(route) {
  app.route = route; app.session = null; app.reviewSession = null;
  if (location.hash !== "#" + route) history.replaceState(null, "", "#" + route);
  render();
}

function render() {
  app.coverEntry = null;
  renderHeader();
  if (app.session) return renderLesson();
  ({ hoy: renderHoy, repasar: renderRepasar, explorar: renderExplorar, biblioteca: renderBiblioteca, cuenta: renderCuenta }[app.route] || renderHoy)();
  window.scrollTo({ top: 0 });
}

// ------------------------------------------------------------ Hoy
function weekStrip() {
  const w = app.state?.week || { learningDays: 0, reviews: 0 };
  return `<div class="week"><span><b>${w.learningDays}</b> ${w.learningDays === 1 ? "día" : "días"} de aprendizaje esta semana</span><span><b>${w.reviews}</b> ${w.reviews === 1 ? "concepto repasado" : "conceptos repasados"}</span></div>`;
}

function renderHoy() {
  const entry = todayEntry();
  const now = new Date();
  const hoy = todayIso();
  const [, , dd] = hoy.split("-").map(Number);
  const dow = new Date(hoy + "T12:00:00Z").getUTCDay();
  const mm = Number(hoy.split("-")[1]) - 1;
  const fecha = `${DIAS[dow]} · ${dd} de ${MESES[mm]} de ${hoy.slice(0, 4)}`;
  if (!entry || !visible(entry)) {
    view.innerHTML = `${weekStrip()}<article class="leaf"><div class="leaf-head"><div class="daynum">${dd}</div><div><div class="daymeta">${fecha}</div><h1>Aún no hay lección publicada para hoy</h1></div></div>
      <div class="leaf-body"><p class="lede">Puedes elegir cualquier lección del archivo o hacer tus repasos pendientes.</p><div class="row"><button class="btn" data-go="explorar">Ir a Explorar</button><button class="btn ghost" data-go="repasar">Repasar</button></div></div></article>`;
    bindGo(); return;
  }
  renderCover(entry, { isToday: true, dd, fecha });
}

function bindGo() { view.querySelectorAll("[data-go]").forEach(b => b.onclick = () => go(b.dataset.go)); }

async function renderCover(entry, opts = {}) {
  app.coverEntry = entry;
  const L = app.lessons.get(`${entry.id}@${entry.revision}`);
  const offline = Boolean(L);
  const st = L ? lessonState(L) : null;
  const est = editorialState(entry);
  const draft = est !== "publicado";
  let primary = "Comenzar lección";
  if (st?.completed) primary = "Repasar lección";
  else if (st && st.maxStep >= 0) primary = `Retomar desde el avance alcanzado (paso ${st.maxStep + 1})`;
  view.innerHTML = `${opts.isToday ? weekStrip() : ""}<article class="leaf">
    <div class="leaf-head"><div class="daynum">${opts.isToday ? opts.dd : "§"}</div>
      <div><div class="daymeta">${opts.isToday ? esc(opts.fecha) : "Lección del archivo"}</div>
      <h1>${esc(entry.titulo)}</h1>
      <div class="chips-row"><span class="disc">${esc(entry.disciplina)}</span>${draft ? `<span class="chip-flag">${est === "verificado" ? "Verificada · pendiente de V°B°" : "Borrador · pendiente de verificación"}</span>` : ""}</div></div></div>
    <div class="leaf-body">
      ${L ? `<ul class="goals">${L.objetivos.map(o => `<li>${esc(o)}</li>`).join("")}</ul>` : ""}
      <div class="facts"><span>Duración <b>${entry.minutosEstimados} min</b></span>${L ? `<span>Pasos <b>${L.pasos.length}</b></span><span>Preguntas <b>${L.quiz.length}</b></span>` : ""}
        <span class="${offline ? "ok" : "muted"}">${offline ? "Disponible sin conexión en este dispositivo" : (navigator.onLine ? "Descargando…" : "No descargada en este dispositivo")}</span></div>
      ${st?.completed ? `<p class="small">Mejor resultado: ${st.bestScore} de ${L.quiz.length}. Intentos: ${st.attempts.filter(a => a.completed).length}.</p>` : ""}
      <div class="row"><button class="btn" id="start" ${L ? "" : "disabled"}>${primary}</button>
        ${!opts.isToday ? `<button class="btn ghost" id="back">Volver</button>` : ""}
        ${st?.activeRunId ? `<button class="btn link" id="restart">Reiniciar lección</button>` : ""}</div>
      <div id="confirm-restart" hidden class="note">Reiniciar crea un recorrido nuevo desde el comienzo. Los intentos y el avance anteriores quedan en tu historial. <div class="row"><button class="btn" id="restart-yes">Reiniciar</button><button class="btn ghost" id="restart-no">Cancelar</button></div></div>
    </div></article>`;
  if (!L) ensureLesson(entry).then(() => refresh()).then(() => { if (!app.session && app.coverEntry === entry) renderCover(entry, opts); });
  const s = $("#start"); if (s) s.onclick = () => startLesson(L, { fromToday: opts.isToday });
  const b = $("#back"); if (b) b.onclick = () => go(app.route);
  const r = $("#restart"); if (r) r.onclick = () => { $("#confirm-restart").hidden = false; };
  const ry = $("#restart-yes"); if (ry) ry.onclick = async () => { await record("lesson_restarted", L, { run_id: crypto.randomUUID() }); startLesson(L, { fromToday: opts.isToday, fresh: true }); };
  const rn = $("#restart-no"); if (rn) rn.onclick = () => { $("#confirm-restart").hidden = true; };
}

// ------------------------------------------------------------ Lección
async function startLesson(L, opts = {}) {
  let st = lessonState(L);
  if (!st.activeRunId) { await record("lesson_opened", L, { run_id: crypto.randomUUID() }); st = lessonState(L); }
  let step = "entrada";
  if (!opts.fresh && !st.completed && st.maxStep >= 0) step = st.maxStep;
  else if ((app.state?.dueCards.length || 0) > 0) step = "recuperar";
  app.session = { L, step, startedAt: Date.now(), attemptId: null, fromToday: opts.fromToday, recovered: 0 };
  render();
}

function progressBar(L, step) {
  const total = L.pasos.length + 3; // entrada + pasos + evaluación + cierre
  const pos = step === "recuperar" ? 0 : step === "entrada" ? 1 : step === "quiz" ? L.pasos.length + 2 : step === "cierre" ? total : step + 2;
  const label = step === "recuperar" ? "Recuperar" : step === "entrada" ? "Descubrir" : step === "quiz" ? "Comprobar" : step === "cierre" ? "Cerrar" : `Comprender · paso ${step + 1} de ${L.pasos.length}`;
  return `<div class="stephead"><span>${esc(L.disciplina.toUpperCase())} · ${esc(L.titulo)}</span><span>${label}</span></div><div class="progress"><i style="width:${Math.round(pos / total * 100)}%"></i></div>`;
}

function renderLesson() {
  const { L, step } = app.session;
  if (step === "recuperar") return renderRecover();
  if (step === "entrada") return renderEntrada();
  if (step === "quiz") return renderQuiz();
  if (step === "cierre") return renderCierre();
  return renderStep(step);
}

function leaf(inner) { view.innerHTML = `<article class="leaf"><div class="leaf-body pad-top">${inner}</div></article>`; window.scrollTo({ top: 0 }); }
function exitLesson() { const r = app.session?.fromToday ? "hoy" : app.route; app.session = null; go(r); }

function renderRecover() {
  const { L } = app.session;
  const card = app.state.dueCards[0];
  if (!card || app.session.recovered >= 2) { app.session.step = "entrada"; return renderEntrada(); }
  leaf(`${progressBar(L, "recuperar")}
    <h2>Antes de empezar, recupera</h2><p class="small">Responde de memoria. Son ${Math.min(2, app.state.dueCards.length) - app.session.recovered} ${Math.min(2, app.state.dueCards.length) - app.session.recovered === 1 ? "pregunta" : "preguntas"} de lecciones anteriores.</p>
    ${reviewCardHtml(card)}
    <div class="row"><button class="btn link" id="skip">Saltar repaso</button></div>`);
  bindReviewCard(card, async () => { app.session.recovered++; renderRecover(); });
  $("#skip").onclick = () => { app.session.step = "entrada"; renderEntrada(); };
}

function renderEntrada() {
  const { L } = app.session;
  leaf(`${progressBar(L, "entrada")}
    <h2>${esc(L.entrada.pregunta)}</h2>
    <label class="small" for="idea">Tu idea inicial (opcional, no se guarda ni se sincroniza)</label>
    <textarea id="idea" rows="3"></textarea>
    <p class="section-title">Al terminar podrás</p><ul class="goals">${L.objetivos.map(o => `<li>${esc(o)}</li>`).join("")}</ul>
    <div class="row"><button class="btn ghost" id="prev">Salir</button><button class="btn" id="next">Comenzar</button></div>`);
  $("#prev").onclick = exitLesson;
  $("#next").onclick = () => { app.session.step = 0; renderLesson(); };
}

function figureHtml(L, f, i) {
  const clean = sanitizeSvg(f.contenido, L.id);
  if (!clean) return `<div class="figure-alt">${esc(f.alt)}</div>`;
  return `<figure class="as-figure"><div class="figure">${clean}</div><figcaption class="figcap">${esc(f.pie)}</figcaption><p class="sr-only">${esc(f.alt)}</p></figure>`;
}

async function renderStep(i) {
  const { L } = app.session;
  const S = L.pasos[i];
  const st = lessonState(L);
  if (i > st.maxStep) await record("step_reached", L, { run_id: st.activeRunId, payload: { step_id: S.id } });
  const revealed = lessonState(L).revealed.includes(S.id);
  const A = S.actividad;
  leaf(`${progressBar(L, i)}
    <section class="step"><h2>${esc(S.titulo)}</h2>${S.parrafos.map(p => `<p>${esc(p)}</p>`).join("")}
      ${S.figura ? figureHtml(L, S.figura, i) : ""}
      ${A ? `<div class="activity"><span class="act-kind">${{ prediccion: "Predice", calculo: "Calcula", explicacion: "Explica" }[A.tipo] || "Actividad"}</span><p>${esc(A.pregunta)}</p>
        <button class="btn link" id="rev" aria-expanded="${revealed}">${revealed ? "Ocultar respuesta" : "Ver respuesta"}</button><div id="ans" ${revealed ? "" : "hidden"}>${esc(A.respuesta)}</div></div>` : ""}
      <p class="sources-inline">Fuentes: ${S.fuenteIds.map(id => { const f = L.fuentes.find(x => x.id === id); return f ? esc(f.entidad) : esc(id); }).join(" · ")}</p>
    </section>
    <div class="row"><button class="btn ghost" id="prev">${i === 0 ? "Volver" : "Anterior"}</button><button class="btn" id="next">${i === L.pasos.length - 1 ? "Ir a la evaluación" : "Siguiente"}</button></div>`);
  const rev = $("#rev");
  if (rev) rev.onclick = async () => {
    const a = $("#ans"); a.hidden = !a.hidden; rev.textContent = a.hidden ? "Ver respuesta" : "Ocultar respuesta"; rev.setAttribute("aria-expanded", String(!a.hidden));
    if (!a.hidden && !lessonState(L).revealed.includes(S.id)) await record("activity_revealed", L, { run_id: lessonState(L).activeRunId, payload: { step_id: S.id } });
  };
  $("#prev").onclick = () => { app.session.step = i === 0 ? "entrada" : i - 1; renderLesson(); };
  $("#next").onclick = () => { app.session.step = i === L.pasos.length - 1 ? "quiz" : i + 1; renderLesson(); };
}

async function renderQuiz() {
  const { L } = app.session;
  let st = lessonState(L);
  if (!app.session.attemptId) {
    if (st.openAttempt) app.session.attemptId = st.openAttempt.attempt_id; // continúa el mismo intento (también desde otro equipo)
    else { const id = crypto.randomUUID(); await record("attempt_started", L, { run_id: st.activeRunId, payload: { attempt_id: id } }); app.session.attemptId = id; }
    st = lessonState(L);
  }
  const att = st.attempts.find(a => a.attempt_id === app.session.attemptId) || { answers: {}, completed: false };
  const answers = att.answers || {};
  leaf(`${progressBar(L, "quiz")}
    <h2>Comprueba lo aprendido</h2>
    ${L.quiz.map((q, qi) => {
      const chosen = answers[q.id];
      return `<fieldset class="q"><legend>${qi + 1}. ${esc(q.pregunta)}</legend>
        ${q.opciones.map(o => {
          const cls = chosen ? (o.id === q.correctaId ? "right" : o.id === chosen ? "wrong" : "") : "";
          return `<button class="opt ${cls}" data-q="${q.id}" data-o="${o.id}" ${chosen ? "disabled" : ""}>${esc(o.texto)}</button>`;
        }).join("")}
        ${chosen ? `<p class="feedback ${chosen === q.correctaId ? "ok" : "bad"}">${esc(q.opciones.find(o => o.id === chosen)?.retroalimentacion)}</p>` : ""}
      </fieldset>`;
    }).join("")}
    <div class="row"><button class="btn ghost" id="prev">Volver a los pasos</button>${att.completed ? `<button class="btn" id="next">Continuar</button>` : ""}</div>`);
  view.querySelectorAll(".opt:not([disabled])").forEach(b => b.onclick = async () => {
    view.querySelectorAll(`.opt[data-q="${b.dataset.q}"]`).forEach(x => x.disabled = true);
    await record("quiz_answered", L, { run_id: lessonState(L).activeRunId, payload: { attempt_id: app.session.attemptId, question_id: b.dataset.q, option_id: b.dataset.o } });
    const a2 = lessonState(L).attempts.find(a => a.attempt_id === app.session.attemptId);
    if (a2 && !a2.completed && L.quiz.every(q => a2.answers[q.id])) {
      const dur = Math.min(86400, Math.max(0, Math.round((Date.now() - app.session.startedAt) / 1000)));
      await record("lesson_completed", L, { run_id: lessonState(L).activeRunId, payload: { attempt_id: app.session.attemptId, duration_s: dur } });
    }
    renderQuiz();
  });
  $("#prev").onclick = () => { app.session.step = L.pasos.length - 1; renderLesson(); };
  const n = $("#next"); if (n) n.onclick = () => { app.session.step = "cierre"; renderLesson(); };
}

function renderCierre() {
  const { L } = app.session;
  const st = lessonState(L);
  const att = st.attempts.find(a => a.attempt_id === app.session.attemptId);
  const saved = app.state.library.get(L.id)?.saved;
  const mins = att?.duration_s != null ? Math.round(att.duration_s / 60) : null;
  leaf(`${progressBar(L, "cierre")}
    <h2>Cierre</h2><p>${esc(L.cierre)}</p>
    ${att ? `<div class="note"><span class="score">${att.score} de ${att.of} correctas</span><br><span class="small">Tiempo en esta sesión: ${mins} min (redondeado). Un resultado inmediato no acredita dominio: los repasos te lo mostrarán en 1, 3, 7 y 21 días.</span></div>` : ""}
    <details class="sources"><summary>Fuentes de esta lección</summary><ul>${L.fuentes.map(f => `<li><b>${esc(f.entidad)}</b>, ${esc(f.titulo)}. ${esc(f.ubicacion)}. <a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.url)}</a>${f.consultadaEl ? ` (consultada el ${esc(f.consultadaEl)})` : " (pendiente de verificación)"}</li>`).join("")}</ul></details>
    <div class="row"><button class="btn" id="save">${saved ? "Quitar de mi biblioteca" : "Guardar en mi biblioteca"}</button><button class="btn ghost" id="home">Terminar</button></div>`);
  $("#save").onclick = async () => { await record(saved ? "library_removed" : "library_saved", L); toast(saved ? "Lección quitada de tu biblioteca" : "Lección guardada en tu biblioteca"); renderCierre(); };
  $("#home").onclick = exitLesson;
}

// ------------------------------------------------------------ Repasar
function reviewCardHtml(c) {
  const L = app.lessons.get(`${c.lesson_id}@${c.revision}`);
  return `<div class="review-card"><div class="small">${esc(L?.titulo || c.lesson_id)}</div><p class="rq">${esc(c.pregunta)}</p>
    <button class="btn ghost" id="show">Mostrar respuesta</button>
    <div id="rans" hidden><p class="ra">${esc(c.respuesta)}</p><p class="small">¿Cómo te fue?</p>
    <div class="row"><button class="btn grade" data-g="0">No recordé</button><button class="btn grade" data-g="1">Recordé parcialmente</button><button class="btn grade" data-g="2">Recordé</button></div></div></div>`;
}
function bindReviewCard(c, after) {
  $("#show").onclick = () => { $("#rans").hidden = false; $("#show").hidden = true; };
  view.querySelectorAll(".grade").forEach(b => b.onclick = async () => {
    view.querySelectorAll(".grade").forEach(x => x.disabled = true);
    await record("review_graded", { lesson_id: c.lesson_id, revision: c.revision }, { payload: { review_id: c.review_id, review_attempt_id: crypto.randomUUID(), grade: Number(b.dataset.g) } });
    after();
  });
}

function renderRepasar() {
  const due = app.state?.dueCards || [];
  app.reviewSession = app.reviewSession || { done: 0 };
  if (!due.length) {
    view.innerHTML = `${weekStrip()}<div class="empty"><h2>No tienes repasos pendientes</h2><p>Cuando termines una lección, sus conceptos volverán aquí al día siguiente, y después a los 3, 7 y 21 días.</p></div>`;
    return;
  }
  const c = due[0];
  const over = app.reviewSession.done >= 4;
  view.innerHTML = `${weekStrip()}<article class="leaf"><div class="leaf-body pad-top">
    <div class="stephead"><span>REPASO</span><span>${due.length} ${due.length === 1 ? "pendiente" : "pendientes"}</span></div>
    ${over ? `<p class="note">Ya llevas unos dos minutos de repaso. Puedes seguir o dejar el resto para mañana; nada se pierde.</p>` : ""}
    ${reviewCardHtml(c)}</div></article>`;
  bindReviewCard(c, () => { app.reviewSession.done++; renderHeader(); renderRepasar(); });
}

// ------------------------------------------------------------ Explorar y Biblioteca
function lessonCard(e, extra = "") {
  return `<button class="card" data-id="${esc(e.id)}" data-rev="${e.revision}"><span class="disc">${esc(e.disciplina)}</span><h3>${esc(e.titulo)}</h3>
    <span class="date">${e.minutosEstimados} min${isOffline(e.id, e.revision) ? " · sin conexión ✓" : ""}${editorialState(e) === "verificado" ? " · verificada" : editorialState(e) !== "publicado" ? " · borrador" : ""}${extra}</span></button>`;
}
function bindCards() {
  view.querySelectorAll(".card").forEach(c => c.onclick = () => { const e = catEntry(c.dataset.id, Number(c.dataset.rev)); renderCover(e, { isToday: false }); });
}

function renderExplorar() {
  const list = (app.catalog?.lecciones || []).filter(visible);
  const discs = ["Todas", ...new Set(list.map(l => l.disciplina))];
  const shown = list.filter(l => app.filter === "Todas" || l.disciplina === app.filter);
  view.innerHTML = `<div class="stack"><p class="section-title">Archivo de lecciones</p>
    <div class="chips">${discs.map(d => `<button class="chip" aria-pressed="${d === app.filter}" data-d="${esc(d)}">${esc(d)}</button>`).join("")}</div>
    ${shown.length ? `<div class="lib-grid">${shown.map(e => lessonCard(e)).join("")}</div>` : `<div class="empty">No hay lecciones disponibles${navigator.onLine ? "" : " sin conexión"}.</div>`}</div>`;
  view.querySelectorAll(".chip").forEach(c => c.onclick = () => { app.filter = c.dataset.d; renderExplorar(); });
  bindCards();
}

function renderBiblioteca() {
  const lib = [...(app.state?.library || [])].filter(([, v]) => v.saved).map(([id, v]) => catEntry(id, v.revision)).filter(visible);
  const done = [...(app.state?.perLesson.values() || [])].filter(p => p.completed).map(p => catEntry(p.lesson_id, p.revision)).filter(visible).filter(e => !lib.includes(e));
  const extra = (e) => { const p = app.state.perLesson.get(`${e.id}@${e.revision}`); return p?.completed ? ` · mejor ${p.bestScore}/${app.lessons.get(`${e.id}@${e.revision}`)?.quiz.length ?? "?"}` : ""; };
  view.innerHTML = `<div class="stack"><p class="section-title">Guardadas · ${lib.length}</p>
    ${lib.length ? `<div class="lib-grid">${lib.map(e => lessonCard(e, extra(e))).join("")}</div>` : `<div class="empty">Aún no guardas lecciones. Al terminar una lección, pulsa “Guardar en mi biblioteca”.</div>`}
    ${done.length ? `<p class="section-title">Terminadas sin guardar · ${done.length}</p><div class="lib-grid">${done.map(e => lessonCard(e, extra(e))).join("")}</div>` : ""}</div>`;
  bindCards();
}

// ------------------------------------------------------------ Cuenta
async function renderCuenta() {
  const s = app.syncStatus || sync.status;
  const persist = await db.getMeta("persist");
  const dev = await db.getMeta("device");
  let acct = "";
  if (!sync.isEnabled()) {
    acct = `<p>La app funciona en <b>modo local</b>: tu avance queda guardado solo en este dispositivo. Para compartirlo entre el PC y el celular hay que configurar la conexión (archivo <code>js/config.js</code>, ver instrucciones).</p>`;
  } else if (!sync.currentUser()) {
    acct = `<form id="f-email" class="form"><label for="email">Correo</label><input id="email" type="email" autocomplete="email" required placeholder="tu@correo.cl">
      <button class="btn" type="submit">Enviar código</button></form>
      <form id="f-code" class="form" hidden><label for="code">Código de 6 dígitos recibido por correo</label><input id="code" inputmode="numeric" autocomplete="one-time-code" pattern="[0-9]{6}" maxlength="6" required>
      <button class="btn" type="submit">Ingresar</button></form><p id="auth-msg" class="small"></p>
      <p class="small">El código se escribe aquí mismo, dentro de la app. Puedes pedir uno nuevo cada 60 segundos.</p>`;
  } else {
    acct = `<p>Sesión iniciada como <b>${esc(s.email)}</b>.</p>
      <div class="row"><button class="btn" id="sync-now">Sincronizar ahora</button><button class="btn ghost" id="logout">Cerrar sesión</button></div>
      ${s.otherOwner ? `<p class="note">Este equipo ya tiene avance asociado a otra cuenta; no se enviará con esta sesión.</p>` : ""}`;
  }
  const m = s.metrics;
  view.innerHTML = `<div class="stack">
    <section class="panel"><h2>Cuenta y sincronización</h2>${acct}
      <dl class="kv"><dt>Estado</dt><dd>${esc((SYNC_LABEL[s.state] || (() => s.state))(s))}</dd>
      <dt>Última sincronización</dt><dd>${s.lastOk ? new Date(s.lastOk).toLocaleString("es-CL") : "—"}</dd>
      <dt>${sync.isEnabled() ? "Pendientes en este equipo" : "Registros guardados solo aquí"}</dt><dd>${s.pending}</dd>
      ${s.conflicts ? `<dt>Conflictos</dt><dd>${s.conflicts} (se conservan las copias locales)</dd>` : ""}
      ${s.invalid ? `<dt>Eventos rechazados</dt><dd>${s.invalid}</dd>` : ""}
      ${m ? `<dt>Último ciclo</dt><dd>${m.sent} enviados · ${m.received} recibidos · ${(m.bytesIn / 1024).toFixed(1)} KB · ${m.ms} ms</dd>` : ""}
      ${s.lastError ? `<dt>Detalle</dt><dd class="small">${esc(s.lastError)}</dd>` : ""}</dl>
      <p class="small">“Avance sincronizado” significa que este equipo envió todo y recibió lo último disponible. El otro equipo puede tener avances sin conexión que llegarán cuando se conecte.</p>
    </section>
    <section class="panel"><h2>Este dispositivo</h2>
      <dl class="kv"><dt>Lecciones disponibles sin conexión</dt><dd>${app.lessons.size}</dd>
      <dt>Almacenamiento persistente</dt><dd>${persist === true ? "Concedido" : persist === false ? "No concedido por el navegador" : "Aún no solicitado"}</dd>
      <dt>Identificador</dt><dd class="mono small">${esc(dev?.device_id || "—")}</dd></dl>
      <div class="row"><button class="btn ghost" id="dl-week">Descargar próxima semana</button></div>
    </section>
    <section class="panel"><h2>Respaldo opcional</h2>
      <p class="small">Exporta tu historial a un archivo JSON. Importarlo fusiona por identificador de evento: no duplica ni reemplaza tu avance.</p>
      <div class="row"><button class="btn ghost" id="export">Exportar respaldo</button><label class="btn ghost" for="import">Importar respaldo</label><input id="import" type="file" accept="application/json,.json" hidden></div>
      <div id="import-preview"></div>
    </section></div>`;

  const fe = $("#f-email");
  if (fe) {
    fe.onsubmit = async (ev) => { ev.preventDefault(); const email = $("#email").value.trim(); $("#auth-msg").textContent = "Enviando…"; const err = await sync.requestCode(email); $("#auth-msg").textContent = err ? `No pude enviar el código: ${err}` : "Revisa tu correo y escribe el código."; if (!err) { $("#f-code").hidden = false; $("#code").focus(); } };
    $("#f-code").onsubmit = async (ev) => { ev.preventDefault(); const err = await sync.verifyCode($("#email").value.trim(), $("#code").value.trim()); $("#auth-msg").textContent = err ? `No pude verificar el código: ${err}` : "Sesión iniciada."; };
  }
  const sn = $("#sync-now"); if (sn) sn.onclick = () => sync.schedule(0);
  const lo = $("#logout"); if (lo) lo.onclick = async () => { await sync.signOut(); };
  $("#dl-week").onclick = async () => { await prefetch(); await refresh(); toast("Lecciones de la próxima semana descargadas"); renderCuenta(); };
  $("#export").onclick = exportBackup;
  $("#import").onchange = (ev) => previewImport(ev.target.files[0]);
}

async function exportBackup() {
  const data = { format: "almanaque-respaldo", version: 1, exported_at: new Date().toISOString(), device: await db.getMeta("device"), owner: (await db.getMeta("owner")) || null, events: await db.allEvents(), lessons: (await db.allLessons()).map(l => ({ sha256: l.sha256, data: l.data })) };
  const blob = new Blob([JSON.stringify(data, null, 1)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `almanaque-respaldo-${todayIso()}.json`;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}

async function previewImport(file) {
  const box = $("#import-preview");
  if (!file) return;
  let data;
  try { data = JSON.parse(await file.text()); } catch { box.innerHTML = `<p class="note">El archivo no es un JSON válido.</p>`; return; }
  if (data?.format !== "almanaque-respaldo" || data.version !== 1 || !Array.isArray(data.events)) { box.innerHTML = `<p class="note">El archivo no es un respaldo del Almanaque (formato o versión no reconocidos).</p>`; return; }
  const owner = (await db.getMeta("owner")) || null;
  const plan = { add: [], same: 0, conflict: 0, foreign: 0, lessons: [] };
  for (const e of data.events) {
    if (!e?.id || !e.type || !e.lesson_id) continue;
    if (e.user_id && owner && e.user_id !== owner) { plan.foreign++; continue; }
    const l = await db.getEvent(e.id);
    if (!l) plan.add.push(e);
    else if (JSON.stringify([l.type, l.lesson_id, l.lesson_revision, l.payload, l.run_id]) === JSON.stringify([e.type, e.lesson_id, e.lesson_revision, e.payload, e.run_id])) plan.same++;
    else plan.conflict++;
  }
  for (const l of data.lessons || []) if (l?.data?.id && !app.lessons.has(`${l.data.id}@${l.data.revision}`)) plan.lessons.push(l);
  app.importPreview = plan;
  box.innerHTML = `<div class="note">Vista previa: <b>${plan.add.length}</b> eventos nuevos, ${plan.same} ya existentes, ${plan.conflict} con contenido distinto (se conserva la copia local), ${plan.foreign} de otra cuenta (se omiten), ${plan.lessons.length} lecciones nuevas.
    <div class="row"><button class="btn" id="imp-yes" ${plan.add.length || plan.lessons.length ? "" : "disabled"}>Importar</button><button class="btn ghost" id="imp-no">Cancelar</button></div></div>`;
  $("#imp-no").onclick = () => { box.innerHTML = ""; app.importPreview = null; };
  $("#imp-yes").onclick = async () => {
    const own = (await db.getMeta("owner")) || null;
    await db.putEvents(plan.add.map(e => ({ ...e, user_id: e.user_id || own, sync: (e.user_id || own) ? (e.seq != null ? "awaiting_confirmation" : "pending") : "local" })));
    for (const l of plan.lessons) await db.putLesson(l.data, l.sha256);
    await refresh(); sync.schedule(0);
    toast(`Importados ${plan.add.length} eventos`); box.innerHTML = "";
  };
}

// ------------------------------------------------------------ utilidades UI
function toast(t) { const el = $("#toast"); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => el.hidden = true, 2400); }

function setupServiceWorker() {
  if (!("serviceWorker" in navigator)) return;
  navigator.serviceWorker.register("./sw.js").then(reg => {
    app.swReg = reg;
    const markWaiting = () => { if (reg.waiting && navigator.serviceWorker.controller) { app.updateWaiting = true; renderHeader(); } };
    markWaiting();
    reg.addEventListener("updatefound", () => { const w = reg.installing; w?.addEventListener("statechange", () => { if (w.state === "installed") markWaiting(); }); });
  }).catch(() => {});
  let reloading = false;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloading) { reloading = true; location.reload(); } });
  $("#update-btn").onclick = () => {
    if (app.session?.step === "quiz") { toast("Termina la evaluación y vuelve a pulsar Actualizar"); return; }
    app.swReg?.waiting?.postMessage("SKIP_WAITING");
  };
}

// ------------------------------------------------------------ arranque
async function main() {
  for (const t of ["hoy", "repasar", "explorar", "biblioteca", "cuenta"]) $("#tab-" + t).onclick = () => go(t);
  $("#sync-pill").onclick = () => go("cuenta");
  const h = location.hash.slice(1);
  if (["hoy", "repasar", "explorar", "biblioteca", "cuenta"].includes(h)) app.route = h;
  setupServiceWorker();
  [app.catalog, app.calendar, app.approvals] = await Promise.all([loadIndex("catalog.v1.json", "catalog"), loadIndex("calendar.v1.json", "calendar"), loadIndex("aprobaciones.v1.json", "aprobaciones")]);
  await refresh();
  render();
  sync.onStatus(s => { app.syncStatus = s; renderHeader(); if (app.route === "cuenta" && !app.session) renderCuenta(); });
  window.addEventListener("almanaque:synced", async () => { await refresh(); await prefetch(); await refresh(); if (!app.session) render(); else renderHeader(); });
  await sync.init();
  await prefetch(); await refresh();
  if (!app.session) render();
}
main();
