// Service worker: solo la interfaz. Las lecciones viven en IndexedDB (las guarda la app).
// No intercepta peticiones de otros orígenes (Supabase) ni respuestas de autenticación.
const VERSION = "2.1.3";
const CACHE = "almanaque-shell-" + VERSION;
const SHELL = [
  "./", "./index.html", "./styles.css", "./manifest.webmanifest",
  "./js/app.js", "./js/db.js", "./js/state.js", "./js/sync.js", "./js/synccore.js", "./js/sanitize.js", "./js/config.js",
  "./vendor/supabase-2.45.4.js",
  "./fonts/young-serif-latin-400-normal.woff2",
  "./fonts/instrument-sans-latin-400-normal.woff2", "./fonts/instrument-sans-latin-500-normal.woff2", "./fonts/instrument-sans-latin-600-normal.woff2",
  "./fonts/ibm-plex-mono-latin-400-normal.woff2", "./fonts/ibm-plex-mono-latin-500-normal.woff2",
  "./icons/icon-192.png", "./icons/icon-512.png", "./icons/maskable-512.png", "./icons/apple-touch-icon.png",
];
const SHELL_URLS = new Set(SHELL.map(p => new URL(p, self.registration.scope).href));

self.addEventListener("install", (event) => {
  // cache: "reload" evita que la versión nueva se instale con archivos viejos guardados por el navegador.
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL.map(p => new Request(p, { cache: "reload" })))));
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    for (const name of await caches.keys()) if (name.startsWith("almanaque-shell-") && name !== CACHE) await caches.delete(name);
    await self.clients.claim();
  })());
});

self.addEventListener("message", (event) => { if (event.data === "SKIP_WAITING") self.skipWaiting(); });

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (req.mode === "navigate") {
    event.respondWith(caches.open(CACHE).then(c => c.match(new URL("./index.html", self.registration.scope).href)).then(r => r || fetch(req)));
    return;
  }
  const clean = url.origin + url.pathname;
  if (!SHELL_URLS.has(clean)) return; // datos y lecciones: red; la app conserva la última versión válida
  event.respondWith(caches.open(CACHE).then(async c => (await c.match(clean)) || fetch(req)));
});
