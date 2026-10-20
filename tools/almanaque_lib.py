# Biblioteca común para producir lecciones en tarjetas (esquema 2.0). La usan los scripts de tools/lotes/.
import json, hashlib, os
ROOT = os.path.join(os.path.dirname(__file__), "..")

def card(id, tipo, **k):
    c = {"id": id, "tipo": tipo}
    for key in ("titulo", "texto", "revelado", "pregunta", "correctaId"):
        if k.get(key) is not None: c[key] = k[key]
    if "opciones" in k: c["opciones"] = [dict(id=o[0], texto=o[1], retro=o[2]) for o in k["opciones"]]
    c["fuenteIds"] = k.get("fuentes", [])
    return c

def src(id, entidad, titulo, url, ubicacion, afirmaciones, respalda, consultada):
    return dict(id=id, entidad=entidad, titulo=titulo, url=url, ubicacion=ubicacion,
                afirmaciones=afirmaciones, respalda=respalda, consultadaEl=consultada)

def lesson(id, disciplina, familia, titulo, subtitulo, tarjetas, resumen, fuentes, revision=1, minutos=5):
    return {"schemaVersion": "2.0", "id": id, "revision": revision, "idioma": "es-CL",
            "disciplina": disciplina, "familia": familia, "titulo": titulo, "subtitulo": subtitulo,
            "minutosEstimados": minutos, "tarjetas": tarjetas,
            "resumen": {"titulo": resumen[0], "puntos": resumen[1]}, "fuentes": fuentes,
            "controlEditorial": {"estado": "borrador", "revisadoPor": None, "fechaRevision": None}}

FAMILIAS = {"fisica", "astronomia", "biologia", "salud", "quimica", "cocina", "historia", "arte", "matematica", "tecnologia", "geografia", "economia", "sociedad", "literatura"}

def validate(L):
    """Controles del lote: rechaza la lección si falla cualquiera."""
    assert L["schemaVersion"] == "2.0" and L["familia"] in FAMILIAS, L["id"]
    assert 6 <= len(L["tarjetas"]) <= 9, (L["id"], "tarjetas")
    assert any(t["tipo"] == "pregunta" for t in L["tarjetas"]), (L["id"], "sin pregunta")
    assert 2 <= len(L["resumen"]["puntos"]) <= 3, (L["id"], "resumen")
    assert len({t["id"] for t in L["tarjetas"]}) == len(L["tarjetas"]), (L["id"], "ids repetidos")
    ids = {f["id"] for f in L["fuentes"]}
    for f in L["fuentes"]:
        assert f["url"].startswith("https://") and f["consultadaEl"] and f["afirmaciones"], (L["id"], f["id"])
        for c in f["respalda"]:
            assert f["id"] in next(t for t in L["tarjetas"] if t["id"] == c)["fuenteIds"], (L["id"], f["id"], c)
    for t in L["tarjetas"]:
        assert t["fuenteIds"], ("tarjeta sin fuente", L["id"], t["id"])
        assert set(t["fuenteIds"]) <= ids, (L["id"], t["id"])
        for f in L["fuentes"]:
            if f["id"] in t["fuenteIds"]: assert t["id"] in f["respalda"], (L["id"], t["id"], f["id"])
        if t["tipo"] == "pregunta":
            assert len(t["opciones"]) == 3 and t["correctaId"] in {o["id"] for o in t["opciones"]}, (L["id"], t["id"])

def write(lote_dir, lessons):
    """Valida y escribe cada lección en borradores/<lote_dir>/<id>.r<rev>.json. Devuelve [(id, rev, sha)]."""
    out = os.path.join(ROOT, "borradores", lote_dir); os.makedirs(out, exist_ok=True); res = []
    for L in lessons:
        validate(L)
        data = json.dumps(L, ensure_ascii=False, indent=2).encode("utf-8")
        open(os.path.join(out, f"{L['id']}.r{L['revision']}.json"), "wb").write(data)
        res.append((L["id"], L["revision"], hashlib.sha256(data).hexdigest()))
    return res
