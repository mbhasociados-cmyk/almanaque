# Control de publicación (pedido por ChatGPT en su respuesta al N°19).
# Comprueba que archivo, catálogo, calendario y registro de aprobaciones coinciden en id, revisión y SHA-256.
# Uso: python3 tools/verificar_publicacion.py [carpeta_raiz]   (por defecto, la carpeta del proyecto)
import json, hashlib, os, sys
from collections import Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")
# Versiones que Max revisó una por una (huellas verificadas por ChatGPT en N°14, N°17 y N°18).
# Desde el 20-10-2026 (opción A) Max delegó la producción y publicación en Claude: esas lecciones llevan modalidad "opcion-A" en su registro.
APROBADAS_POR_MAX = {
    ("cielo-azul", 3): "e68c9e3315f25ced78fbbb61402dfcf06ed892d51700fd33282fa443bff8a8a8",
    ("pan-duro", 2): "3adc5f6d782087f383b1aa5dd7b41762af3b8adbf292847087ad3ff864d21a05",
    ("temblores-chile", 2): "fea71cf537e4cc0ed41eb4500f1ae10aa21d460e48ce9a4a5e62a7f82da2ac00",
    ("unidad-fomento", 2): "eae96171f04f74038eaf3ebd49e6aa5b275976ba96472d611285f540bad71d0b",
    ("fases-luna", 2): "6cc20cb48916ab368ec0365a96ede9cf9072b595e4bef64b934884484611b70f",
    ("gabriela-mistral", 3): "790672c9d8268907e56798e8d2a2ceb7a377b8d7297036d66a717f828a084351",
    ("como-funciona-gps", 3): "312b7c592e8c6e0c39b777a26395f22607d16330a3dcbbce8759b9f306e3171e",
    ("mar-salado", 2): "f048712c30906637637731978d5b2aa345e2aed290b416d3dc95492146fe3d75",
}
errores = []
def err(m): errores.append(m)
load = lambda p: json.load(open(os.path.join(ROOT, p), encoding="utf-8"))
cat, cal, apr = load("data/catalog.v1.json"), load("data/calendar.v1.json"), load("data/aprobaciones.v1.json")

# 1. Registros: sin duplicados por (id, revisión)
cuenta = Counter((r["id"], r["revision"]) for r in apr["registros"])
for k, n in cuenta.items():
    if n > 1: err(f"registro duplicado: {k} aparece {n} veces")
reg = {(r["id"], r["revision"]): r for r in apr["registros"]}

def opcion_a(r):
    d = r.get("delegacion") or {}
    return (r.get("modalidad") == "opcion-A" and r.get("estadoRevision") == "AUTOVERIFICADA_POR_CLAUDE"
            and r.get("publicacion") == "AUTORIZADA_POR_DELEGACION_GENERAL_DE_MAX" and bool(d.get("por") and d.get("fecha")))
def verificado(r):
    if opcion_a(r): return True
    v = r.get("verificacion") or {}
    return (v.get("resultado") == "aprobado" or v.get("estado") == "verificado") and v.get("revisor") and v.get("fecha")
def con_vb(r):
    if opcion_a(r): return True
    return bool((r.get("vb") or {}).get("por") and (r.get("vb") or {}).get("fecha"))

# 2. Catálogo: sin duplicados; la huella declarada coincide con el archivo
cuenta_cat = Counter((l["id"], l["revision"]) for l in cat["lecciones"])
for k, n in cuenta_cat.items():
    if n > 1: err(f"catálogo duplicado: {k}")
catk = {}
for l in cat["lecciones"]:
    k = (l["id"], l["revision"]); catk[k] = l
    ruta = os.path.join(ROOT, l["archivo"])
    if not os.path.exists(ruta): err(f"falta el archivo {l['archivo']}"); continue
    data = open(ruta, "rb").read(); sha = hashlib.sha256(data).hexdigest()
    if sha != l["sha256"]: err(f"huella del catálogo distinta del archivo: {k}")
    js = json.loads(data)
    if (js["id"], js["revision"]) != k: err(f"id o revisión del archivo no coincide con el catálogo: {l['archivo']}")
    if js.get("schemaVersion") != l.get("schemaVersion"): err(f"esquema distinto entre archivo y catálogo: {k}")

# 3. Calendario: una lección por fecha; cada entrada existe en el catálogo
cuenta_fechas = Counter(e["fecha"] for e in cal["entradas"])
for f, n in cuenta_fechas.items():
    if n > 1: err(f"la fecha {f} tiene {n} lecciones")
for e in cal["entradas"]:
    k = (e["id"], e["revision"])
    if k not in catk: err(f"calendario {e['fecha']} apunta a {k}, que no está en el catálogo")

# 4. Lecciones en tarjetas (las que muestra la app v3): publicadas = verificación + V°B° + misma huella
publicadas = []
for k, l in catk.items():
    if l.get("schemaVersion") != "2.0": continue
    r = reg.get(k)
    if r is None:
        if any(e["id"] == k[0] and e["revision"] == k[1] for e in cal["entradas"]):
            err(f"{k} está en el calendario sin registro de aprobación")
        continue
    if r["sha256"] != l["sha256"]: err(f"huella del registro distinta del catálogo: {k}"); continue
    if not verificado(r): err(f"{k} tiene registro sin verificación válida"); continue
    if not con_vb(r): err(f"{k} tiene registro sin V°B° de Max"); continue
    if l.get("estado") != "publicado": err(f"{k}: el catálogo no la marca como publicada")
    publicadas.append(k)

# 5. Lo publicado es exactamente lo que Max aprobó, y todo lo aprobado está publicado y programado
for k in publicadas:
    if k in APROBADAS_POR_MAX:
        if APROBADAS_POR_MAX[k] != catk[k]["sha256"]: err(f"{k} publicada con una huella distinta de la que revisó Max")
    elif not opcion_a(reg[k]):
        # Fuera de la lista revisada por Max, solo se admite lo publicado bajo la delegación general (opción A, 20-10-2026)
        err(f"{k} publicada sin estar en la lista revisada por Max ni en la modalidad opción A")
    elif "vb" in reg[k]:
        err(f"{k}: un registro de opción A no puede llevar V°B° individual de Max")
for k, sha in APROBADAS_POR_MAX.items():
    if k not in publicadas: err(f"{k} aprobada por Max pero no publicada")
    elif not any(e["id"] == k[0] and e["revision"] == k[1] for e in cal["entradas"]):
        nueva = [e for e in cal["entradas"] if e["id"] == k[0] and e["revision"] > k[1] and (e["id"], e["revision"]) in publicadas]
        if not nueva: err(f"{k} publicada pero sin fecha en el calendario")

# 6. Una misma lección no aparece en el calendario con dos revisiones distintas
revs = {}
for e in cal["entradas"]:
    revs.setdefault(e["id"], set()).add(e["revision"])
for i, s in revs.items():
    if len(s) > 1: err(f"{i} aparece en el calendario con revisiones {sorted(s)}")

for k in sorted(publicadas, key=lambda k: next((e["fecha"] for e in cal["entradas"] if (e["id"], e["revision"]) == k), "")):
    f = next((e["fecha"] for e in cal["entradas"] if (e["id"], e["revision"]) == k), "—")
    print(f"OK  {f}  {k[0]} r{k[1]}  {catk[k]['sha256'][:12]}")
if errores:
    print("\nRECHAZADO:"); [print(" -", e) for e in errores]; sys.exit(1)
print(f"\nCUMPLE: {len(publicadas)} lecciones publicadas; cada una con verificación y con V°B° individual de Max o publicada bajo la opción A, con su huella exacta.")
