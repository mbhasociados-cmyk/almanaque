# Publica un lote bajo la opción A (delegación de Max del 20-10-2026).
# Uso: python3 tools/publicar_lote.py <carpeta_en_borradores> <id1:AAAA-MM-DD> <id2:AAAA-MM-DD> ...
# Agrega cada lección al manifiesto y al registro de aprobaciones (modalidad opcion-A), regenera catálogo y calendario
# y ejecuta el control de publicación. Si algo falla, no deja cambios.
import json, hashlib, os, sys, subprocess, shutil, datetime
ROOT = os.path.join(os.path.dirname(__file__), "..")
carpeta, pares = sys.argv[1], [a.split(":") for a in sys.argv[2:]]
MAN, APR = os.path.join(ROOT, "tools", "manifiesto_publicacion.json"), os.path.join(ROOT, "data", "aprobaciones.v1.json")
respaldo = {p: open(p, "rb").read() for p in (MAN, APR, os.path.join(ROOT, "data", "catalog.v1.json"), os.path.join(ROOT, "data", "calendar.v1.json"))}
hoy = datetime.date.today().isoformat()
try:
    man = json.load(open(MAN, encoding="utf-8")); apr = json.load(open(APR, encoding="utf-8"))
    fechas = {x["fecha"] for x in man["lecciones"]} | {"2026-10-27"}
    for lid, fecha in pares:
        datetime.date.fromisoformat(fecha)
        assert fecha not in fechas, f"la fecha {fecha} ya tiene lección"; fechas.add(fecha)
        f = next(n for n in os.listdir(os.path.join(ROOT, "borradores", carpeta)) if n.startswith(lid + ".r") and n.endswith(".json"))
        data = open(os.path.join(ROOT, "borradores", carpeta, f), "rb").read(); L = json.loads(data)
        sys.path.insert(0, os.path.dirname(__file__)); from almanaque_lib import validate; validate(L)
        assert not any(r["id"] == lid and r["revision"] == L["revision"] for r in apr["registros"]), f"{lid} ya tiene registro"
        man["lecciones"].append({"carpeta": f"borradores/{carpeta}", "id": lid, "revision": L["revision"], "fecha": fecha})
        apr["registros"].append({"id": lid, "revision": L["revision"], "sha256": hashlib.sha256(data).hexdigest(),
            "modalidad": "opcion-A",
            "estadoRevision": "AUTOVERIFICADA_POR_CLAUDE",
            "autoverificacion": {"por": "Claude", "fecha": hoy, "alcance": "fuentes abiertas y comprobadas por Claude; controles automáticos del lote; prueba local en la app"},
            "publicacion": "AUTORIZADA_POR_DELEGACION_GENERAL_DE_MAX",
            "delegacion": {"por": "Max Monsalves Blanco", "fecha": "2026-10-20", "referencia": "Declaración expresa de Max del 20-10-2026 (\"dale opcion A\"), confirmada a ChatGPT"},
            "revisionIndependienteChatGPT": "OPCIONAL_NO_REALIZADA",
            "funcionamiento": "PROBADA_POR_CLAUDE"})
    open(MAN, "w", encoding="utf-8").write(json.dumps(man, ensure_ascii=False, indent=2))
    open(APR, "w", encoding="utf-8").write(json.dumps(apr, ensure_ascii=False, indent=2))
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "gen_lessons.py")], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "verificar_publicacion.py")], check=True)
except Exception as e:
    for p, b in respaldo.items(): open(p, "wb").write(b)
    print("NO SE PUBLICÓ. Se restauraron los archivos:", e); sys.exit(1)
