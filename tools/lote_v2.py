# Lecciones en formato de tarjetas (esquema 2.0, interfaz v3). Se ejecuta dentro de gen_lessons.py.
# Tipos de tarjeta: portada, idea, pregunta, revelar, dato. Al final, el resumen que se guarda en "Aprendido".
HOY2 = "2026-10-20"

def card(id, tipo, **k):
    c = {"id": id, "tipo": tipo}
    for key in ("titulo", "texto", "visual", "revelado", "pregunta", "correctaId"):
        if key in k and k[key] is not None: c[key] = k[key]
    if "opciones" in k: c["opciones"] = [dict(id=o[0], texto=o[1], retro=o[2]) for o in k["opciones"]]
    c["fuenteIds"] = k.get("fuentes", [])
    return c

def lesson2(id, rev, disciplina, familia, titulo, subtitulo, minutos, tarjetas, resumen, fuentes):
    REVISION[id] = rev
    return {"schemaVersion": "2.0", "id": id, "revision": rev, "idioma": "es-CL",
            "disciplina": disciplina, "familia": familia, "titulo": titulo, "subtitulo": subtitulo,
            "minutosEstimados": minutos, "tarjetas": tarjetas,
            "resumen": {"titulo": resumen[0], "puntos": resumen[1]}, "fuentes": fuentes,
            "controlEditorial": {"estado": "borrador", "revisadoPor": None, "fechaRevision": None}}

P = "cielo-azul"
def S(body, title, vb="0 0 320 200"): return svg(vb, body, title)

v_portada = S(
    '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'
    '<circle cx="232" cy="64" r="30" class="as-svg__sun"/>'
    '<path d="M0 160 C60 130 110 150 160 140 C220 128 270 150 320 138 L320 200 L0 200 Z" class="as-svg__fill"/>'
    '<path d="M70 70 q8 -8 16 0 q8 -8 16 0" class="as-svg__ink"/>'
    '<path d="M120 50 q6 -6 12 0 q6 -6 12 0" class="as-svg__ink"/>',
    "Un cielo con sol sobre unos cerros")
v_prisma = S(
    arrow_def(P + "-v2-ah") +
    '<line x1="10" y1="100" x2="118" y2="100" class="as-svg__ink" stroke-width="4"/>'
    '<text x="62" y="88" text-anchor="middle" class="as-svg__label" font-size="12">luz blanca</text>'
    '<polygon points="120,40 170,150 70,150" class="as-svg__soft"/>'
    '<polygon points="120,40 170,150 70,150" class="as-svg__ink"/>'
    '<polygon points="140,98 310,40 310,66" class="as-svg__warm"/>'
    '<polygon points="140,100 310,66 310,92" class="as-svg__sun"/>'
    '<polygon points="140,102 310,92 310,118" class="as-svg__fill"/>'
    '<polygon points="140,104 310,118 310,144" class="as-svg__cool"/>'
    '<text x="300" y="168" text-anchor="end" class="as-svg__label as-svg__muted" font-size="11">todos los colores</text>',
    "Un rayo de luz blanca entra a un prisma y sale separado en colores")
v_ondas = S(
    '<path d="M20 60 q15 -30 30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0" class="as-svg__coolline"/>'
    '<text x="20" y="22" class="as-svg__label" font-size="13">azul: ondas cortas</text>'
    '<path d="M20 150 q45 -40 90 0 t90 0 t90 0" class="as-svg__warmline"/>'
    '<text x="20" y="108" class="as-svg__label" font-size="13">rojo: ondas largas</text>',
    "Dos ondas: la azul es corta y apretada; la roja es larga y estirada")
v_desvio = S(
    arrow_def(P + "-v3-ah") +
    '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'
    '<circle cx="40" cy="44" r="22" class="as-svg__sun"/>'
    '<line x1="62" y1="54" x2="262" y2="150" class="as-svg__ink" stroke-width="2" marker-end="url(#' + P + '-v3-ah)"/>'
    '<circle cx="160" cy="101" r="5" class="as-svg__fill"/>'
    '<line x1="160" y1="101" x2="160" y2="40" class="as-svg__coolline" marker-end="url(#' + P + '-v3-ah)"/>'
    '<line x1="160" y1="101" x2="210" y2="56" class="as-svg__coolline" marker-end="url(#' + P + '-v3-ah)"/>'
    '<line x1="160" y1="101" x2="105" y2="142" class="as-svg__coolline" marker-end="url(#' + P + '-v3-ah)"/>'
    '<line x1="160" y1="101" x2="100" y2="80" class="as-svg__coolline" marker-end="url(#' + P + '-v3-ah)"/>'
    '<circle cx="282" cy="160" r="10" class="as-svg__ink"/>'
    '<text x="282" y="188" text-anchor="middle" class="as-svg__label" font-size="12">tú</text>'
    '<text x="200" y="30" class="as-svg__label as-svg__muted" font-size="11">el azul se desvía</text>',
    "El sol envía su luz hacia una persona; en el camino, flechas azules salen en todas direcciones")
v_camino = S(
    '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'
    '<path d="M0 170 L320 170" class="as-svg__ink"/>'
    '<circle cx="250" cy="166" r="7" class="as-svg__ink"/>'
    '<text x="250" y="190" text-anchor="middle" class="as-svg__label" font-size="12">tú</text>'
    '<circle cx="250" cy="34" r="16" class="as-svg__sun"/>'
    '<line x1="250" y1="52" x2="250" y2="156" class="as-svg__coolline" stroke-dasharray="6 6"/>'
    '<text x="240" y="90" text-anchor="end" class="as-svg__label" font-size="11">mediodía:</text>'
    '<text x="240" y="104" text-anchor="end" class="as-svg__label" font-size="11">camino corto</text>'
    '<circle cx="24" cy="150" r="16" class="as-svg__warm"/>'
    '<line x1="42" y1="152" x2="240" y2="164" class="as-svg__warmline" stroke-dasharray="6 6"/>'
    '<text x="40" y="136" class="as-svg__label" font-size="11">atardecer: camino largo</text>',
    "Al mediodía la luz baja recta y recorre poco aire; al atardecer cruza mucho más aire")
v_marte = S(
    '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__warm"/>'
    '<circle cx="160" cy="118" r="44" class="as-svg__cool"/>'
    '<circle cx="160" cy="118" r="12" class="as-svg__sun"/>'
    '<path d="M0 150 C80 135 140 160 200 148 C250 138 290 152 320 146 L320 200 L0 200 Z" class="as-svg__fill"/>'
    '<text x="16" y="28" class="as-svg__label" font-size="13">Marte, al atardecer</text>',
    "Un atardecer en Marte: cielo anaranjado y un halo azulado alrededor del Sol")

L.append(lesson2(P, 3, "Ciencia cotidiana", "fisica", "¿Por qué el cielo es azul?",
  "Y por qué al atardecer se pone naranjo.", 5,
  [
    card("c1", "portada", titulo="¿Por qué el cielo es azul?", texto="Y por qué al atardecer se pone naranjo, si es el mismo sol. En cinco minutos lo vas a entender.", visual=v_portada),
    card("c2", "idea", titulo="La luz blanca esconde un arcoíris", texto="La luz del sol parece blanca, pero trae mezclados todos los colores del arcoíris.", visual=v_prisma, fuentes=["nasa-cielo"]),
    card("c3", "idea", titulo="Cada color es una onda", texto="La luz viaja en ondas, como las olas del mar. Las ondas del azul son más cortas que las del rojo.", visual=v_ondas, fuentes=["nasa-cielo"]),
    card("c4", "pregunta", pregunta="Cuando la luz del sol entra al aire, ¿qué color crees que el aire desvía más?", correctaId="a", opciones=[
      ("a", "El azul", "¡Exacto! Las moléculas del aire desvían mucho más los colores de ondas cortas, como el azul."),
      ("b", "El rojo", "Es al revés: el rojo es de los que el aire desvía menos."),
      ("c", "Todos por igual", "No: el aire desvía mucho más el azul, el color de ondas más cortas.")], fuentes=["nasa-cielo"]),
    card("c5", "idea", titulo="Por eso el cielo es azul", texto="Las moléculas diminutas del aire desvían el azul en todas direcciones. Ese azul te llega desde todo el cielo, mires hacia donde mires.", visual=v_desvio, fuentes=["nasa-cielo", "britannica-rayleigh"]),
    card("c6", "revelar", titulo="¿Y el atardecer?", texto="Cuando el sol está bajo, su luz cruza mucho más aire para llegar hasta ti. ¿Qué crees que le pasa al azul en ese camino tan largo?",
         revelado="Gran parte del azul se desvía antes de llegar a tus ojos. Lo que sigue derecho es, sobre todo, el amarillo, el naranjo y el rojo. El polvo del aire puede hacerlo todavía más rojo.", visual=v_camino, fuentes=["nasa-cielo"]),
    card("c7", "pregunta", pregunta="Vas por la carretera al atardecer y el sol, ya bajo, se ve naranjo. ¿Qué le pasó a su luz?", correctaId="a", opciones=[
      ("a", "Cruzó mucho aire y gran parte del azul se desvió en el camino", "¡Así es! Llegan directo sobre todo el amarillo, el naranjo y el rojo."),
      ("b", "El sol cambia de color al final del día", "El sol es el mismo; lo que cambia es el largo del camino que recorre su luz por el aire."),
      ("c", "El aire se tiñe de naranjo en la tarde", "El aire no se tiñe: desvía el azul y deja pasar más el naranjo y el rojo.")], fuentes=["nasa-cielo"]),
    card("c8", "dato", texto="En Marte pasa algo curioso: al atardecer, el cielo cerca del Sol puede verse azulado. Allí interviene el polvo fino de su atmósfera, que deja pasar mejor la luz azul. El robot Curiosity de la NASA lo fotografió en abril de 2015.", visual=v_marte, fuentes=["jpl-marte"]),
  ],
  ("El color del cielo", [
    "La luz del sol trae mezclados todos los colores.",
    "El aire desvía sobre todo el azul, y ese azul nos llega desde todo el cielo.",
    "Al atardecer la luz cruza más aire: gran parte del azul se desvía en el camino y vemos amarillo, naranjo y rojo."]),
  [src("nasa-cielo", "NASA Space Place", "Why Is the Sky Blue?", "https://spaceplace.nasa.gov/blue-sky/en/", "Secciones de la luz blanca y las ondas; por qué el cielo es azul; por qué el atardecer es rojo", ["La luz del sol se ve blanca, pero está formada por todos los colores del arcoíris", "La luz viaja en ondas; las ondas de la luz azul son más cortas que las de la roja", "Las moléculas diminutas del aire dispersan la luz azul en todas direcciones; por eso vemos el cielo azul la mayor parte del tiempo", "Con el sol bajo, la luz cruza más atmósfera; se dispersa aún más el azul y el rojo y el amarillo pasan derecho", "El polvo, la contaminación y otros aerosoles también dispersan la luz azul"], HOY2),
   src("britannica-rayleigh", "Encyclopaedia Britannica", "Rayleigh scattering", "https://www.britannica.com/science/Rayleigh-scattering", "Párrafo inicial", ["La dispersión de Rayleigh produce el color azul del cielo iluminado por el sol", "Las longitudes de onda más cortas se dispersan mucho más"], HOY2),
   src("jpl-marte", "NASA Jet Propulsion Laboratory", "Sunset in Mars' Gale Crater (PIA19400)", "https://www.jpl.nasa.gov/images/pia19400-sunset-in-mars-gale-crater/", "Descripción de la imagen", ["Imagen tomada al cierre del sol 956 de la misión, el 15 de abril de 2015", "El polvo tiene partículas finas que permiten que la luz azul atraviese la atmósfera con más eficiencia", "Los colores azules se mantienen más cerca de la zona del cielo donde está el sol"], HOY2)]))
