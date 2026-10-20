// Almanaque del Saber — estado derivado (función pura y determinista).
// Reglas acordadas en mensajes Claude N°3–N°4 / ChatGPT N°3–N°4.

export const INTERVALS = [1, 3, 7, 21];
export const TZ = "America/Santiago";

const fmt = new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" });
export function chileDate(d) { return fmt.format(d instanceof Date ? d : new Date(d)); }
export function addDays(iso, n) {
  const [y, m, d] = iso.split("-").map(Number);
  const t = new Date(Date.UTC(y, m - 1, d + n));
  return t.toISOString().slice(0, 10); // fecha civil pura, sin zona
}
export function weekStart(iso) { // lunes de la semana de iso
  const [y, m, d] = iso.split("-").map(Number);
  const dow = new Date(Date.UTC(y, m - 1, d)).getUTCDay(); // 0 domingo
  return addDays(iso, -((dow + 6) % 7));
}

// Orden canónico: primero los eventos con seq del servidor, por seq;
// después los provisionales, por (device_id, device_seq). Nunca por reloj.
export function canonicalOrder(events) {
  const canon = events.filter(e => e.seq != null).sort((a, b) => a.seq - b.seq);
  const prov = events.filter(e => e.seq == null)
    .sort((a, b) => (a.device_id < b.device_id ? -1 : a.device_id > b.device_id ? 1 : a.device_seq - b.device_seq));
  return canon.concat(prov);
}

const key = (id, rev) => `${id}@${rev}`;
// Preguntas de una lección: esquema 1.x (quiz) o 2.0 (tarjetas de tipo "pregunta").
export const questionsOf = (lesson) => lesson.tarjetas ? lesson.tarjetas.filter(t => t.tipo === "pregunta") : (lesson.quiz || []);

// lessons: Map "id@rev" -> lección (esquema 1.0). Puede faltar contenido: en ese caso
// los eventos se conservan pero no se interpretan pasos ni puntajes.
export function deriveState(events, lessons, todayIso = chileDate(new Date())) {
  const ordered = canonicalOrder(events.filter(e => e.sync !== "invalid"));
  const L = new Map(); // key -> estado por lección y revisión
  const library = new Map(); // lesson_id -> {saved, revision}
  const reviewEvents = [];
  const activity = []; // {date, kind}

  const get = (e) => {
    const k = key(e.lesson_id, e.lesson_revision);
    if (!L.has(k)) L.set(k, { lesson_id: e.lesson_id, revision: e.lesson_revision, runs: new Map(), firstOpenRun: null, lastRestartRun: null, attempts: new Map(), completedAttempts: [] });
    return L.get(k);
  };
  const run = (st, id) => {
    if (!st.runs.has(id)) st.runs.set(id, { run_id: id, maxStep: -1, revealed: new Set(), attemptIds: [] });
    return st.runs.get(id);
  };

  for (const e of ordered) {
    const st = (e.type === "library_saved" || e.type === "library_removed" || e.type === "review_graded") ? null : get(e);
    const lesson = lessons.get(key(e.lesson_id, e.lesson_revision));
    switch (e.type) {
      case "lesson_opened": {
        run(st, e.run_id);
        if (!st.firstOpenRun) st.firstOpenRun = e.run_id;
        break;
      }
      case "lesson_restarted": {
        run(st, e.run_id);
        st.lastRestartRun = e.run_id;
        break;
      }
      case "step_reached": {
        const r = run(st, e.run_id);
        const idx = lesson ? (lesson.tarjetas || lesson.pasos).findIndex(p => p.id === e.payload.step_id) : -1;
        if (idx > r.maxStep) r.maxStep = idx;
        break;
      }
      case "activity_revealed": {
        run(st, e.run_id).revealed.add(e.payload.step_id);
        break;
      }
      case "attempt_started": {
        const id = e.payload.attempt_id;
        if (!st.attempts.has(id)) {
          st.attempts.set(id, { attempt_id: id, run_id: e.run_id, answers: new Map(), completed: false, duration_s: null, completedAt: null });
          run(st, e.run_id).attemptIds.push(id);
        }
        break;
      }
      case "quiz_answered": {
        const a = st.attempts.get(e.payload.attempt_id);
        if (!a || a.completed) break;                 // intento completado no se reabre
        if (!a.answers.has(e.payload.question_id))    // cuenta la primera respuesta canónica
          a.answers.set(e.payload.question_id, e.payload.option_id);
        break;
      }
      case "lesson_completed": {
        const a = st.attempts.get(e.payload.attempt_id);
        if (!a || a.completed) break;
        a.completed = true;
        a.duration_s = e.payload.duration_s;
        a.completedAt = e.client_ts;
        st.completedAttempts.push(a);
        activity.push({ date: chileDate(e.client_ts), kind: "lesson" });
        break;
      }
      case "library_saved": library.set(e.lesson_id, { saved: true, revision: e.lesson_revision }); break;
      case "library_removed": library.set(e.lesson_id, { saved: false, revision: e.lesson_revision }); break;
      case "review_graded": reviewEvents.push(e); activity.push({ date: chileDate(e.client_ts), kind: "review" }); break;
    }
  }

  // Recorrido activo y puntajes recalculados desde el contenido
  const perLesson = new Map();
  for (const st of L.values()) {
    const activeRunId = st.lastRestartRun || st.firstOpenRun || null;
    const lesson = lessons.get(key(st.lesson_id, st.revision));
    const r = activeRunId ? st.runs.get(activeRunId) : null;
    const score = (a) => {
      if (!lesson) return null;
      let ok = 0;
      for (const qq of questionsOf(lesson)) if (a.answers.get(qq.id) === qq.correctaId) ok++;
      return ok;
    };
    const attempts = [...st.attempts.values()].map(a => ({ ...a, answers: Object.fromEntries(a.answers), score: score(a), of: lesson ? questionsOf(lesson).length : null }));
    const openAttempt = r ? attempts.filter(a => a.run_id === r.run_id && !a.completed).pop() || null : null;
    perLesson.set(key(st.lesson_id, st.revision), {
      lesson_id: st.lesson_id, revision: st.revision,
      activeRunId, maxStep: r ? r.maxStep : -1, revealed: r ? [...r.revealed] : [],
      attempts, openAttempt,
      completed: st.completedAttempts.length > 0,
      firstCompletedAt: st.completedAttempts[0]?.completedAt || null,
      bestScore: attempts.filter(a => a.completed).reduce((m, a) => Math.max(m, a.score ?? 0), -1),
    });
  }

  // Tarjetas de repaso: nacen al completar la lección por primera vez (nivel 0, vence en 1 día)
  const cards = new Map(); // "lesson_id:review_id" -> card
  for (const pl of perLesson.values()) {
    if (!pl.completed) continue;
    const lesson = lessons.get(key(pl.lesson_id, pl.revision));
    if (!lesson) continue;
    const base = chileDate(pl.firstCompletedAt);
    for (const r of lesson.repaso || []) {
      const k = `${pl.lesson_id}:${r.id}`;
      if (!cards.has(k)) cards.set(k, { key: k, lesson_id: pl.lesson_id, revision: pl.revision, review_id: r.id, pregunta: r.pregunta, respuesta: r.respuesta, level: 0, due: addDays(base, INTERVALS[0]), history: [] });
    }
  }
  const seenReviewAttempts = new Set();
  for (const e of reviewEvents) {
    const c = cards.get(`${e.lesson_id}:${e.payload.review_id}`);
    if (!c || seenReviewAttempts.has(e.payload.review_attempt_id)) continue;
    seenReviewAttempts.add(e.payload.review_attempt_id);
    const d = chileDate(e.client_ts); // la fecha declarada orienta el calendario; no resuelve conflictos
    const g = e.payload.grade;
    if (g === 2) { c.level = Math.min(c.level + 1, INTERVALS.length - 1); c.due = addDays(d, INTERVALS[c.level]); }
    else if (g === 1) { c.due = addDays(d, 1); }
    else { c.level = 0; c.due = addDays(d, INTERVALS[0]); }
    c.history.push({ date: d, grade: g, received: e.server_ts || null });
  }
  const dueCards = [...cards.values()].filter(c => c.due <= todayIso).sort((a, b) => (a.due < b.due ? -1 : a.due > b.due ? 1 : a.key < b.key ? -1 : 1));

  const ws = weekStart(todayIso);
  const weekDays = new Set(activity.filter(a => a.date >= ws && a.date <= todayIso).map(a => a.date));
  const weekReviews = activity.filter(a => a.kind === "review" && a.date >= ws && a.date <= todayIso).length;

  return {
    perLesson, library, cards, dueCards,
    week: { start: ws, learningDays: weekDays.size, reviews: weekReviews },
  };
}
