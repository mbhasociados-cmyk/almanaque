# Lote 4 (opción A, 28-10-2026): 7 lecciones nuevas en tarjetas (esquema 2.0), del 04-11 al 10-11-2026.
# Producidas por Claude bajo la delegación de Max del 20-10-2026. Fuentes abiertas y comprobadas el 28-10-2026.
# Cada ilustración muestra solo lo que dice el texto de su tarjeta.
# Salida: borradores/lote4/
import math, os, sys
HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "visuales"))
from almanaque_lib import card, src, lesson, write, validate_visuals
from svgkit import svg, BG, arrow_def, arrow, text, poly, waves

HOY = "2026-10-28"
LOTE = []
VIS = {}

def box(x, y, w, h, cls="as-svg__warm", rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="as-svg__ink"/>'

def shape(d, cls):
    return f'<path d="{d}" class="{cls}"/><path d="{d}" class="as-svg__ink"/>'

def dots(pts, r=3, cls="as-svg__fill"):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>' for x, y in pts)

def drop(x, y, s=1.0, cls="as-svg__cool"):
    d = f"M{x} {y - 7 * s} C{x + 5 * s} {y - 1 * s} {x + 5 * s} {y + 4 * s} {x} {y + 4 * s} C{x - 5 * s} {y + 4 * s} {x - 5 * s} {y - 1 * s} {x} {y - 7 * s} Z"
    return f'<path d="{d}" class="{cls}"/>'

def glass(x, y, w=70, h=100, water=True):
    """Vaso de lados levemente inclinados; (x, y) = esquina superior izquierda."""
    d = f"M{x} {y} L{x + w} {y} L{x + w - 8} {y + h} L{x + 8} {y + h} Z"
    out = ""
    if water:
        out += f'<path d="M{x + 3} {y + 18} L{x + w - 3} {y + 18} L{x + w - 8} {y + h} L{x + 8} {y + h} Z" class="as-svg__cool"/>'
    return out + f'<path d="{d}" class="as-svg__ink"/>'

def cloud(x, y, s=1.0, cls="as-svg__warm"):
    d = (f"M{x} {y} C{x - 30 * s} {y} {x - 30 * s} {y - 30 * s} {x - 6 * s} {y - 30 * s} C{x} {y - 50 * s} {x + 40 * s} {y - 50 * s} {x + 46 * s} {y - 30 * s} "
         f"C{x + 74 * s} {y - 32 * s} {x + 74 * s} {y} {x + 50 * s} {y} Z")
    return shape(d, cls)

# =================================================================== 04-11 vaso-empanado (física)
L = "vaso-empanado"; A = arrow_def(L)
V = VIS[L] = {
 "c1": svg("Un vaso con bebida helada y gotas de agua en la parte de afuera del vidrio",
   BG + glass(120, 50, 80, 120) + box(140, 80, 18, 18, "as-svg__soft", 3) + box(164, 92, 18, 18, "as-svg__soft", 3) +
   drop(116, 100) + drop(206, 88) + drop(112, 140) + drop(204, 132) + drop(118, 120, 0.8) +
   text(160, 34, "¿de dónde sale el agua?", 17)),
 "c3": svg("El vapor de agua del aire, que no se ve, se convierte en gotas de agua líquida: condensación",
   BG + A + box(20, 50, 110, 90, "as-svg__soft", 10) +
   dots([(40, 70), (62, 84), (90, 66), (110, 90), (48, 110), (80, 120), (112, 124), (70, 98)], 3, "as-svg__muted") +
   arrow(L, 140, 95, 182, 95, 3) + drop(214, 82, 1.6) + drop(250, 106, 1.6) + drop(278, 80, 1.6) +
   text(75, 165, "vapor (gas)", 16) + text(246, 165, "agua líquida", 16) + text(160, 32, "condensación", 17)),
 "c4": svg("El aire tibio puede contener más vapor que el frío; si el aire se enfría lo suficiente, se satura y el vapor forma gotitas",
   BG + A + box(16, 40, 120, 100, "as-svg__warm", 10) +
   dots([(34, 60), (56, 74), (80, 58), (104, 70), (122, 90), (40, 96), (70, 104), (98, 118), (120, 124), (50, 126), (84, 82)], 3, "as-svg__fill") +
   arrow(L, 146, 90, 176, 90, 3) + box(186, 40, 120, 100, "as-svg__soft", 10) +
   drop(214, 84, 1.3) + drop(244, 104, 1.3) + drop(276, 80, 1.3) + drop(260, 124, 1.0) +
   text(76, 166, "aire tibio", 16) + text(76, 188, "más vapor", 15, muted=True) +
   text(246, 166, "se enfría y se satura", 15) + text(246, 188, "gotitas", 15, muted=True)),
 "c5": svg("El aire que toca el vaso helado se enfría; al llegar a su punto de rocío aparecen gotas en el vidrio",
   BG + A + glass(210, 50, 80, 120) + drop(206, 100) + drop(206, 130) + drop(296, 110) +
   arrow(L, 30, 140, 188, 140, 3) + text(100, 128, "aire", 16) +
   '<rect x="24" y="30" width="12" height="44" rx="6" class="as-svg__ink"/><circle cx="30" cy="78" r="9" class="as-svg__fill"/><rect x="27" y="50" width="6" height="26" class="as-svg__fill"/>' +
   text(48, 50, "baja hasta su", 15, "start") + text(48, 72, "punto de rocío", 16, "start") + text(250, 192, "aparecen gotas", 15)),
 "c7": svg("Al amanecer, el pasto aparece mojado: la superficie se enfrió hasta su punto de rocío y se formó rocío",
   BG + '<path d="M250 120 A30 30 0 0 1 310 120 Z" class="as-svg__sun"/>' +
   '<rect x="0" y="120" width="320" height="80" class="as-svg__warm"/>' +
   "".join(f'<path d="M{x} 170 L{x + 6} 128 M{x + 10} 170 L{x + 14} 136 M{x + 20} 170 L{x + 18} 130" class="as-svg__ink"/>' for x in range(20, 240, 40)) +
   drop(26, 124, 0.8) + drop(66, 132, 0.8) + drop(108, 126, 0.8) + drop(146, 134, 0.8) + drop(186, 128, 0.8) + drop(224, 132, 0.8) +
   text(120, 50, "sin lluvia, pasto mojado", 16) + text(120, 74, "rocío o escarcha", 16, muted=True)),
 "c8": svg("Las nubes se forman igual: el aire con vapor sube, se enfría y el vapor se condensa en gotitas",
   BG + A + cloud(130, 80, 1.1, "as-svg__soft") + drop(150, 62, 0.8) + drop(172, 52, 0.8) + drop(194, 64, 0.8) + drop(126, 64, 0.8) +
   arrow(L, 160, 180, 160, 100, 3) + dots([(140, 160), (178, 150), (146, 128), (174, 120)], 3, "as-svg__muted") +
   text(40, 150, "sube y", 16, "start") + text(40, 170, "se enfría", 16, "start") + text(214, 150, "gotitas:", 16, "start") + text(214, 170, "una nube", 16, "start")),
}
LOTE.append(lesson(L, "Ciencia cotidiana", "fisica",
  "¿Por qué se empaña un vaso frío?", "El agua que aparece por fuera viene del aire.",
  [card("c1", "portada", titulo="¿Por qué se empaña un vaso frío?", texto="En un día húmedo, un vaso con bebida helada se moja por fuera. ¿De dónde sale esa agua?", fuentes=["usgs-cond"]),
   card("c2", "pregunta", pregunta="¿De dónde viene el agua que aparece afuera de un vaso helado?", correctaId="a", opciones=[
     ("a", "Del vapor de agua que hay en el aire", "¡Exacto! El vapor del aire se convierte en agua líquida sobre el vidrio."),
     ("b", "Del líquido del vaso, que se filtra por el vidrio", "No: el vidrio no deja pasar el líquido. El agua viene del aire."),
     ("c", "Del hielo, que se derrite hacia afuera", "No: el agua de afuera no viene del vaso, sino del vapor del aire.")], fuentes=["usgs-cond"]),
   card("c3", "idea", titulo="Vapor que no se ve", texto="El aire lleva vapor de agua, un gas que no vemos. La condensación es el paso de ese vapor a agua líquida.", fuentes=["usgs-cond"]),
   card("c4", "idea", titulo="El aire tibio guarda más vapor", texto="El aire tibio puede contener más vapor de agua que el aire frío. Si el aire se enfría lo suficiente, se satura y el vapor se condensa en gotitas.", fuentes=["nws-rocio"]),
   card("c5", "idea", titulo="El punto de rocío", texto="La temperatura a la que hay que enfriar el aire para que se sature se llama punto de rocío. Cuando aire húmedo toca una superficie más fría, como un vaso helado, se enfría y puede llegar a ese punto.", fuentes=["uw-rocio", "usgs-cond"]),
   card("c6", "pregunta", pregunta="Cuando se empañan los anteojos, ¿qué cubre los vidrios?", correctaId="b", opciones=[
     ("a", "Una capa de polvo", "No: lo que los cubre es agua."),
     ("b", "Gotitas de agua que se condensaron", "¡Así es! Es el mismo fenómeno del vaso helado."),
     ("c", "Una capa fina de hielo", "No: son gotitas de agua líquida, formadas por condensación.")], fuentes=["usgs-cond"]),
   card("c7", "revelar", titulo="Lo mismo pasa en el pasto", texto="Temprano en la mañana, el pasto puede estar mojado aunque no haya llovido. ¿Por qué?",
        revelado="Porque la superficie se enfrió hasta su punto de rocío y el vapor del aire se condensó en ella: así se forma el rocío, o la escarcha.", fuentes=["nws-rocio"]),
   card("c8", "dato", texto="Las nubes nacen de la misma manera: el aire con vapor sube, se enfría y el vapor se condensa en gotitas. Una nube pesa toneladas, y aun así no se nos cae encima.", fuentes=["usgs-cond"])],
  ("El vaso empañado", ["El agua que aparece afuera de un vaso helado viene del vapor del aire: es condensación.",
                        "El aire tibio puede contener más vapor que el frío; al enfriarse hasta su punto de rocío, se satura y forma gotitas.",
                        "El rocío del pasto, los anteojos empañados y las nubes se forman de la misma manera."]),
  [src("usgs-cond", "U.S. Geological Survey (USGS), Water Science School", "Condensation and the Water Cycle", "https://www.usgs.gov/water-science-school/science/condensation-and-water-cycle", "Texto principal y secciones \"Common examples of condensation\" y \"Condensation in the air\"",
       ["La condensación es el proceso por el que el vapor de agua del aire pasa a agua líquida", "El agua en el exterior de un vaso frío en un día húmedo es condensación", "La niebla se forma cuando aire con humedad relativamente alta encuentra una superficie más fría y se enfría hasta el punto de rocío", "Los lentes se empañan porque pequeñas gotas de agua cubren la superficie por condensación", "Las nubes se forman porque el aire con vapor sube y se enfría", "Aunque una nube pesa toneladas, no cae sobre uno"],
       ["c1", "c2", "c3", "c5", "c6", "c8"], HOY),
   src("nws-rocio", "National Weather Service (NOAA), oficina de Lincoln, Illinois", "Severe Weather Topics — Week 3: What is Dewpoint?", "https://www.weather.gov/ilx/swop-springtopics3", "Texto principal",
       ["El aire cálido tiene mayor capacidad de contener vapor de agua que el aire frío", "El punto de rocío es la temperatura a la que hay que enfriar el aire para saturarlo", "Al saturarse, el vapor de agua se condensa en gotitas", "Cuando la superficie se enfría hasta su punto de rocío se forma rocío o escarcha en el pasto, a menudo temprano en la mañana"],
       ["c4", "c7"], HOY),
   src("uw-rocio", "Universidad de Wisconsin-Madison, CIMSS/SSEC", "Definitions: Dew Point and Relative Humidity", "https://cimss.ssec.wisc.edu/wxwise/rh/page2.html", "Texto principal",
       ["El punto de rocío es la temperatura a la que el aire debe enfriarse, sin cambiar la presión, para saturarse", "La humedad relativa describe qué tan lejos está el aire de la saturación"],
       ["c5"], HOY)]))

# =================================================================== 05-11 niebla-costera (geografía)
L = "niebla-costera"; A = arrow_def(L)
sea = lambda: '<rect x="0" y="130" width="150" height="70" class="as-svg__cool"/>' + waves(6, 140, 130, 5, 24)
hills = lambda: shape("M140 200 L140 130 L180 90 L210 110 L250 60 L290 100 L320 80 L320 200 Z", "as-svg__warm")
fog = lambda x0, x1, y: "".join(f'<path d="M{x} {y} q12 -10 24 0 t24 0" class="as-svg__muted" stroke-width="3"/>' for x in range(x0, x1, 48))
V = VIS[L] = {
 "c1": svg("La camanchaca: una niebla espesa que avanza desde el océano hacia la costa del norte de Chile",
   BG + A + sea() + hills() + fog(10, 100, 108) + fog(30, 120, 88) + arrow(L, 40, 60, 110, 60, 3) +
   text(80, 40, "desde el océano", 16) + text(230, 180, "casi no llueve", 15)),
 "c2": svg("Frente a la costa, una nube baja tipo estratocúmulo se forma sobre el océano y avanza hacia el continente",
   BG + A + '<rect x="0" y="130" width="230" height="70" class="as-svg__cool"/>' + waves(6, 220, 130, 5, 24) +
   shape("M230 200 L230 120 L270 100 L320 110 L320 200 Z", "as-svg__warm") +
   cloud(50, 100, 0.9, "as-svg__soft") + cloud(130, 104, 0.8, "as-svg__soft") +
   arrow(L, 200, 80, 250, 80, 3) + text(110, 36, "nube baja sobre el mar", 16) + text(276, 70, "costa", 16)),
 "c3": svg("La nube marina choca con la cordillera de la Costa y forma la niebla costera, la camanchaca",
   BG + A + sea() + hills() + cloud(150, 116, 0.8, "as-svg__soft") + arrow(L, 40, 92, 120, 92, 3) +
   text(250, 30, "cordillera", 16) + text(250, 48, "de la Costa", 16) + text(240, 180, "camanchaca", 16)),
 "c5": svg("Aire húmedo que se encuentra con una superficie más fría: así aparece la niebla",
   BG + A + '<rect x="20" y="140" width="280" height="40" rx="6" class="as-svg__cool"/>' + text(160, 166, "superficie fría", 16) +
   arrow(L, 30, 60, 120, 60, 3) + text(70, 44, "aire húmedo", 16) + fog(140, 300, 120) + fog(164, 300, 102) + text(234, 74, "niebla", 17)),
 "c7": svg("Un atrapanieblas: la malla intercepta las gotitas de la niebla, el agua escurre por una canaleta y se guarda en un estanque",
   BG + A + fog(20, 100, 60) + fog(20, 100, 84) +
   '<line x1="110" y1="30" x2="110" y2="150" class="as-svg__ink" stroke-width="3"/><line x1="230" y1="30" x2="230" y2="150" class="as-svg__ink" stroke-width="3"/>' +
   "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="120" class="as-svg__muted"/>' for x in range(120, 230, 12)) +
   "".join(f'<line x1="110" y1="{y}" x2="230" y2="{y}" class="as-svg__muted"/>' for y in range(40, 130, 12)) +
   '<rect x="110" y="120" width="120" height="8" class="as-svg__fill"/>' + drop(160, 110, 0.8) + drop(190, 96, 0.8) +
   arrow(L, 232, 126, 262, 150, 2) + box(254, 150, 52, 36, "as-svg__cool") +
   text(170, 24, "malla", 16) + text(60, 116, "niebla", 16) + text(246, 178, "estanque", 15, "end")),
 "c8": svg("En Peña Blanca, 34 atrapanieblas pueden recoger hasta 650.000 litros de agua al año, sobre todo en primavera",
   BG + "".join('<rect x="%d" y="50" width="44" height="40" class="as-svg__soft"/><rect x="%d" y="50" width="44" height="40" class="as-svg__ink"/>' % (x, x) +
               f'<line x1="{x}" y1="90" x2="{x}" y2="110" class="as-svg__ink"/><line x1="{x + 44}" y1="90" x2="{x + 44}" y2="110" class="as-svg__ink"/>' for x in (30, 90, 150, 210)) +
   text(270, 76, "×34", 18, "start") + box(50, 124, 220, 50, "as-svg__cool") + text(160, 148, "hasta 650.000 litros", 16) +
   text(160, 167, "al año", 15) + text(160, 34, "Peña Blanca", 16)),
}
LOTE.append(lesson(L, "Geografía", "geografia",
  "¿Por qué hay niebla en una costa donde llueve poco?", "La camanchaca nace en el mar.",
  [card("c1", "portada", titulo="¿Por qué hay niebla en una costa donde llueve poco?", texto="En la costa del norte de Chile llueve muy poco. Aun así, una niebla espesa, la camanchaca, avanza desde el océano. ¿De dónde sale?", fuentes=["fao-niebla", "uc-niebla"]),
   card("c2", "idea", titulo="Una nube que nace en el mar", texto="Frente a la costa es frecuente una nube baja, de tipo estratocúmulo. Se forma sobre el océano y avanza hacia el continente.", fuentes=["uc-niebla"]),
   card("c3", "idea", titulo="La nube choca con los cerros", texto="Cuando esa nube marina es atajada por la cordillera de la Costa, se forma la niebla costera: la camanchaca.", fuentes=["uc-niebla"]),
   card("c4", "pregunta", pregunta="¿Qué es la camanchaca?", correctaId="a", opciones=[
     ("a", "Una nube marina atajada por la cordillera de la Costa", "¡Exacto! Nace sobre el océano y queda atrapada en los cerros de la costa."),
     ("b", "Humo que viene de los volcanes", "No: es una nube que viene del mar."),
     ("c", "Polvo del desierto que levanta el viento", "No: está hecha de gotitas de agua y viene del océano.")], fuentes=["uc-niebla"]),
   card("c5", "idea", titulo="Aire húmedo, superficie fría", texto="En general, la niebla aparece cuando aire húmedo se encuentra con una superficie más fría. Cuando aire más cálido se mueve sobre una superficie fría, se habla de niebla de advección.", fuentes=["usgs-niebla"]),
   card("c6", "pregunta", pregunta="La niebla costera entra solo unos pocos kilómetros tierra adentro. ¿Por qué?", correctaId="b", opciones=[
     ("a", "Porque el viento la empuja siempre de vuelta al mar", "No es lo que describe el estudio: el calor del suelo y los cerros altos son los que la frenan."),
     ("b", "Porque el calor del suelo evapora sus gotitas y los cerros altos la frenan", "¡Así es! El suelo caliente la disipa y las serranías altas son obstáculos."),
     ("c", "Porque se congela al llegar a tierra", "No: el suelo caliente evapora sus gotitas.")], fuentes=["uc-niebla"]),
   card("c7", "revelar", titulo="Agua atrapada en una malla", texto="En algunos lugares de Chile se cosecha agua de la camanchaca. ¿Cómo?",
        revelado="Con atrapanieblas: mallas que interceptan las microgotas de la niebla. El agua cae por canaletas, se guarda en estanques y se usa para regar.", fuentes=["fao-niebla"]),
   card("c8", "dato", texto="En la Reserva Ecológica Cerro Grande, de la comunidad agrícola de Peña Blanca, 34 atrapanieblas pueden recoger hasta 650.000 litros de agua al año, sobre todo en primavera.", fuentes=["fao-niebla"])],
  ("La camanchaca", ["Es una nube baja que se forma sobre el océano y queda atajada por la cordillera de la Costa.",
                     "La niebla aparece cuando aire húmedo se encuentra con una superficie más fría.",
                     "Con atrapanieblas, sus gotitas se recogen como agua para regar, aunque casi no llueva."]),
  [src("uc-niebla", "Pontificia Universidad Católica de Chile, Instituto de Geografía (Cereceda, Larrain, Osses, Lázaro, Pinto y Schemenauer)", "Penetración continental de la niebla de advección en Tarapacá, Chile (2001)", "https://cda.uc.cl/wp-content/uploads/2024/02/Penetracion-continental-de-la-niebla-de-adveccion-en-Tarapaca-Chile.pdf", "Introducción y desarrollo",
       ["En la costa es frecuente una nubosidad de tipo estratocúmulo, que se forma en el océano y avanza hacia el continente", "Al ser interceptada por la cordillera de la Costa forma la niebla costera o camanchaca", "La niebla penetra pocos kilómetros: el calentamiento de la superficie evapora sus gotas y las altas serranías son obstáculos", "La costa del norte tiene muy baja pluviosidad"],
       ["c1", "c2", "c3", "c4", "c6"], HOY),
   src("usgs-niebla", "U.S. Geological Survey (USGS), Water Science School", "Condensation and the Water Cycle", "https://www.usgs.gov/water-science-school/science/condensation-and-water-cycle", "Sección \"Condensation near the ground\"",
       ["La niebla se forma cuando aire con humedad relativamente alta encuentra una superficie más fría", "La niebla que se forma cuando aire más cálido se mueve sobre una superficie fría se llama niebla de advección"],
       ["c5"], HOY),
   src("fao-niebla", "Organización de las Naciones Unidas para la Alimentación y la Agricultura (FAO)", "Atrapar la niebla para generar agua (15-06-2026)", "https://www.fao.org/newsroom/story/capturing-fog-to-make-water/es", "Texto principal",
       ["Una espesa niebla, la camanchaca, avanza desde el océano", "Los atrapanieblas son estructuras de malla que interceptan las microgotas de la niebla; el agua cae por canalones, se almacena en estanques y se usa para riego", "En la Reserva Ecológica Cerro Grande, comunidad agrícola de Peña Blanca, 34 atrapanieblas pueden recoger hasta 650.000 litros al año, sobre todo en primavera"],
       ["c1", "c7", "c8"], HOY)]))

# =================================================================== 06-11 barco-acero (física)
L = "barco-acero"; A = arrow_def(L)
def ship(x, y, s=1.0, air=False):
    d = f"M{x} {y} L{x + 120 * s} {y} L{x + 100 * s} {y + 40 * s} L{x + 20 * s} {y + 40 * s} Z"
    out = shape(d, "as-svg__warm")
    if air:
        out += f'<path d="M{x + 12 * s} {y + 6 * s} L{x + 108 * s} {y + 6 * s} L{x + 94 * s} {y + 34 * s} L{x + 26 * s} {y + 34 * s} Z" class="as-svg__soft"/>'
    return out + f'<rect x="{x + 40 * s}" y="{y - 22 * s}" width="{40 * s}" height="{22 * s}" class="as-svg__fill"/><rect x="{x + 40 * s}" y="{y - 22 * s}" width="{40 * s}" height="{22 * s}" class="as-svg__ink"/>'
water = lambda y: f'<rect x="0" y="{y}" width="320" height="{200 - y}" rx="0" class="as-svg__cool"/>' + waves(4, 316, y, 4, 24)
V = VIS[L] = {
 "c1": svg("Un perno de acero se va al fondo de un balde con agua, mientras un barco de acero flota",
   BG + A + shape("M30 70 L110 70 L100 170 L40 170 Z", "as-svg__soft") + '<path d="M33 90 L107 90 L100 170 L40 170 Z" class="as-svg__cool"/>' +
   '<rect x="64" y="146" width="12" height="20" class="as-svg__ink"/><rect x="60" y="142" width="20" height="6" class="as-svg__ink"/>' +
   '<rect x="160" y="130" width="150" height="50" class="as-svg__cool"/>' + ship(175, 112, 1.0) +
   text(70, 194, "perno: se hunde", 15) + text(235, 194, "barco: flota", 15) + text(160, 36, "los dos son de acero", 16)),
 "c3": svg("Un objeto en el agua recibe un empuje hacia arriba igual al peso del agua que desplaza",
   BG + A + water(80) + box(120, 100, 80, 50, "as-svg__warm") + arrow(L, 160, 186, 160, 156, 3) +
   text(160, 40, "empuje hacia arriba =", 16) + text(160, 62, "peso del agua desplazada", 16) + text(250, 186, "empuje", 16)),
 "c4": svg("Un barco se hunde hasta que el agua que desplaza pesa lo mismo que él, y ahí queda flotando",
   BG + A + water(110) + ship(110, 92, 1.0) + arrow(L, 170, 40, 170, 66, 3) + arrow(L, 170, 190, 170, 140, 3) +
   text(170, 30, "peso del barco", 15) + text(20, 166, "peso del agua", 15, "start") + text(20, 186, "desplazada", 15, "start") + text(260, 176, "iguales", 17)),
 "c5": svg("Corte de un casco de acero que encierra aire: contando acero y aire, el barco es menos denso que el agua",
   BG + water(120) + ship(80, 90, 1.3, air=True) + text(160, 116, "aire", 17) + text(160, 36, "acero + aire", 17) +
   text(160, 186, "menos denso que el agua", 16)),
 "c7": svg("Con la misma cantidad de material, la forma cambia cuánta agua desplaza el objeto",
   BG + '<rect x="20" y="110" width="120" height="40" class="as-svg__cool"/><rect x="180" y="110" width="120" height="40" class="as-svg__cool"/>' +
   '<circle cx="80" cy="104" r="12" class="as-svg__warm"/><circle cx="80" cy="104" r="12" class="as-svg__ink"/>' +
   shape("M190 100 L290 100 L278 128 L202 128 Z", "as-svg__warm") +
   text(160, 36, "mismo material, otra forma", 16) + text(80, 176, "desplaza menos", 15) + text(240, 176, "desplaza más", 15)),
 "c8": svg("Un vehículo sumergible: si bombea agua hacia adentro baja, y si la saca vuelve a subir",
   BG + A + water(40) + shape("M100 100 C100 80 220 80 220 100 C220 120 100 120 100 100 Z", "as-svg__warm") + box(140, 72, 40, 14, "as-svg__fill", 4) +
   arrow(L, 66, 70, 66, 136, 3) + arrow(L, 254, 136, 254, 70, 3) +
   text(66, 166, "agua adentro:", 15) + text(66, 186, "baja", 15) + text(254, 166, "agua afuera:", 15) + text(254, 186, "sube", 15)),
}
LOTE.append(lesson(L, "Ciencia cotidiana", "fisica",
  "¿Cómo puede flotar un barco de acero?", "No es el material: es el agua que desplaza.",
  [card("c1", "portada", titulo="¿Cómo puede flotar un barco de acero?", texto="Un perno de acero que cae a un balde con agua se va al fondo. Pero un barco con casco de acero flota. ¿Cómo?", fuentes=["sciam-barco"]),
   card("c2", "pregunta", pregunta="¿Qué decide si un objeto flota o se hunde en el agua?", correctaId="a", opciones=[
     ("a", "Si es más o menos denso que el agua", "¡Exacto! Lo que es menos denso que el agua flota; lo que es más denso se hunde."),
     ("b", "Solo cuánto pesa", "No basta con el peso: un barco enorme pesa mucho y flota. Lo que importa es la densidad."),
     ("c", "El color del material", "No: el color no cambia nada. Lo que importa es la densidad.")], fuentes=["noaa-flota", "sciam-barco"]),
   card("c3", "idea", titulo="El agua empuja hacia arriba", texto="Todo objeto en el agua recibe un empuje hacia arriba igual al peso del agua que desplaza. Es el principio de Arquímedes.", fuentes=["noaa-flota", "kids-arquimedes"]),
   card("c4", "idea", titulo="Flota a la altura justa", texto="Un barco se hunde hasta que el agua que desplaza pesa lo mismo que él. Ahí queda flotando.", fuentes=["kids-arquimedes"]),
   card("c5", "idea", titulo="Un casco lleno de aire", texto="El casco de acero encierra mucho aire. Si se cuentan juntos el acero y el aire, el barco es menos denso que el agua, y por eso flota.", fuentes=["sciam-barco"]),
   card("c6", "pregunta", pregunta="¿Qué pasa si a un barco se le pone demasiada carga?", correctaId="b", opciones=[
     ("a", "Nada: un barco de acero nunca se hunde", "No: con demasiado peso, su densidad supera la del agua."),
     ("b", "Su densidad puede superar la del agua y se hunde", "¡Así es! La carga aumenta su densidad, y con demasiado peso se hunde."),
     ("c", "Flota más alto", "Al revés: con más carga, el barco se hunde más.")], fuentes=["sciam-barco"]),
   card("c7", "revelar", titulo="La forma importa", texto="Con la misma cantidad de material, un objeto puede flotar más o menos. ¿De qué depende?",
        revelado="De su forma: al cambiarla, el objeto desplaza más o menos agua, y así cambia su flotación.", fuentes=["noaa-flota"]),
   card("c8", "dato", texto="Los vehículos que bajan a explorar el fondo del mar cambian su masa bombeando agua hacia adentro o sacándola. Así se hunden y vuelven a subir.", fuentes=["noaa-flota"])],
  ("El barco de acero", ["El agua empuja hacia arriba con una fuerza igual al peso del agua desplazada: el principio de Arquímedes.",
                         "Un casco de acero encierra aire; juntos, acero y aire son menos densos que el agua.",
                         "Con demasiada carga, la densidad del barco supera la del agua y se hunde."]),
  [src("sciam-barco", "Science Buddies, publicado en Scientific American", "Shipping Science: Building a Boat That Can Carry Cargo", "https://www.scientificamerican.com/article/bring-science-home-shipping-science", "Texto de fondo (Background)",
       ["Un perno de acero que cae a un balde con agua se hunde rápidamente", "Si un objeto es más denso que el fluido, se hunde", "Un barco vacío con casco de acero encierra un volumen de aire; flota porque su densidad es menor que la del agua", "Al agregar carga aumenta su densidad; con demasiado peso supera la del agua y se hunde"],
       ["c1", "c2", "c5", "c6"], HOY),
   src("noaa-flota", "NOAA Ocean Exploration", "Deep East 2001 — Come on Down! (plan de clase, 7.° y 8.° grado)", "https://oceanexplorer.noaa.gov/edu/lessonplans/come_down.pdf", "Información de fondo",
       ["La flotación de un objeto depende de su densidad; un objeto menos denso que el medio que lo rodea flota", "Un objeto sumergido recibe un empuje hacia arriba igual al peso del fluido que desplaza (principio de Arquímedes)", "Cambiar la forma hace que el objeto desplace más o menos agua, y cambia su flotación", "Los vehículos sumergibles cambian su masa bombeando agua hacia adentro o expulsándola"],
       ["c2", "c3", "c7", "c8"], HOY),
   src("kids-arquimedes", "Britannica (Britannica Kids, Students)", "Archimedes' principle", "https://kids.britannica.com/students/article/Archimedes-principle/599600", "Texto principal",
       ["La fuerza de empuje es igual al peso del fluido desplazado por el objeto", "Un barco flota a la profundidad en que el peso del agua que desplaza es igual a su propio peso"],
       ["c3", "c4"], HOY)]))

# =================================================================== 07-11 rieles-horizonte (arte)
L = "rieles-horizonte"; A = arrow_def(L)
def rails(vx=160, vy=60, y0=190, half=110, ties=True):
    out = f'<line x1="0" y1="{vy}" x2="320" y2="{vy}" class="as-svg__muted"/>'
    out += poly([(vx - half, y0), (vx, vy), (vx + half, y0)], "as-svg__warm")
    if ties:
        for t in (0.15, 0.3, 0.45, 0.6, 0.75, 0.9):
            y = vy + (y0 - vy) * t; w = half * t
            out += f'<line x1="{vx - w}" y1="{y:.1f}" x2="{vx + w}" y2="{y:.1f}" class="as-svg__ink"/>'
    out += f'<line x1="{vx - half}" y1="{y0}" x2="{vx}" y2="{vy}" class="as-svg__ink" stroke-width="3"/><line x1="{vx + half}" y1="{y0}" x2="{vx}" y2="{vy}" class="as-svg__ink" stroke-width="3"/>'
    return out
V = VIS[L] = {
 "c1": svg("Una vía de tren vista desde adentro: los dos rieles parecen juntarse a lo lejos, en el horizonte",
   BG + rails() + text(160, 36, "¿se juntan?", 18)),
 "c2": svg("Un ojo mira dos postes iguales: el cercano ocupa un ángulo grande y el lejano un ángulo chico",
   BG + '<path d="M20 100 C34 84 54 84 68 100 C54 116 34 116 20 100 Z" class="as-svg__ink"/><circle cx="44" cy="100" r="7" class="as-svg__fill"/>' +
   box(120, 60, 14, 80, "as-svg__fill", 2) + box(260, 60, 14, 80, "as-svg__fill", 2) +
   '<line x1="56" y1="100" x2="120" y2="60" class="as-svg__ink" stroke-dasharray="4 4"/><line x1="56" y1="100" x2="120" y2="140" class="as-svg__ink" stroke-dasharray="4 4"/>'
   '<line x1="56" y1="100" x2="260" y2="60" class="as-svg__accent as-svg__ink" stroke-dasharray="2 4"/><line x1="56" y1="100" x2="260" y2="140" class="as-svg__accent as-svg__ink" stroke-dasharray="2 4"/>' +
   text(127, 168, "cerca:", 15) + text(127, 188, "ángulo grande", 15) + text(267, 168, "lejos:", 15) + text(267, 188, "ángulo chico", 15) +
   text(190, 36, "lo mismo, cerca y lejos", 16)),
 "c3": svg("El espacio entre los rieles se ve cada vez más angosto a lo lejos, hasta que parecen juntarse",
   BG + rails(ties=False) +
   '<line x1="80" y1="170" x2="240" y2="170" class="as-svg__ink as-svg__accent" stroke-width="3"/>'
   '<line x1="122" y1="125" x2="198" y2="125" class="as-svg__ink as-svg__accent" stroke-width="3"/>'
   '<line x1="145" y1="96" x2="175" y2="96" class="as-svg__ink as-svg__accent" stroke-width="3"/>' +
   text(160, 36, "cada vez más angosto", 17)),
 "c5": svg("El sistema visual interpreta las líneas que convergen como paralelas que se alejan hacia el horizonte",
   BG + A + rails() + arrow(L, 300, 170, 252, 122, 2) + text(254, 28, "paralelas", 16) + text(254, 48, "que se alejan", 16) +
   text(62, 28, "pista de", 16) + text(62, 48, "profundidad", 16)),
 "c6": svg("La ilusión de Ponzo: dos barras iguales entre líneas que se juntan; la que parece más lejos se ve más larga",
   BG + '<line x1="80" y1="190" x2="160" y2="30" class="as-svg__ink" stroke-width="2"/><line x1="240" y1="190" x2="160" y2="30" class="as-svg__ink" stroke-width="2"/>' +
   '<rect x="130" y="76" width="60" height="8" class="as-svg__fill"/><rect x="130" y="150" width="60" height="8" class="as-svg__fill"/>' +
   text(250, 84, "parece", 15, "start") + text(250, 102, "más larga", 15, "start") + text(26, 150, "son", 15, "start") + text(26, 168, "iguales", 15, "start")),
 "c8": svg("Un cuadro con perspectiva lineal: las líneas se juntan en el punto de fuga; Brunelleschi hacia 1415 y Alberti en 1435",
   BG + box(30, 30, 180, 130, "as-svg__soft", 4) + '<line x1="30" y1="90" x2="210" y2="90" class="as-svg__muted"/>' +
   '<line x1="40" y1="160" x2="120" y2="90" class="as-svg__ink"/><line x1="200" y1="160" x2="120" y2="90" class="as-svg__ink"/>'
   '<line x1="30" y1="40" x2="120" y2="90" class="as-svg__ink"/><line x1="210" y1="40" x2="120" y2="90" class="as-svg__ink"/>' +
   '<circle cx="120" cy="90" r="5" class="as-svg__fill"/>' + text(120, 184, "punto de fuga", 15) +
   text(266, 70, "Brunelleschi", 15) + text(266, 90, "hacia 1415", 15) + text(266, 126, "Alberti", 15) + text(266, 146, "1435", 15)),
}
LOTE.append(lesson(L, "Arte y percepción", "arte",
  "¿Por qué los rieles parecen juntarse a lo lejos?", "Lo que pasa en el ojo y lo que aprovecharon los pintores.",
  [card("c1", "portada", titulo="¿Por qué los rieles parecen juntarse a lo lejos?", texto="Si te paras en una vía de tren, los dos rieles parecen juntarse a lo lejos. Pero son paralelos. ¿Qué está pasando?", fuentes=["msu-ponzo"]),
   card("c2", "idea", titulo="Lo lejano se ve más chico", texto="Mientras más lejos está algo, más pequeño es el ángulo que ocupa en nuestra vista: su imagen en el ojo se achica.", fuentes=["yorku-persp"]),
   card("c3", "idea", titulo="El espacio entre los rieles", texto="Lo mismo pasa con el espacio entre los dos rieles: a lo lejos se ve cada vez más angosto, y los rieles parecen converger hacia el horizonte.", fuentes=["yorku-persp", "msu-ponzo"]),
   card("c4", "pregunta", pregunta="Dos postes iguales, uno cerca y otro lejos. ¿Cuál ocupa un ángulo más chico en tu vista?", correctaId="a", opciones=[
     ("a", "El que está lejos", "¡Exacto! Mientras más lejos está algo, más chico es el ángulo que ocupa."),
     ("b", "El que está cerca", "Al revés: el cercano ocupa un ángulo más grande."),
     ("c", "Los dos ocupan lo mismo", "No: aunque son iguales, el lejano ocupa un ángulo más chico.")], fuentes=["yorku-persp"]),
   card("c5", "idea", titulo="Una pista de profundidad", texto="Aun así, no creemos que los rieles se toquen: nuestro sistema visual interpreta esas líneas que convergen como paralelas que se alejan hacia el horizonte.", fuentes=["msu-ponzo"]),
   card("c6", "revelar", titulo="La ilusión de Ponzo", texto="Entre dos líneas que se juntan, como rieles, se dibujan dos barras iguales. ¿Cuál parece más larga?",
        revelado="La que parece estar más lejos. Si dos cosas se ven del mismo tamaño pero una parece más lejana, la percibimos más grande. Al borrar las líneas, se nota que las barras son iguales.", fuentes=["msu-ponzo"]),
   card("c7", "pregunta", pregunta="En un dibujo con perspectiva lineal, ¿dónde se juntan las líneas paralelas?", correctaId="b", opciones=[
     ("a", "En una esquina del cuadro", "No: se juntan en un punto de la línea del horizonte."),
     ("b", "En un punto de fuga, sobre la línea del horizonte", "¡Así es! Y los objetos se dibujan más chicos a medida que se acercan a ese punto."),
     ("c", "No se juntan nunca", "En la realidad no, pero en el dibujo con perspectiva sí: en el punto de fuga.")], fuentes=["brit-lineal", "brit-fuga"]),
   card("c8", "dato", texto="Los pintores usan este mismo efecto para crear profundidad. Se cree que el arquitecto Filippo Brunelleschi ideó la perspectiva lineal hacia 1415, y Leon Battista Alberti la explicó por escrito en 1435.", fuentes=["brit-lineal"])],
  ("Los rieles que se juntan", ["Mientras más lejos está algo, más chico es el ángulo que ocupa en nuestra vista.",
                                "El espacio entre los rieles se ve cada vez más angosto a lo lejos, y el sistema visual lo interpreta como profundidad.",
                                "Los pintores usan la perspectiva lineal: las paralelas se juntan en un punto de fuga sobre el horizonte."]),
  [src("yorku-persp", "York University (Canadá)", "Perspective Illusion", "https://www.yorku.ca/eye/perspect.htm", "Texto principal",
       ["Mientras más lejos están los objetos, menor es el ángulo visual que ocupan en la retina", "Los patrones del suelo, las paredes y el techo tienden a converger hacia un punto común en la distancia"],
       ["c2", "c3", "c4"], HOY),
   src("msu-ponzo", "Mississippi State University (ePsych)", "Ponzo illusion", "https://epsych.msstate.edu/descriptive/Vision/DepthValley/ponzo/4.html", "Texto principal",
       ["Parado sobre una vía de tren, los dos rieles paralelos parecen converger hacia el horizonte", "El sistema visual interpreta las líneas como paralelas que se proyectan hacia el horizonte", "La ilusión de Ponzo usa claves de profundidad, como líneas convergentes, para sugerir distancia", "Si dos objetos tienen el mismo tamaño visual pero uno está más lejos, el más lejano se percibe más grande", "Al quitar las líneas se ve que las barras miden lo mismo"],
       ["c1", "c3", "c5", "c6"], HOY),
   src("brit-lineal", "Encyclopaedia Britannica", "Linear perspective", "https://www.britannica.com/art/linear-perspective", "Texto principal",
       ["Sistema para crear la ilusión de profundidad en una superficie plana", "Las líneas paralelas convergen en un único punto de fuga en la línea del horizonte", "Los objetos se dibujan cada vez más pequeños a medida que se acercan al punto de fuga", "Se cree que Brunelleschi lo ideó hacia 1415; Alberti lo documentó en 1435 (Della pittura)"],
       ["c7", "c8"], HOY),
   src("brit-fuga", "Encyclopaedia Britannica", "Vanishing point", "https://www.britannica.com/art/vanishing-point", "Resumen del artículo",
       ["Las líneas paralelas (ortogonales) convergen en el punto de fuga, sobre la línea del horizonte", "Los objetos se dibujan más pequeños al acercarse al punto de fuga"],
       ["c7"], HOY)]))

# =================================================================== 08-11 hielo-flota (física)
L = "hielo-flota"; A = arrow_def(L)
V = VIS[L] = {
 "c1": svg("Un vaso con agua y un cubo de hielo flotando arriba, no en el fondo",
   BG + glass(120, 50, 80, 120) + box(146, 58, 28, 26, "as-svg__soft", 4) + text(160, 34, "¿por qué flota?", 17) +
   text(250, 72, "hielo", 16) + text(250, 140, "agua", 16)),
 "c2": svg("Un cubo de hielo y un cubo de agua del mismo tamaño en una balanza: el hielo pesa menos, cerca del 90 %",
   BG + '<line x1="160" y1="70" x2="160" y2="170" class="as-svg__ink" stroke-width="3"/><path d="M130 180 L190 180 L160 166 Z" class="as-svg__warm"/>' +
   '<line x1="70" y1="60" x2="250" y2="80" class="as-svg__ink" stroke-width="3"/>' +
   box(60, 24, 40, 36, "as-svg__soft", 3) + box(220, 44, 40, 36, "as-svg__cool", 3) +
   text(80, 84, "hielo", 16) + text(240, 104, "agua", 16) + text(80, 140, "≈ 90 %", 17) +
   text(160, 196, "mismo tamaño", 15)),
 "c4": svg("En el hielo las moléculas forman una red ordenada; en el agua líquida están más desordenadas",
   BG + box(20, 30, 130, 110, "as-svg__soft", 8) + dots([(40 + i * 22, 50 + j * 22) for i in range(5) for j in range(4)], 5, "as-svg__fill") +
   box(170, 30, 130, 110, "as-svg__cool", 8) + dots([(186, 50), (214, 62), (240, 46), (270, 58), (290, 80), (196, 86), (228, 92), (258, 100), (184, 118), (212, 124), (246, 130), (280, 120), (230, 70), (270, 86)], 5, "as-svg__sun") +
   text(85, 164, "hielo: ordenadas", 15) + text(235, 164, "líquido: al azar", 15) + text(160, 190, "el hielo es ≈ 9 % menos denso", 15)),
 "c5": svg("Un iceberg: cerca del 10 % queda sobre el agua y casi todo su volumen queda bajo el agua",
   BG + '<rect x="0" y="70" width="320" height="130" class="as-svg__cool"/>' + waves(4, 316, 70, 4, 24) +
   poly([(140, 70), (160, 40), (178, 54), (190, 70)], "as-svg__soft") + poly([(140, 70), (160, 40), (178, 54), (190, 70)], "as-svg__ink") +
   poly([(140, 70), (190, 70), (240, 120), (220, 180), (130, 186), (96, 130)], "as-svg__soft") + poly([(140, 70), (190, 70), (240, 120), (220, 180), (130, 186), (96, 130)], "as-svg__ink") +
   text(250, 50, "≈ 10 %", 17) + text(166, 140, "casi todo", 16) + text(166, 160, "bajo el agua", 16)),
 "c7": svg("Si el agua más fría fuera la más densa, se hundiría y el lago podría congelarse desde el fondo",
   BG + A + box(20, 50, 130, 100, "as-svg__cool", 4) + '<rect x="20" y="50" width="130" height="16" class="as-svg__soft"/>' +
   box(170, 50, 130, 100, "as-svg__cool", 4) + '<rect x="170" y="128" width="130" height="22" class="as-svg__soft"/>' + arrow(L, 235, 62, 235, 120, 3) +
   text(85, 36, "lo real", 16) + text(85, 172, "hielo arriba", 15) + text(235, 36, "si se hundiera", 16) + text(235, 172, "se congela", 15) + text(235, 192, "desde el fondo", 15)),
 "c8": svg("Hielo común flota en un vaso; hielo pesado, un 10,6 % más denso, se va al fondo",
   BG + glass(40, 50, 80, 120) + box(66, 58, 26, 24, "as-svg__soft", 4) + glass(200, 50, 80, 120) + box(226, 138, 26, 24, "as-svg__warm", 4) +
   text(80, 190, "hielo común", 15) + text(240, 190, "hielo pesado", 15) + text(240, 34, "10,6 % más denso", 15)),
}
LOTE.append(lesson(L, "Ciencia cotidiana", "fisica",
  "¿Por qué el hielo flota?", "El agua sólida es menos densa que la líquida.",
  [card("c1", "portada", titulo="¿Por qué el hielo flota?", texto="Echas hielo a un vaso con agua y queda flotando arriba. ¿Por qué el agua sólida flota sobre el agua líquida?", fuentes=["usgs-dens"]),
   card("c2", "idea", titulo="Menos denso que el agua", texto="El hielo flota porque es menos denso que el agua líquida. Su densidad es cerca del 90 % de la del agua, aunque varía, porque el hielo puede tener aire adentro.", fuentes=["usgs-dens"]),
   card("c3", "pregunta", pregunta="Al congelarse, ¿qué le pasa a la densidad del agua?", correctaId="a", opciones=[
     ("a", "Baja, cerca de un 9 %", "¡Exacto! Por eso el hielo queda arriba."),
     ("b", "Sube mucho", "Al revés: el hielo es menos denso que el agua líquida."),
     ("c", "Queda igual", "No: al congelarse, la densidad baja cerca de un 9 %.")], fuentes=["usgs-dens"]),
   card("c4", "idea", titulo="Una red ordenada", texto="En el hielo, las moléculas de agua se ordenan en una red regular; en el agua líquida están más al azar. Al congelarse, la densidad baja cerca de un 9 %.", fuentes=["usgs-dens"]),
   card("c5", "revelar", titulo="La punta del iceberg", texto="Un iceberg flota igual que un cubo de hielo en un vaso. ¿Qué parte queda sobre el agua?",
        revelado="Solo cerca del 10 %. Casi todo su volumen queda bajo el agua.", fuentes=["usgs-dens", "usgs-iceberg"]),
   card("c6", "pregunta", pregunta="El agua líquida es más densa cerca de los 4 °C que a 0 °C. En un lago, ¿qué hace esa agua de 4 °C?", correctaId="b", opciones=[
     ("a", "Sube a la superficie", "Al revés: el agua más densa se hunde."),
     ("b", "Se hunde bajo el agua menos densa", "¡Así es! El agua más densa queda abajo."),
     ("c", "Se congela primero", "No: a 4 °C el agua sigue líquida; por ser más densa, se va al fondo.")], fuentes=["usgs-dens"]),
   card("c7", "idea", titulo="Si el hielo se hundiera", texto="Si el agua más fría fuera la más densa, en invierno el agua helada de la superficie se hundiría, y un lago podría congelarse desde el fondo hacia arriba.", fuentes=["usgs-dens"]),
   card("c8", "dato", texto="Existe un \"hielo pesado\", hecho de agua pesada. Es un 10,6 % más denso que el agua común, así que un cubo de ese hielo se hundiría en un vaso de agua normal.", fuentes=["usgs-dens"])],
  ("El hielo que flota", ["El hielo flota porque es menos denso que el agua líquida: al congelarse, la densidad baja cerca de un 9 %.",
                          "En el hielo, las moléculas forman una red ordenada, y un iceberg asoma solo cerca del 10 %.",
                          "Si el agua más fría fuera la más densa, un lago podría congelarse desde el fondo."]),
  [src("usgs-dens", "U.S. Geological Survey (USGS), Water Science School", "Water Density", "https://www.usgs.gov/water-science-school/science/water-density", "Secciones \"Ice is less dense than water\" y \"Water's density varies with temperature\"",
       ["El hielo es menos denso que el agua líquida, por eso flota", "La densidad del hielo es cerca del 90 % de la del agua, pero varía porque el hielo puede contener aire", "Al congelarse, la densidad baja cerca de un 9 %", "En el hielo las moléculas se alinean en una red regular, y no al azar como en el líquido", "Cerca del 10 % de un cubo de hielo o de un iceberg queda sobre la línea del agua", "El agua a unos 4 °C es más densa que a 0 °C, y el agua más densa se hunde bajo la menos densa", "Si el agua fuera más densa en el punto de congelación, en invierno se hundiría y el lago podría congelarse de abajo hacia arriba", "El hielo pesado es 10,6 % más denso que el agua normal y se hunde en ella"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"], HOY),
   src("usgs-iceberg", "U.S. Geological Survey (USGS)", "Ninety percent of an iceberg is below the waterline (imagen)", "https://www.usgs.gov/media/images/ninety-percent-iceberg-below-waterline", "Título y descripción de la imagen",
       ["El noventa por ciento de un iceberg está bajo la línea del agua", "La mayor parte de un iceberg está bajo la superficie"],
       ["c5"], HOY)]))

# =================================================================== 09-11 imprenta-libros (historia)
L = "imprenta-libros"; A = arrow_def(L)
def openbook(x, y, w=120, h=60, cls="as-svg__warm"):
    m = x + w / 2
    d = f"M{x} {y} C{x + w * 0.2} {y - 10} {m - 10} {y - 10} {m} {y} C{m + 10} {y - 10} {x + w * 0.8} {y - 10} {x + w} {y} L{x + w} {y + h} C{x + w * 0.8} {y + h - 10} {m + 10} {y + h - 10} {m} {y + h} C{m - 10} {y + h - 10} {x + w * 0.2} {y + h - 10} {x} {y + h} Z"
    return shape(d, cls) + f'<line x1="{m}" y1="{y}" x2="{m}" y2="{y + h}" class="as-svg__ink"/>'
def press(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">' + box(0, 0, 14, 110, "as-svg__fill", 2) + box(86, 0, 14, 110, "as-svg__fill", 2) +
            box(0, 0, 100, 16, "as-svg__fill", 2) + '<line x1="50" y1="16" x2="50" y2="50" class="as-svg__ink" stroke-width="3"/>' +
            box(22, 50, 56, 12, "as-svg__warm", 2) + box(14, 80, 72, 10, "as-svg__soft", 2) + '</g>')
V = VIS[L] = {
 "c1": svg("Un libro abierto y una prensa de imprimir: antes de la imprenta, un libro era caro y lento de hacer",
   BG + openbook(20, 80, 120, 70) + press(190, 50, 0.9) + text(80, 40, "caro y lento", 17) + text(235, 186, "imprenta", 16)),
 "c2": svg("Un libro copiado a mano con pluma: era laborioso y costaba lo que ganaba en un mes un funcionario de la corte",
   BG + openbook(20, 60, 130, 80) +
   "".join(f'<line x1="{x}" y1="{y}" x2="{x + 40}" y2="{y}" class="as-svg__ink"/>' for x in (32, 96) for y in (78, 92, 106, 120)) +
   shape("M180 30 C210 40 216 70 196 96 L190 110 L184 106 L188 92 C170 78 170 50 180 30 Z", "as-svg__fill") +
   text(264, 70, "copiado", 16) + text(264, 90, "a mano", 16) + text(160, 168, "costaba un mes de sueldo", 16) + text(160, 190, "de un funcionario de la corte", 15, muted=True)),
 "c3": svg("Tipos metálicos móviles y una prensa manual: Gutenberg, en Estrasburgo y Maguncia, en las décadas de 1440 y 1450",
   BG + "".join(box(24 + i * 30, 70, 26, 30, "as-svg__warm", 3) + text(37 + i * 30, 91, ch, 17) for i, ch in enumerate("TIPOS")) +
   press(200, 40, 0.9) + text(85, 130, "tipos de metal", 16) + text(85, 150, "móviles", 16) + text(245, 30, "prensa", 16) +
   text(110, 176, "Estrasburgo y Maguncia", 15) + text(110, 194, "décadas de 1440 y 1450", 15)),
 "c5": svg("Muchos libros a un costo relativamente bajo: los impresos llegan a más gente",
   BG + "".join(box(30 + i * 22, 140 - j * 22, 20, 22, "as-svg__warm" if (i + j) % 2 else "as-svg__fill", 2) for i in range(5) for j in range(4 - i % 2)) +
   openbook(180, 70, 110, 60, "as-svg__soft") + text(85, 40, "muchos libros", 16) + text(235, 160, "más lectores", 16) + text(235, 180, "y educación", 15, muted=True)),
 "c6": svg("La Biblia de Gutenberg, hacia 1455: unas 180 copias, 145 en papel y 35 en pergamino, en columnas de 42 líneas",
   BG + box(30, 40, 80, 110, "as-svg__soft", 3) +
   "".join(f'<line x1="40" y1="{y}" x2="66" y2="{y}" class="as-svg__ink"/><line x1="74" y1="{y}" x2="100" y2="{y}" class="as-svg__ink"/>' for y in range(52, 142, 8)) +
   text(70, 174, "42 líneas", 15) + text(220, 50, "≈ 180 copias", 17) +
   box(144, 76, 132, 24, "as-svg__warm", 3) + text(210, 94, "145 papel", 15) + box(144, 110, 132, 24, "as-svg__soft", 3) + text(210, 128, "35 pergamino", 15) +
   text(220, 172, "Maguncia, ≈ 1455", 16)),
 "c8": svg("La imprenta se difundió rápido por Europa; en Chile, la Aurora de Chile se imprimió en 1812",
   BG + A + '<circle cx="80" cy="90" r="10" class="as-svg__fill"/>' + arrow(L, 92, 82, 130, 56) + arrow(L, 92, 96, 136, 120) + arrow(L, 70, 80, 40, 50) +
   text(80, 160, "Europa", 16) + box(190, 50, 110, 90, "as-svg__warm", 4) + text(245, 76, "Aurora", 16) + text(245, 96, "de Chile", 16) +
   '<line x1="204" y1="110" x2="286" y2="110" class="as-svg__ink"/><line x1="204" y1="122" x2="270" y2="122" class="as-svg__ink"/>' + text(245, 168, "1812", 18)),
}
LOTE.append(lesson(L, "Historia", "historia",
  "¿Cómo cambió los libros la imprenta?", "De copiar a mano a imprimir muchas copias.",
  [card("c1", "portada", titulo="¿Cómo cambió los libros la imprenta?", texto="Antes de la imprenta, hacer un libro en Europa era caro y lento. ¿Qué cambió con la prensa de Gutenberg?", fuentes=["utas-impr"]),
   card("c2", "idea", titulo="Libros escasos y caros", texto="Copiar un libro a mano era un trabajo laborioso y costoso. Un manuscrito encuadernado costaba lo que ganaba en un mes un funcionario de la corte.", fuentes=["uwm-manus"]),
   card("c3", "idea", titulo="Tipos de metal y una prensa", texto="En las décadas de 1440 y 1450, Johann Gutenberg desarrolló en Estrasburgo y Maguncia la imprenta: tipos metálicos móviles y una prensa manual.", fuentes=["utas-impr"]),
   card("c4", "pregunta", pregunta="¿Qué cambió con la prensa de Gutenberg?", correctaId="a", opciones=[
     ("a", "Se pudieron fabricar muchos libros a un costo relativamente bajo", "¡Exacto! Fue la primera vez en Europa que eso fue posible."),
     ("b", "Los libros se volvieron más caros", "Al revés: el costo por libro bajó."),
     ("c", "Se dejó de usar papel", "No: la mayoría de las Biblias de Gutenberg, por ejemplo, se imprimieron en papel.")], fuentes=["brit-gutenberg", "loc-biblia"]),
   card("c5", "idea", titulo="Más libros, más lectores", texto="Por primera vez en Europa se pudo fabricar una gran cantidad de libros con un costo relativamente bajo. Los impresos llegaron a más gente, lo que favoreció la alfabetización y la educación.", fuentes=["brit-gutenberg"]),
   card("c6", "revelar", titulo="La Biblia de Gutenberg", texto="Hacia 1455 salió en Maguncia su obra más famosa. ¿Cuántas copias se imprimieron?",
        revelado="Unas 180: 145 en papel y 35 en pergamino de piel de ternero. Se imprimió en columnas de 42 líneas.", fuentes=["loc-biblia", "brit-biblia"]),
   card("c7", "pregunta", pregunta="¿Fue Gutenberg el primero en imprimir con tipos móviles de metal?", correctaId="b", opciones=[
     ("a", "Sí, nadie lo había hecho antes", "No: hay evidencia de que en Corea se usaron casi un siglo antes."),
     ("b", "No: en Corea se usaron casi un siglo antes", "¡Así es! Lo de Gutenberg fue el primer libro con tipos metálicos móviles en Europa occidental."),
     ("c", "No: los inventaron los romanos", "No: la evidencia más antigua citada viene de Corea, casi un siglo antes de Gutenberg.")], fuentes=["loc-biblia", "brit-gutenberg"]),
   card("c8", "dato", texto="La imprenta se difundió rápido por Europa. Y en Chile, la Aurora de Chile, primer periódico de la República, se imprimió en 1812.", fuentes=["utas-impr", "mc-aurora"])],
  ("La imprenta", ["Antes, los libros se copiaban a mano: eran lentos de hacer y caros.",
                   "Gutenberg desarrolló en Maguncia tipos metálicos móviles y una prensa, y su Biblia salió hacia 1455.",
                   "Se pudieron hacer muchos libros a menor costo y llegaron a más lectores."]),
  [src("utas-impr", "University of Tasmania Library", "From Manuscript to Print (exposición en línea)", "https://www.utas.edu.au/library/exhibitions/manuscript_print/intro.html", "Introducción",
       ["Los manuscritos eran relativamente caros y lentos de producir", "La imprenta fue desarrollada por Johann Gutenberg en Estrasburgo y Maguncia en las décadas de 1440 y 1450, con tipos metálicos móviles y prensa manual", "La imprenta se difundió rápidamente por Europa"],
       ["c1", "c3", "c8"], HOY),
   src("uwm-manus", "University of Wisconsin-Milwaukee Libraries, Special Collections", "The Manuscript Tradition and the Transition to Printing", "https://web.uwm.edu/lib-omeka-spc2/exhibits/show/incunabula/manuscripttrad", "Texto principal",
       ["Copiar manuscritos a mano era un trabajo laborioso y costoso", "Un manuscrito encuadernado costaba lo que un funcionario de la corte promedio recibía en un mes"],
       ["c2"], HOY),
   src("brit-gutenberg", "Encyclopaedia Britannica", "What did Johannes Gutenberg do to change the world?", "https://britannica.com/question/What-did-Johannes-Gutenberg-do-to-change-the-world", "Respuesta",
       ["Su prensa permitió por primera vez en Europa fabricar gran cantidad de libros a un costo relativamente bajo", "Los impresos llegaron a un público general, lo que favoreció la alfabetización y la educación", "Gutenberg no inventó la impresión con tipos móviles, que ocurrió en Corea en el siglo XIV"],
       ["c4", "c5", "c7"], HOY),
   src("loc-biblia", "Library of Congress (EE. UU.)", "The Gutenberg Bible (exposición)", "https://www.loc.gov/exhibits/bibles/interactives/gutenberg/index.html", "Texto principal",
       ["Se imprimieron unas 180 copias, disponibles hacia 1455; 145 en papel y 35 en pergamino (vellum, piel de ternero tratada)", "Primer libro impreso con tipos metálicos móviles en Europa occidental", "Hay evidencia de que en Corea se usaron tipos metálicos móviles casi un siglo antes"],
       ["c4", "c6", "c7"], HOY),
   src("brit-biblia", "Encyclopaedia Britannica", "Gutenberg Bible", "https://www.britannica.com/topic/Gutenberg-Bible", "Texto principal",
       ["Gutenberg la completó hacia 1455 en Maguncia (Mainz)", "Se imprimió en columnas de 42 líneas"],
       ["c6"], HOY),
   src("mc-aurora", "Memoria Chilena, Biblioteca Nacional de Chile", "Imagen corporativa de la Aurora de Chile, 1812", "https://www.memoriachilena.gob.cl/602/w3-article-84574.html", "Descripción de la imagen",
       ["La Aurora de Chile, de 1812, fue el primer periódico de la República"],
       ["c8"], HOY)]))

# =================================================================== 10-11 jabon-grasa (química)
L = "jabon-grasa"; A = arrow_def(L)
def mol(x, y, ang=0, s=1.0):
    """Molécula de jabón: cabeza (se une al agua) y cola (se pega a la grasa)."""
    return (f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
            '<path d="M8 0 L18 -5 L28 5 L38 -5 L48 5 L56 0" class="as-svg__ink" stroke-width="2"/>'
            '<circle cx="0" cy="0" r="8" class="as-svg__fill"/><circle cx="0" cy="0" r="8" class="as-svg__ink"/></g>')
V = VIS[L] = {
 "c1": svg("Un plato con una mancha de grasa y burbujas de jabón",
   BG + '<ellipse cx="140" cy="120" rx="110" ry="50" class="as-svg__soft"/><ellipse cx="140" cy="120" rx="110" ry="50" class="as-svg__ink"/>'
   '<ellipse cx="140" cy="120" rx="70" ry="30" class="as-svg__ink"/><path d="M110 116 C120 104 150 108 160 118 C170 130 130 136 112 128 Z" class="as-svg__warm"/>' +
   "".join(f'<circle cx="{x}" cy="{y}" r="{r}" class="as-svg__ink"/>' for x, y, r in [(250, 60, 14), (276, 90, 9), (230, 40, 7), (290, 50, 11)]) +
   text(80, 40, "¿qué hace el jabón?", 16) + text(136, 190, "grasa", 15)),
 "c2": svg("Una molécula de jabón: una parte se une al agua y la otra rehúye el agua y se pega a la grasa",
   BG + A + mol(110, 100, 0, 2.2) + arrow(L, 110, 40, 110, 76, 2) + arrow(L, 220, 150, 200, 114, 2) +
   text(110, 30, "se une al agua", 16) + text(220, 172, "se pega a la grasa", 16)),
 "c4": svg("Sin jabón, una gota de agua queda abultada; con jabón, el agua se extiende y moja mejor",
   BG + '<line x1="20" y1="130" x2="300" y2="130" class="as-svg__ink" stroke-width="2"/>' +
   '<path d="M60 130 C60 96 120 96 120 130 Z" class="as-svg__cool"/><path d="M60 130 C60 96 120 96 120 130" class="as-svg__ink"/>' +
   '<path d="M180 130 C190 118 280 118 296 130 Z" class="as-svg__cool"/><path d="M180 130 C190 118 280 118 296 130" class="as-svg__ink"/>' +
   text(90, 160, "sin jabón", 16) + text(238, 160, "con jabón", 16) + text(238, 182, "se extiende", 15, muted=True) + text(160, 50, "el agua moja mejor", 17)),
 "c5": svg("La capa de grasa se rompe en gotitas rodeadas de jabón, y la suciedad queda suspendida en el agua",
   BG + A + '<rect x="10" y="150" width="120" height="14" rx="4" class="as-svg__warm"/><rect x="10" y="150" width="120" height="14" rx="4" class="as-svg__ink"/>' +
   text(70, 140, "capa de grasa", 15) + arrow(L, 138, 120, 168, 120, 3) +
   '<rect x="176" y="30" width="134" height="150" rx="8" class="as-svg__soft"/>' +
   "".join(f'<circle cx="{x}" cy="{y}" r="12" class="as-svg__warm"/><circle cx="{x}" cy="{y}" r="12" class="as-svg__ink"/>' +
           "".join(mol(x + 24 * math.cos(a), y + 24 * math.sin(a), a * 57.2958 + 180, 0.35) for a in (0, 1.57, 3.14, 4.71))
           for x, y in [(212, 64), (276, 92), (224, 144)]) +
   text(243, 196, "gotitas en el agua", 15)),
 "c7": svg("Hace al menos 2.300 años ya se conocía el jabón: los fenicios lo hacían con sebo de cabra y ceniza de madera",
   BG + A + shape("M110 90 L210 90 L200 150 L120 150 Z", "as-svg__fill") +
   box(30, 40, 60, 30, "as-svg__warm", 4) + text(60, 60, "sebo", 15) + box(230, 40, 60, 30, "as-svg__soft", 4) + text(260, 60, "ceniza", 15) +
   arrow(L, 92, 64, 124, 88) + arrow(L, 228, 64, 196, 88) + text(160, 196, "al menos 2.300 años", 15)),
 "c8": svg("En agua dura el jabón forma un grumo; a los detergentes sintéticos esas sales casi no les afectan",
   BG + glass(40, 50, 80, 120) + "".join(f'<circle cx="{x}" cy="78" r="5" class="as-svg__warm"/>' for x in range(52, 112, 10)) +
   glass(200, 50, 80, 120) +
   text(80, 30, "jabón", 16) + text(240, 30, "detergente", 16) + text(80, 190, "grumo", 15) + text(240, 190, "casi no cambia", 15) +
   text(160, 110, "agua dura", 15, muted=True)),
}
LOTE.append(lesson(L, "Química cotidiana", "quimica",
  "¿Por qué el jabón ayuda a quitar la grasa?", "Una molécula con un lado para el agua y otro para la grasa.",
  [card("c1", "portada", titulo="¿Por qué el jabón ayuda a quitar la grasa?", texto="Para lavar un plato con grasa usamos jabón. ¿Cómo ayuda? La respuesta está en cómo son sus moléculas.", fuentes=["brit-jabon"]),
   card("c2", "idea", titulo="Una molécula con dos lados", texto="Cada molécula de jabón tiene una parte que se une al agua y otra que rehúye el agua y se pega a la suciedad.", fuentes=["brit-jabon"]),
   card("c3", "pregunta", pregunta="¿Qué parte de la molécula de jabón se pega a la grasa?", correctaId="a", opciones=[
     ("a", "La parte que rehúye el agua", "¡Exacto! Esa parte se pega a la suciedad, y la otra se une al agua."),
     ("b", "La parte que se une al agua", "No: esa parte queda hacia el agua. La que rehúye el agua es la que se pega a la grasa."),
     ("c", "Ninguna: el jabón solo calienta la grasa", "No: el jabón se pega a la suciedad con la parte que rehúye el agua.")], fuentes=["brit-jabon"]),
   card("c4", "idea", titulo="El agua moja mejor", texto="El jabón baja la tensión superficial del agua. Así, el agua se extiende y moja mejor.", fuentes=["brit-jabon"]),
   card("c5", "idea", titulo="La grasa se separa en gotitas", texto="Con el jabón, la capa de aceite se rompe y se separa en gotitas, y la suciedad queda suspendida en el agua.", fuentes=["brit-jabon"]),
   card("c6", "pregunta", pregunta="¿Con qué se hace el jabón?", correctaId="b", opciones=[
     ("a", "Con arena y agua", "No: se hace a partir de grasas o aceites."),
     ("b", "Con grasas o aceites tratados con un álcali, como la soda cáustica", "¡Así es! Esa reacción produce las moléculas de jabón."),
     ("c", "Con sal de mesa y vinagre", "No: se hace a partir de grasas o aceites y un álcali.")], fuentes=["brit-jabon"]),
   card("c7", "revelar", titulo="Un invento muy antiguo", texto="El jabón no es un invento moderno. ¿Desde cuándo se conoce?",
        revelado="Desde hace al menos 2.300 años. Según Plinio el Viejo, los fenicios lo preparaban con sebo de cabra y ceniza de madera.", fuentes=["brit-jabon"]),
   card("c8", "dato", texto="En el agua dura, que trae sales de calcio y otros metales, el jabón forma un grumo o nata. A los detergentes sintéticos, en cambio, esas sales casi no les afectan.", fuentes=["brit-jabon"])],
  ("El jabón y la grasa", ["Cada molécula de jabón tiene un lado que se une al agua y otro que se pega a la grasa.",
                           "El jabón ayuda al agua a mojar mejor y rompe la capa de grasa en gotitas que quedan en el agua.",
                           "Se hace con grasas o aceites y un álcali, y se conoce hace al menos 2.300 años."]),
  [src("brit-jabon", "Encyclopaedia Britannica", "Soap", "https://www.britannica.com/technology/soap", "Introducción y secciones \"History\" y \"Soap manufacturing processes and products\"",
       ["La parte hidrofóbica de la molécula se adhiere a la suciedad y la parte hidrofílica al agua", "Aumenta la capacidad del agua de extenderse y mojar al reducir su tensión superficial", "La película de aceite se rompe y se separa en gotitas; la suciedad queda suspendida", "El jabón se forma por reacción de ácidos grasos con un álcali; una solución alcalina caliente, como la soda cáustica, actúa sobre grasas o aceites", "Se conoce hace al menos 2.300 años; según Plinio el Viejo, los fenicios lo preparaban con sebo de cabra y ceniza de madera", "En agua dura el jabón forma una nata o precipitado con sales de calcio y otros metales; los detergentes sintéticos casi no se ven afectados"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"], HOY)]))

# Agrega las ilustraciones a la portada y a las tarjetas idea, revelar y dato.
for L_ in LOTE:
    for c in L_["tarjetas"]:
        if c["tipo"] in ("portada", "idea", "revelar", "dato"):
            c["visual"] = VIS[L_["id"]][c["id"]]

if __name__ == "__main__":
    for L_ in LOTE:
        validate_visuals(L_)
    for lid, rev, sha in write("lote4", LOTE):
        print(f"{lid} r{rev}  {sha[:12]}")
