// Copia la interfaz web (sin los datos) a www/ para empaquetarla en la app Android.
// Los datos (catálogo, calendario, lecciones) se piden en línea al sitio publicado.
import { cpSync, rmSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
const out = join(dirname(fileURLToPath(import.meta.url)), "..", "www");
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
for (const item of ["index.html", "styles.css", "manifest.webmanifest", "js", "vendor", "fonts", "icons"]) {
  cpSync(join(root, item), join(out, item), { recursive: true });
}
console.log("Interfaz copiada a", out);
