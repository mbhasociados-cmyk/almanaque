// Sanitizador de SVG por lista permitida (convención .as-svg__*).
// Rechaza scripts, eventos, estilos, colores literales y referencias externas.
const ELEMENTS = new Set(["svg", "g", "path", "line", "polyline", "polygon", "rect", "circle", "ellipse", "text", "tspan", "title", "desc", "defs", "marker"]);
const ATTRS = new Set(["xmlns", "viewBox", "width", "height", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry", "d", "points", "transform", "class", "text-anchor", "font-size", "stroke-width", "stroke-dasharray", "id", "refX", "refY", "markerWidth", "markerHeight", "orient", "marker-end", "marker-start", "role", "aria-label", "aria-hidden"]);
const CLASSES = new Set(["as-svg", "as-svg__ink", "as-svg__muted", "as-svg__accent", "as-svg__surface", "as-svg__label", "as-svg__hit"]);
const NUMERIC = /^[-0-9.,\s eE]*$/;

export function sanitizeSvg(src, lessonId) {
  if (typeof src !== "string" || src.length > 60000) return null;
  const doc = new DOMParser().parseFromString(src, "image/svg+xml");
  if (doc.getElementsByTagName("parsererror").length) return null;
  const root = doc.documentElement;
  if (root.localName !== "svg") return null;
  const idPrefix = lessonId + "-";
  const walk = (el) => {
    for (const child of [...el.children]) {
      if (!ELEMENTS.has(child.localName)) { child.remove(); continue; }
      walk(child);
    }
    for (const a of [...el.attributes]) {
      const n = a.name, v = a.value;
      let ok = ATTRS.has(n);
      if (ok && n === "class") { const kept = v.split(/\s+/).filter(c => CLASSES.has(c)); if (kept.length) el.setAttribute("class", kept.join(" ")); else el.removeAttribute("class"); continue; }
      if (ok && n === "id") ok = v.startsWith(idPrefix) && /^[a-z0-9-]+$/.test(v);
      if (ok && (n === "marker-end" || n === "marker-start")) ok = new RegExp("^url\\(#" + idPrefix.replace(/[-]/g, "\\-") + "[a-z0-9-]+\\)$").test(v);
      if (ok && n === "transform") ok = /^(\s*(translate|scale|rotate)\([-0-9.,\s]+\)\s*)+$/.test(v);
      if (ok && ["x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry", "width", "height", "font-size", "stroke-width", "stroke-dasharray", "refX", "refY", "markerWidth", "markerHeight", "points", "viewBox"].includes(n)) ok = NUMERIC.test(v);
      if (ok && n === "d") ok = /^[MmLlHhVvCcSsQqTtAaZz0-9.,\s-]*$/.test(v);
      if (!ok) el.removeAttribute(n);
    }
  };
  walk(root);
  root.setAttribute("class", "as-svg");
  root.setAttribute("focusable", "false");
  return new XMLSerializer().serializeToString(root);
}
