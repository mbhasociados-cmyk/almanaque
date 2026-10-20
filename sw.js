// Service worker v3: la app funciona en línea. Siempre pide a la red y usa la copia guardada
// solo si la red falla un momento. No intercepta otros orígenes (Supabase) ni los datos de lecciones.
const VERSION = "3.0.0";
const CACHE = "almanaque-shell-" + VERSION;

self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    for (const name of await caches.keys()) if (name !== CACHE) await caches.delete(name);
    await self.clients.claim();
  })());
});
self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.includes("/data/")) return; // catálogo, calendario, aprobaciones y lecciones: siempre red
  event.respondWith((async () => {
    try {
      const res = await fetch(req, { cache: "no-store" });
      if (res.ok) (await caches.open(CACHE)).put(req, res.clone());
      return res;
    } catch {
      const hit = await caches.match(req, { ignoreSearch: true });
      if (hit) return hit;
      if (req.mode === "navigate") { const idx = await caches.match(new URL("./index.html", self.registration.scope).href); if (idx) return idx; }
      throw new Error("sin red");
    }
  })());
});
