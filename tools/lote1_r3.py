# Lote 1, revisión 3: solo gabriela-mistral y como-funciona-gps (ajustes de ChatGPT N°17).
# Parte del archivo r2 exacto y cambia únicamente los campos indicados. Las otras cinco lecciones siguen en r2.
import json, hashlib, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
R2, R3 = os.path.join(ROOT, "borradores", "lote1_r2"), os.path.join(ROOT, "borradores", "lote1_r3")
os.makedirs(R3, exist_ok=True)
dump = lambda L: json.dumps(L, ensure_ascii=False, indent=2).encode("utf-8")
CAMBIOS = {
  "gabriela-mistral": [("c6", "texto",
     "También escribió canciones y poemas para niños, como los de «Ternura», de 1924. Por eso muchas personas la recuerdan como madre y maestra.",
     "También escribió canciones y poemas para niños, como los de «Ternura», de 1924. Durante mucho tiempo, su imagen pública quedó asociada a las figuras de «madre» y «maestra».")],
  "como-funciona-gps": [("c5", "titulo", "Con cuatro basta", "Por lo menos cuatro"),
     ("c7", "opciones.c.retro", "Hay al menos 24 en órbita, pero para calcular la posición le basta con cuatro o más.",
      "Hay al menos 24 en órbita, pero el mínimo para calcular la posición es conocer la distancia a cuatro.")],
}
for lid, cambios in CAMBIOS.items():
    raw = open(os.path.join(R2, f"{lid}.r2.json"), "rb").read(); L = json.loads(raw)
    assert dump(L) == raw
    L["revision"] = 3
    T = {t["id"]: t for t in L["tarjetas"]}
    for cid, campo, antes, ahora in cambios:
        if campo.startswith("opciones."):
            _, oid, k = campo.split("."); obj = next(o for o in T[cid]["opciones"] if o["id"] == oid)
        else: obj, k = T[cid], campo
        assert obj[k] == antes, (lid, cid, campo); obj[k] = ahora
    open(os.path.join(R3, f"{lid}.r3.json"), "wb").write(dump(L))
