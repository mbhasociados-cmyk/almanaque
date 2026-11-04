# Lote 5 (opción A, 04-11-2026): 7 lecciones nuevas en tarjetas (esquema 2.0), del 11-11 al 17-11-2026.
# Producidas por Claude bajo la delegación de Max del 20-10-2026. Fuentes abiertas y comprobadas el 04-11-2026.
# Cada ilustración muestra solo lo que dice el texto de su tarjeta.
# Salida: borradores/lote5/
import os, sys
HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "visuales"))
from almanaque_lib import card, src, lesson, write, validate_visuals
from svgkit import svg, BG, arrow_def, arrow, text, waves

HOY = "2026-11-04"
LOTE = []
VIS = {}

def box(x, y, w, h, cls="as-svg__warm", rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="as-svg__ink"/>'

def shape(d, cls):
    return f'<path d="{d}" class="{cls}"/><path d="{d}" class="as-svg__ink"/>'

def dots(pts, r=3, cls="as-svg__fill"):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>' for x, y in pts)

def star(x, y, r=7, cls="as-svg__sun"):
    k = r * 0.3
    d = f"M{x} {y - r} L{x + k} {y - k} L{x + r} {y} L{x + k} {y + k} L{x} {y + r} L{x - k} {y + k} L{x - r} {y} L{x - k} {y - k} Z"
    return f'<path d="{d}" class="{cls}"/><path d="{d}" class="as-svg__ink"/>'

def mountain(x0, x1, top_x, top_y, base=200, cls="as-svg__warm"):
    return shape(f"M{x0} {base} L{top_x} {top_y} L{x1} {base} Z", cls)

def dome(x, y, s=1.0):
    return shape(f"M{x - 16 * s} {y} A{16 * s} {16 * s} 0 0 1 {x + 16 * s} {y} Z", "as-svg__fill")

def disc(x, y, r, cls):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/><circle cx="{x}" cy="{y}" r="{r}" class="as-svg__ink"/>'

def line(x1, y1, x2, y2, extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="as-svg__ink" {extra}/>'

def spoon(x, y, cls):
    """Cuchara vertical; (x, y) = centro del cuenco."""
    return (f'<rect x="{x - 5}" y="{y + 18}" width="10" height="100" rx="5" class="{cls}"/><rect x="{x - 5}" y="{y + 18}" width="10" height="100" rx="5" class="as-svg__ink"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="20" ry="27" class="{cls}"/><ellipse cx="{x}" cy="{y}" rx="20" ry="27" class="as-svg__ink"/>')

def hand(x, y):
    """Palma simple, vista de costado, apoyada desde arriba."""
    return shape(f"M{x - 34} {y} C{x - 34} {y - 30} {x + 34} {y - 30} {x + 34} {y} Z", "as-svg__warm")

def person(x, y, cls="as-svg__warm"):
    return f'<circle cx="{x}" cy="{y}" r="11" class="{cls}"/><circle cx="{x}" cy="{y}" r="11" class="as-svg__ink"/>' + shape(f"M{x - 18} {y + 44} C{x - 18} {y + 14} {x + 18} {y + 14} {x + 18} {y + 44} Z", cls)

def basket(x, y, w=120, h=64, cls="as-svg__warm"):
    d = f"M{x} {y} L{x + w} {y} L{x + w - 14} {y + h} L{x + 14} {y + h} Z"
    return f'<path d="M{x + 24} {y} C{x + 24} {y - 40} {x + w - 24} {y - 40} {x + w - 24} {y}" class="as-svg__ink"/>' + shape(d, cls)

def earth(x, y, r=30, tilt=23):
    return (disc(x, y, r, "as-svg__cool") +
            f'<line x1="{x}" y1="{y - r - 12}" x2="{x}" y2="{y + r + 12}" class="as-svg__ink" stroke-dasharray="4 4" transform="rotate({tilt} {x} {y})"/>')

# =================================================================== 11-11 cerros-estrellas (astronomía)
L = "cerros-estrellas"; A = arrow_def(L)
VIS[L] = {
 "c1": svg("Un telescopio en la cima de un cerro bajo un cielo con estrellas",
   BG + mountain(40, 280, 160, 70) + dome(160, 72) + star(60, 40) + star(110, 26, 5) + star(232, 30) + star(280, 58, 5) +
   text(160, 186, "¿qué tiene este lugar?", 17)),
 "c2": svg("La luz de una estrella se desvía al cruzar el aire en movimiento; por eso titila y la imagen sale borrosa",
   BG + star(160, 26, 10) +
   '<path d="M160 40 C135 60 185 78 160 96 C135 114 185 130 160 150" class="as-svg__warmline"/>' +
   waves(14, 120, 74, 5, 26, "as-svg__coolline") + waves(204, 306, 74, 5, 26, "as-svg__coolline") +
   waves(14, 120, 112, 5, 26, "as-svg__coolline") + waves(204, 306, 112, 5, 26, "as-svg__coolline") +
   text(80, 56, "aire en movimiento", 15) +
   dots([(146, 170), (160, 170), (174, 170)], 4, "as-svg__muted") + text(160, 192, "la luz se desvía", 16)),
 "c4": svg("Un observatorio en lo alto queda por encima de gran parte de la atmósfera",
   BG + A + '<rect x="0" y="120" width="320" height="80" rx="18" class="as-svg__cool"/>' +
   mountain(70, 270, 170, 58) + dome(170, 60) +
   text(66, 38, "menos aire encima", 16, "start") + arrow(L, 112, 50, 150, 70) +
   text(48, 150, "mucha", 16) + text(48, 170, "atmósfera", 16) + text(170, 150, "cerro", 16)),
 "c5": svg("El vapor de agua absorbe parte de la luz infrarroja; en una zona seca esa luz llega mejor al telescopio",
   BG + A + box(16, 40, 136, 96, "as-svg__soft", 10) + box(168, 40, 136, 96, "as-svg__soft", 10) +
   arrow(L, 34, 66, 100, 66, 3) + dots([(70, 96), (84, 84), (112, 66), (112, 88), (126, 74), (98, 110), (126, 112)], 4, "as-svg__cool") +
   arrow(L, 186, 66, 286, 66, 3) +
   text(84, 160, "con vapor", 16) + text(84, 182, "parte se absorbe", 15) +
   text(236, 160, "aire seco", 16) + text(236, 182, "llega mejor", 15) + text(160, 28, "luz infrarroja", 16)),
 "c6": svg("Cerro Paranal en el desierto de Atacama, con 2.635 metros de altura",
   BG + mountain(60, 260, 160, 84, 168) + dome(160, 86) +
   '<line x1="20" y1="168" x2="300" y2="168" class="as-svg__ink"/>' +
   text(160, 40, "Cerro Paranal", 18) + text(160, 62, "2.635 metros", 16) + text(160, 190, "desierto de Atacama", 16)),
 "c8": svg("Desde Chile se ven el centro de la Vía Láctea y las dos Nubes de Magallanes",
   BG + '<path d="M0 150 C70 110 130 90 200 60 C240 44 280 30 320 26 L320 62 C280 70 240 84 200 96 C130 122 70 150 0 186 Z" class="as-svg__warm"/>' +
   dots([(60, 148), (110, 120), (150, 108), (206, 78), (250, 62), (284, 50), (180, 92)], 2, "as-svg__label") +
   '<ellipse cx="66" cy="50" rx="24" ry="13" class="as-svg__fill"/><ellipse cx="124" cy="38" rx="15" ry="9" class="as-svg__fill"/>' +
   text(14, 26, "Nubes de Magallanes", 15, "start") + text(196, 136, "centro de la", 15) + text(196, 156, "Vía Láctea", 15) + text(160, 190, "se ven desde Chile", 16)),
}
LOTE.append(lesson(L, "Astronomía", "astronomia",
  "¿Por qué algunos cerros son buenos para observar estrellas?", "Menos aire encima, menos humedad y un cielo oscuro.",
  [card("c1", "portada", titulo="¿Por qué algunos cerros son buenos para observar estrellas?", texto="Muchos de los grandes telescopios están en lo alto de un cerro. ¿Qué tiene de especial ese lugar?", fuentes=["brit-cerros"]),
   card("c2", "idea", titulo="El aire desvía la luz", texto="El aire de la atmósfera se mueve y desvía un poco la luz de las estrellas. Por eso titilan, y por eso las imágenes de los telescopios pueden salir borrosas.", fuentes=["nasa-titilar", "brit-cerros"]),
   card("c3", "pregunta", pregunta="¿Qué gana un telescopio en la cima de un cerro alto?", correctaId="a", opciones=[
     ("a", "Queda por encima de gran parte de la atmósfera", "¡Exacto! Hay menos aire que distorsione la luz."),
     ("b", "Recibe más calor del Sol", "No: la ventaja no tiene que ver con el calor, sino con tener menos atmósfera encima."),
     ("c", "Las estrellas se mueven más lento", "No: lo que cambia es el aire que cruza la luz, y arriba hay menos.")], fuentes=["brit-cerros"]),
   card("c4", "idea", titulo="Menos aire encima", texto="En lo alto, el observatorio queda por encima de gran parte de la atmósfera. Hay menos aire que distorsione la luz, y las imágenes salen más nítidas.", fuentes=["brit-cerros"]),
   card("c5", "idea", titulo="Mejor si el aire es seco", texto="El vapor de agua absorbe parte de la luz, sobre todo la infrarroja. Por eso ayuda que el cerro esté en una zona seca.", fuentes=["brit-cerros"]),
   card("c6", "revelar", titulo="Un cerro muy seco", texto="Cerro Paranal, en el desierto de Atacama, tiene 2.635 metros de altura y un gran observatorio. ¿Qué tan seco es ese lugar?",
        revelado="El Observatorio Europeo Austral lo describe como posiblemente la zona más seca de la Tierra: llueve menos de 10 milímetros al año.", fuentes=["eso-paranal"]),
   card("c7", "pregunta", pregunta="Según el Observatorio Europeo Austral, ¿qué ofrece el cielo del norte de Chile?", correctaId="b", opciones=[
     ("a", "Lluvias frecuentes que limpian el aire", "No: destaca lo contrario, un cielo despejado y muy seco."),
     ("b", "Cielo despejado y muy seco, con poca turbulencia y poca contaminación lumínica", "¡Así es! Por eso sus observatorios están en Chile."),
     ("c", "Estrellas que brillan más que en otras partes", "No: las estrellas son las mismas; lo que ayuda es el cielo del lugar.")], fuentes=["eso-chile"]),
   card("c8", "dato", texto="Desde el hemisferio norte cuesta ver el centro de la Vía Láctea y las Nubes de Magallanes. Desde Chile, en cambio, se pueden ver.", fuentes=["eso-chile"])],
  ("Cerros y estrellas", ["La atmósfera desvía la luz de las estrellas, y en lo alto hay menos aire que la distorsione.",
                          "El aire seco ayuda porque el vapor de agua absorbe parte de la luz.",
                          "El norte de Chile ofrece cielos despejados y muy secos, con poca contaminación lumínica."]),
  [src("brit-cerros", "Encyclopaedia Britannica", "Why are many large optical telescopes built on high mountains?", "https://www.britannica.com/science/Why-are-many-large-optical-telescopes-built-on-high-mountains", "Texto principal",
       ["Muchos telescopios ópticos grandes se construyen en montañas altas", "La turbulencia de la atmósfera distorsiona la luz: las estrellas centellean y las imágenes salen borrosas", "En altura, el observatorio queda sobre gran parte de la atmósfera", "Muchas de esas montañas están en zonas secas; el vapor de agua absorbe ciertas longitudes de onda, sobre todo en el infrarrojo"],
       ["c1", "c2", "c3", "c4", "c5"], HOY),
   src("nasa-titilar", "NASA, StarChild", "Why do stars twinkle?", "https://starchild.gsfc.nasa.gov/docs/StarChild/questions/question26.html", "Respuesta a la pregunta",
       ["La luz de las estrellas atraviesa la atmósfera y el movimiento del aire la desvía levemente, y por eso parecen titilar"],
       ["c2"], HOY),
   src("eso-paranal", "European Southern Observatory", "Paranal: Site Information", "https://www.eso.org/sci/facilities/paranal/astroclimate/site.html", "Descripción del sitio",
       ["Cerro Paranal tiene 2.635 metros sobre el nivel del mar", "Se considera posiblemente la zona más seca de la Tierra", "La lluvia anual es inferior a 10 milímetros"],
       ["c6"], HOY),
   src("eso-chile", "European Southern Observatory", "Why are ESO's observatories in Chile?", "https://supernova.eso.org/exhibition/0606/?lang=en", "Texto principal",
       ["El cielo del norte de Chile es despejado y muy seco, con muy poca turbulencia y muy poca contaminación lumínica", "Desde el hemisferio norte son difíciles de ver el centro de la Vía Láctea y las Nubes de Magallanes; desde Chile son visibles"],
       ["c7", "c8"], HOY)]))

# =================================================================== 12-11 inflacion-sube (economía)
L = "inflacion-sube"; A = arrow_def(L)
def tag(x, y, s, cls="as-svg__warm"):
    return box(x, y, 66, 34, cls, 6) + text(x + 33, y + 23, s, 16)
VIS[L] = {
 "c1": svg("Un titular de noticias dice que subió la inflación, con un signo de pregunta",
   BG + box(50, 36, 220, 118, "as-svg__warm", 8) + box(64, 50, 192, 40, "as-svg__soft", 4) + text(160, 76, "subió la inflación", 17) +
   line(70, 108, 250, 108) + line(70, 124, 250, 124) + line(70, 140, 190, 140) + text(160, 182, "¿todo más caro?", 17)),
 "c2": svg("Una canasta con productos: el INE mide con el IPC el aumento general de los precios",
   BG + basket(100, 84) + disc(132, 74, 11, "as-svg__fill") + box(150, 54, 18, 30, "as-svg__cool", 3) + disc(190, 72, 13, "as-svg__fill") +
   text(160, 124, "IPC", 20) + text(160, 28, "precios en general", 17) + text(160, 182, "lo mide el INE", 16)),
 "c4": svg("Barras de gasto de varios hogares y una línea que marca el promedio: una familia puede quedar lejos de esa línea",
   BG + A + "".join(box(52 + i * 58, 150 - h, 42, h, "as-svg__warm", 3) for i, h in enumerate((58, 92, 74, 112))) +
   '<line x1="30" y1="66" x2="290" y2="66" class="as-svg__ink" stroke-dasharray="6 5"/>' +
   text(160, 26, "gasto promedio de los hogares", 16) + arrow(L, 160, 34, 160, 62) + text(160, 182, "tu familia puede ser distinta", 16)),
 "c5": svg("El mismo sueldo compra menos cosas cuando los precios suben y los ingresos no",
   BG + A + box(22, 58, 96, 62, "as-svg__warm", 8) + text(70, 96, "sueldo", 17) + arrow(L, 126, 88, 166, 88, 3) +
   "".join(box(182 + i * 44, 60, 36, 56, "as-svg__fill" if i < 2 else "as-svg__soft", 4) for i in range(3)) +
   line(274, 66, 304, 110) + line(304, 66, 274, 110) +
   text(160, 34, "el mismo sueldo", 17) + text(235, 150, "alcanza para menos", 16) + text(70, 150, "no sube", 16)),
 "c7": svg("Una diana con un signo de pregunta: la meta de inflación del Banco Central",
   BG + disc(160, 96, 62, "as-svg__warm") + disc(160, 96, 40, "as-svg__soft") + disc(160, 96, 18, "as-svg__fill") +
   text(160, 103, "?", 20) + text(160, 186, "la meta del Banco Central", 16)),
 "c8": svg("El IPC se publica dentro de los primeros ocho días del mes siguiente y habla del mes anterior",
   BG + A + box(30, 54, 100, 92, "as-svg__soft", 8) + box(30, 54, 100, 24, "as-svg__fill", 8) + text(80, 116, "IPC", 20) +
   arrow(L, 138, 100, 182, 100, 3) +
   box(190, 54, 100, 92, "as-svg__warm", 8) + box(190, 54, 100, 24, "as-svg__fill", 8) + text(240, 112, "días 1 al 8", 16) +
   text(80, 172, "mes anterior", 16) + text(240, 172, "se publica", 16)),
}
LOTE.append(lesson(L, "Economía", "economia",
  "¿Qué significa que suba la inflación?", "Por qué no quiere decir que todo suba igual.",
  [card("c1", "portada", titulo="¿Qué significa que suba la inflación?", texto="En las noticias dicen que subió la inflación. ¿Significa que todo está más caro? No exactamente.", fuentes=["bc-disminucion"]),
   card("c2", "idea", titulo="Los precios en general", texto="La inflación es el aumento generalizado de los precios en una economía. En Chile, el INE la mide con el IPC, una canasta de bienes y servicios que refleja el gasto típico de las familias.", fuentes=["bc-disminucion", "ine-ipc"]),
   card("c3", "pregunta", pregunta="Si el IPC subió 1 % en un mes, ¿qué significa?", correctaId="b", opciones=[
     ("a", "Que todos los precios subieron 1 %", "No: 1 % es el resultado de la canasta completa. Algunos precios suben, otros se mantienen y otros bajan."),
     ("b", "Que la canasta, en conjunto, subió 1 %", "¡Correcto! Dentro de ella, algunos precios suben, otros se mantienen y otros bajan."),
     ("c", "Que los sueldos subieron 1 %", "No: el IPC mide precios de bienes y servicios, no sueldos.")], fuentes=["bc-disminucion"]),
   card("c4", "idea", titulo="Un promedio, no tu cuenta", texto="La canasta se basa en el gasto promedio de los hogares, no en el de una familia específica. Por eso, lo que notas en tus compras puede ser distinto del IPC.", fuentes=["ine-preguntas"]),
   card("c5", "idea", titulo="El sueldo rinde menos", texto="Si los precios suben y los ingresos no, el dinero rinde menos: con el mismo sueldo se compra menos.", fuentes=["bc-bolsillo"]),
   card("c6", "pregunta", pregunta="Si la inflación baja hasta niveles normales, ¿qué pasa con los precios?", correctaId="a", opciones=[
     ("a", "En general siguen subiendo, pero a menor ritmo", "¡Así es! Bajar la inflación no es lo mismo que bajar los precios."),
     ("b", "Vuelven a lo que costaban antes", "No: los precios siguen subiendo, solo que más lento."),
     ("c", "Bajan todos al mismo tiempo", "No: una baja generalizada de precios tiene otro nombre: deflación.")], fuentes=["bc-disminucion"]),
   card("c7", "revelar", titulo="La meta", texto="El Banco Central de Chile tiene una meta de inflación. ¿Cuál es?",
        revelado="Una inflación de 3 % al año, en un horizonte de dos años. Su principal herramienta para cumplirla es la tasa de política monetaria, una tasa de interés.", fuentes=["bc-cespedes"]),
   card("c8", "dato", texto="El INE publica el IPC dentro de los primeros ocho días del mes siguiente. Por eso, la cifra que escuchas siempre habla del mes anterior.", fuentes=["ine-preguntas"])],
  ("La inflación", ["Es el aumento generalizado de los precios; en Chile se mide con el IPC del INE.",
                    "Que suba 1 % no significa que todo suba 1 %: es el resultado de una canasta completa.",
                    "Si la inflación baja, los precios en general siguen subiendo, pero más lento."]),
  [src("bc-disminucion", "Banco Central de Chile", "Entendiendo la disminución de la inflación: Qué es… y qué no", "https://www.bcentral.cl/en/content/-/detalle/entendiendo-la-disminucion-de-la-inflacion-que-es-y-que-no", "Texto principal",
       ["La inflación es el aumento generalizado de los precios en una economía", "El INE la mide con el IPC, una canasta que refleja el gasto de una familia típica", "Si sube 1 %, la canasta subió 1 % en su conjunto: no significa que todos los precios mostraron ese incremento", "Una baja de la inflación significa que los precios aumentan a menor ritmo", "Una baja generalizada de los precios se llama deflación"],
       ["c1", "c2", "c3", "c6"], HOY),
   src("ine-ipc", "Instituto Nacional de Estadísticas", "Índice de Precios al Consumidor", "https://www.ine.gob.cl/estadisticas-por-tema/precios-e-inflacion/indice-de-precios-al-consumidor", "Descripción del indicador",
       ["El IPC mide la variación mensual de los precios de una canasta de bienes y servicios de consumo de los hogares"],
       ["c2"], HOY),
   src("ine-preguntas", "Instituto Nacional de Estadísticas", "Preguntas frecuentes del IPC, base anual 2023=100", "https://www.ine.gob.cl/docs/default-source/%C3%ADndice-de-precios-al-consumidor/metodologias/base-anual-2023-100/2---preguntas-frecuentes-ipc-2023.pdf", "Preguntas sobre la canasta y la publicación",
       ["La canasta se basa en el gasto promedio de los hogares, no en el de una persona o familia específica", "Los resultados se publican en los primeros ocho días del mes siguiente"],
       ["c4", "c8"], HOY),
   src("bc-bolsillo", "Banco Central de Chile", "¿Sabes cómo afecta la inflación el bolsillo de las personas?", "https://www.bcentral.cl/documents/33528/133214/rcc_24082022.pdf/3c82613d-6c7a-6552-cc2d-ed9e69051ea6?t=1661364774053", "Texto principal",
       ["Si los precios suben y los ingresos no, el dinero rinde menos y con el mismo sueldo se compra menos"],
       ["c5"], HOY),
   src("bc-cespedes", "Banco Central de Chile", "El Banco Central y la inflación (presentación en Duoc UC, mayo de 2026)", "https://www.bcentral.cl/documents/33528/8073461/El+Banco+Central+y+la+Inflaci%C3%B3n+(Duoc+UC)+-+Luis+Felipe+C%C3%A9spedes,+Consejero.pdf/f1de7438-8b0c-1ac7-0ac5-64c70fe017a4?t=1778077574539", "Diapositivas sobre la meta y la tasa de política monetaria",
       ["Meta permanente de 3 % en un horizonte de 2 años", "La tasa de política monetaria es una tasa de interés y la principal herramienta para cumplir la meta"],
       ["c7"], HOY)]))

# =================================================================== 13-11 cuchara-fria (física)
L = "cuchara-fria"; A = arrow_def(L)
VIS[L] = {
 "c1": svg("Una cuchara de metal y una de madera sobre la misma mesa",
   BG + spoon(100, 60, "as-svg__cool") + spoon(220, 60, "as-svg__warm") + line(30, 182, 290, 182) +
   text(160, 36, "¿más fría?", 16) + text(50, 112, "metal", 16) + text(270, 112, "madera", 16)),
 "c3": svg("Un termómetro marca lo mismo en la cuchara de metal y en la de madera",
   BG + spoon(70, 58, "as-svg__cool") + spoon(250, 58, "as-svg__warm") +
   box(106, 62, 108, 56, "as-svg__soft", 8) + text(160, 86, "misma", 17) + text(160, 106, "temperatura", 15) +
   text(160, 150, "el termómetro", 16) + text(160, 170, "no ve diferencia", 16)),
 "c4": svg("El calor sale de la mano tibia hacia la cuchara y la piel se enfría",
   BG + A + hand(160, 92) + box(90, 112, 140, 22, "as-svg__cool", 8) +
   arrow(L, 130, 76, 130, 106, 3) + arrow(L, 160, 76, 160, 106, 3) + arrow(L, 190, 76, 190, 106, 3) +
   text(160, 34, "mano más tibia", 17) + text(160, 164, "el calor pasa a la cuchara", 16) + text(160, 186, "y la piel se enfría", 16)),
 "c5": svg("En el metal el calor se va rápido hacia adentro y la superficie sigue fría",
   BG + A + box(30, 70, 260, 50, "as-svg__soft", 8) + hand(90, 70) + arrow(L, 90, 86, 90, 108, 3) +
   arrow(L, 112, 104, 180, 104, 3) + arrow(L, 190, 104, 262, 104, 3) +
   text(160, 34, "el calor se va rápido", 17) + text(160, 146, "hacia adentro del metal", 16) + text(160, 170, "la superficie sigue fría", 16)),
 "c7": svg("Dos barras muy distintas comparan cuánto conducen el calor el acero inoxidable y la madera",
   BG + box(30, 66, 256, 30, "as-svg__fill", 4) + box(30, 124, 3, 30, "as-svg__warm", 1) +
   text(30, 54, "acero inoxidable", 16, "start") + text(30, 116, "madera", 16, "start") + text(70, 145, "¿cuánta diferencia?", 16, "start") +
   text(160, 186, "qué tan bien conducen el calor", 15)),
 "c8": svg("Un pie descalzo pasa de una alfombra a un piso de baldosas; ambos a la misma temperatura",
   BG + box(20, 118, 136, 50, "as-svg__warm", 4) +
   "".join(box(164 + i * 46, 118, 42, 50, "as-svg__cool", 2) for i in range(3)) +
   shape("M210 112 C206 88 214 70 224 70 C234 70 232 90 240 100 C250 106 262 108 262 112 Z", "as-svg__warm") +
   text(88, 192, "alfombra", 16) + text(232, 192, "baldosas", 16) + text(160, 30, "misma temperatura", 16) + text(232, 56, "se sienten más frías", 15)),
}
LOTE.append(lesson(L, "Física cotidiana", "fisica",
  "¿Por qué una cuchara de metal se siente más fría que una de madera?", "Tu mano no siempre es un buen termómetro.",
  [card("c1", "portada", titulo="¿Por qué una cuchara de metal se siente más fría que una de madera?", texto="Deja una cuchara de metal y otra de madera sobre la mesa. Al tocarlas, la de metal se siente más fría. ¿Lo está de verdad?", fuentes=["expl-metal"]),
   card("c2", "pregunta", pregunta="Las dos cucharas llevan una hora en la misma mesa. ¿Cuál está más fría?", correctaId="c", opciones=[
     ("a", "La de metal", "Se siente más fría, pero un termómetro mostraría que no lo está."),
     ("b", "La de madera", "No: un termómetro no mostraría diferencia entre ambas."),
     ("c", "Están a la misma temperatura", "¡Exacto! Las dos quedan a temperatura ambiente, aunque no se sientan igual.")], fuentes=["expl-metal", "illinois-fisica"]),
   card("c3", "idea", titulo="La misma temperatura", texto="Si dejas materiales cerca de una hora en un mismo lugar, llegan a temperatura ambiente. Un termómetro infrarrojo no muestra diferencia, aunque el tacto diga lo contrario.", fuentes=["expl-metal"]),
   card("c4", "idea", titulo="Lo que sientes es tu piel", texto="La temperatura ambiente es menor que la de tu mano, así que el objeto le quita calor a la piel. Si la piel se enfría, sientes que el objeto está frío.", fuentes=["expl-metal"]),
   card("c5", "idea", titulo="El metal se lleva el calor", texto="El metal conduce bien el calor: el de tu mano se va rápido hacia su interior. Por eso su superficie sigue fría, y tú también la sientes fría.", fuentes=["expl-metal", "illinois-fisica"]),
   card("c6", "pregunta", pregunta="¿Por qué la madera se siente menos fría que el metal?", correctaId="a", opciones=[
     ("a", "Porque frena el paso del calor", "¡Así es! La madera es un aislante: el calor de la mano pasa más lento."),
     ("b", "Porque está a más temperatura", "No: ambas cucharas están a temperatura ambiente."),
     ("c", "Porque produce su propio calor", "No: la diferencia está en la rapidez con que deja pasar el calor.")], fuentes=["brit-aislantes", "illinois-fisica"]),
   card("c7", "revelar", titulo="¿Cuánta diferencia hay?", texto="Hay tablas que indican qué tan bien conduce el calor cada material. ¿Cuánto mejor lo conduce el acero inoxidable que la madera?",
        revelado="Entre 87,5 y 175 veces mejor. En una tabla de física, el acero inoxidable marca 14, y la madera, entre 0,08 y 0,16.", fuentes=["openstax-conduccion"]),
   card("c8", "dato", texto="Pasa lo mismo con los pies: una alfombra y un piso de baldosas pueden estar a la misma temperatura, pero las baldosas se sienten más frías. En ellas, la piel pierde más calor.", fuentes=["openstax-conduccion"])],
  ("La cuchara fría", ["La cuchara de metal y la de madera están a la misma temperatura si llevan rato en el mismo lugar.",
                       "Lo que sientes es cómo se enfría tu piel, no la temperatura del objeto.",
                       "El metal se lleva rápido el calor de la mano, y la madera frena su paso."]),
  [src("expl-metal", "Exploratorium", "Cold Metal", "https://www.exploratorium.edu/snacks/cold-metal", "Secciones de preparación y explicación",
       ["Tras cerca de una hora los materiales alcanzan la temperatura ambiente", "Un termómetro infrarrojo muestra que no hay diferencia entre ellos", "La temperatura ambiente es menor que la de la mano", "El metal conduce bien el calor: el de la mano pasa rápido a su interior y la superficie sigue fría", "Si la piel se enfría, el objeto se percibe como frío", "La mano no siempre es un buen termómetro"],
       ["c1", "c2", "c3", "c4", "c5"], HOY),
   src("illinois-fisica", "University of Illinois, Department of Physics (Ask the Van)", "Different Materials get Different Temperatures?", "https://van.physics.illinois.edu/ask/listing/29929", "Respuesta del 23-05-2015",
       ["Dos materiales en contacto, sin un flujo importante de energía desde otros objetos, terminan a la misma temperatura", "No se sienten igual: el metal tiene mayor conductividad térmica y el calor fluye más rápido entre el dedo y el metal"],
       ["c2", "c5", "c6"], HOY),
   src("brit-aislantes", "Britannica Kids", "Insulators and conductors", "https://kids.britannica.com/kids/article/insulators-and-conductors/476281", "Texto principal",
       ["La madera es un buen aislante térmico: frena el paso del calor"],
       ["c6"], HOY),
   src("openstax-conduccion", "OpenStax, Rice University", "College Physics 2e, 14.5 Conduction", "https://openstax.org/books/college-physics-2e/pages/14-5-conduction", "Tabla de conductividades y ejemplo de la alfombra",
       ["Conductividad térmica cerca de 0 °C: acero inoxidable 14, madera 0,08 a 0,16 J/(s·m·°C)", "14 ÷ 0,16 = 87,5 y 14 ÷ 0,08 = 175", "Alfombra y baldosas a la misma temperatura: los pies sienten más frío en las baldosas porque la piel pierde más calor"],
       ["c7", "c8"], HOY)]))

# =================================================================== 14-11 noticia-fuente (sociedad)
L = "noticia-fuente"; A = arrow_def(L)
VIS[L] = {
 "c1": svg("Un diario con una noticia y un signo de pregunta sobre quién lo dice",
   BG + box(70, 30, 180, 130, "as-svg__warm", 8) + box(84, 44, 152, 26, "as-svg__soft", 4) + text(160, 63, "noticia", 17) +
   line(86, 90, 234, 90) + line(86, 108, 234, 108) + line(86, 126, 180, 126) + text(160, 186, "¿quién lo dice?", 17)),
 "c2": svg("Una persona le entrega información a un periodista; puede buscarlo ella o él puede buscarla",
   BG + A + person(66, 62, "as-svg__warm") + person(254, 62, "as-svg__fill") +
   arrow(L, 100, 72, 216, 72, 3) + arrow(L, 216, 104, 100, 104, 3) +
   text(160, 60, "información", 16) + text(160, 124, "testimonio", 16) +
   text(66, 134, "fuente", 16) + text(254, 134, "periodista", 16) + text(160, 180, "cualquiera puede buscar al otro", 15)),
 "c4": svg("Fuente primaria: alguien que lo vio directamente. Fuente secundaria: alguien que lo sabe por un intermediario",
   BG + A + star(160, 30, 14, "as-svg__sun") + person(60, 60) + person(262, 60, "as-svg__soft") + person(160, 92, "as-svg__soft") +
   arrow(L, 142, 34, 84, 50, 3) + arrow(L, 160, 48, 160, 76, 3) + arrow(L, 186, 112, 236, 92, 3) +
   text(60, 132, "primaria", 16) + text(64, 152, "de primera mano", 15) + text(262, 132, "secundaria", 16) + text(160, 182, "intermediario", 15)),
 "c5": svg("Una credencial con nombre, condición y por qué importa esa persona en el tema",
   BG + box(70, 40, 180, 120, "as-svg__warm", 10) + person(108, 72, "as-svg__soft") +
   text(146, 76, "nombre", 16, "start") + text(146, 102, "condición", 16, "start") + text(160, 142, "por qué importa", 16) +
   text(160, 186, "el lector puede comprobarlo", 16)),
 "c6": svg("Una persona sin rostro visible junto a la frase: una fuente que pidió reserva",
   BG + shape("M120 150 C120 96 200 96 200 150 Z", "as-svg__ink") + '<circle cx="160" cy="78" r="26" class="as-svg__muted"/>' +
   text(160, 87, "?", 24) + box(50, 158, 220, 30, "as-svg__warm", 6) + text(160, 179, "una fuente que pidió reserva", 15)),
 "c8": svg("Un candado sobre una tarjeta de fuente: en Chile, la Ley de Prensa de 2001 protege la reserva de la fuente",
   BG + box(120, 84, 80, 62, "as-svg__warm", 8) + '<path d="M138 84 L138 66 C138 38 182 38 182 66 L182 84" class="as-svg__ink" stroke-width="5"/>' +
   text(160, 122, "fuente", 16) + text(160, 170, "Ley de Prensa, 2001", 16) + text(160, 192, "reserva sobre la fuente", 15)),
}
LOTE.append(lesson(L, "Sociedad y medios", "sociedad",
  "¿Qué significa que una noticia tenga una fuente?", "Saber quién lo dice ayuda a decidir cuánto creer.",
  [card("c1", "portada", titulo="¿Qué significa que una noticia tenga una fuente?", texto="Una noticia sin fuentes tiene mucha menos credibilidad. Pero ¿qué es exactamente una fuente?", fuentes=["sp-fuentes"]),
   card("c2", "idea", titulo="Alguien que informa", texto="Una fuente es una persona que transmite información. Puede contactar al periodista para contarle lo que sabe, o el periodista puede buscarla para pedirle su testimonio.", fuentes=["sp-fuentes"]),
   card("c3", "pregunta", pregunta="¿Cuál de estas personas es una fuente primaria de un choque en la calle?", correctaId="a", opciones=[
     ("a", "Alguien que lo vio directamente", "¡Exacto! Un testigo directo da un relato de primera mano."),
     ("b", "El familiar de un testigo, que escuchó lo que este contó", "No: un familiar lo sabe por un intermediario. Es una fuente secundaria."),
     ("c", "Un vocero que recibió un informe", "No: un vocero obtiene la información por intermediarios. Es una fuente secundaria.")], fuentes=["sp-fuentes"]),
   card("c4", "idea", titulo="Directa o por otra persona", texto="Una fuente primaria da un relato de primera mano, como un testigo directo. Una fuente secundaria lo sabe por un intermediario, como un vocero o un familiar.", fuentes=["sp-fuentes"]),
   card("c5", "idea", titulo="Con nombre y razón", texto="Dar el nombre de la fuente y su condición permite al lector comprobar quién es. También hay que explicar por qué esa persona importa en el tema.", fuentes=["sp-fuentes"]),
   card("c6", "revelar", titulo="¿Y si no da su nombre?", texto="A veces una noticia cita a una fuente que pidió reserva. ¿Cuándo se acepta eso?",
        revelado="Cuando hablar pone en riesgo su seguridad, su empleo o su reputación. Aun así, el periodista debe explicar su papel y justificar por qué no la nombra. Como lector, puedes buscar otras pruebas que lo confirmen.", fuentes=["sp-fuentes", "sb-anonimas"]),
   card("c7", "pregunta", pregunta="Un testigo directo le cuenta algo a un periodista. ¿Qué debería hacer el periodista?", correctaId="b", opciones=[
     ("a", "Publicarlo tal cual, porque estuvo ahí", "No: las fuentes primarias no siempre dicen la verdad, aunque actúen de buena fe."),
     ("b", "Contrastarlo con otras fuentes", "¡Así es! Debe validar la información y detectar contradicciones."),
     ("c", "Descartarlo, porque un testigo nunca sirve", "No: un testigo es valioso, pero lo que dice se contrasta.")], fuentes=["sp-fuentes"]),
   card("c8", "dato", texto="En Chile, la Ley de Prensa de 2001 da a los periodistas derecho a mantener reserva sobre su fuente. No se les puede obligar a revelarla, ni siquiera ante un tribunal.", fuentes=["uchile-reserva"])],
  ("Las fuentes de una noticia", ["Una fuente es una persona que transmite información; puede ser directa o saberlo por un intermediario.",
                                  "Nombrar la fuente y explicar por qué importa permite comprobar quién habla.",
                                  "Lo que dice una fuente se contrasta, y la reserva de su nombre debe justificarse."]),
  [src("sp-fuentes", "Agence Science-Presse (Québec)", "Journalistic sources (ficha 3)", "https://www.sciencepresse.qc.ca/sites/default/files/inline-files/Journalistic%20sources_EN.pdf", "Ficha completa",
       ["Una noticia sin fuentes tiene mucha menos credibilidad", "Una fuente es una persona que transmite información; puede contactar al periodista o este buscarla", "Primarias: relato de primera mano, como testigos directos; secundarias: por intermediarios, como familiares o portavoces", "Identificar a la fuente con nombre y condición permite confirmar quién es; se debe explicar por qué es relevante", "Las fuentes anónimas se usan si hablar pone en riesgo la seguridad, el empleo o la reputación; el periodista debe explicar su papel y justificar la reserva", "Las fuentes primarias no siempre dicen la verdad, aunque actúen de buena fe; hay que contrastar"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c7"], HOY),
   src("sb-anonimas", "Stony Brook Center for News Literacy", "Says Who? Evaluating Sources, Part 3: Evaluating Anonymous Sources", "https://digitalresource.center/node/18156", "Preguntas guía",
       ["Ante una fuente anónima conviene preguntarse por qué pide anonimato y buscar otras pruebas que confirmen lo que dice"],
       ["c6"], HOY),
   src("uchile-reserva", "Universidad de Chile", "Académicas y académicos en defensa de la confidencialidad de las fuentes", "https://uchile.cl/noticias/234478/academicos-fcei-en-defensa-de-la-confidencialidad-de-las-fuentes", "Texto principal, que cita el artículo 7 de la Ley de Prensa",
       ["La Ley de Prensa, promulgada en 2001, dispone en su artículo 7 que los periodistas tienen derecho a mantener reserva sobre su fuente informativa y no pueden ser obligados a revelarla, ni aun judicialmente"],
       ["c8"], HOY)]))

# =================================================================== 15-11 levadura-pan (cocina)
L = "levadura-pan"; A = arrow_def(L)
def loaf(x, y, w, h, cls="as-svg__warm"):
    return shape(f"M{x} {y + h} L{x + w} {y + h} C{x + w + 8} {y + h * 0.3} {x + w - 16} {y} {x + w / 2} {y} C{x + 16} {y} {x - 8} {y + h * 0.3} {x} {y + h} Z", cls)
def cell(x, y, r=26, bud=True):
    return (disc(x, y, r, "as-svg__fill") + (disc(x + r + 8, y - r * 0.4, r * 0.4, "as-svg__fill") if bud else ""))
VIS[L] = {
 "c1": svg("Una masa de pan pequeña que crece hasta ser una masa más grande mientras reposa",
   BG + A + loaf(36, 112, 86, 44) + arrow(L, 132, 128, 170, 128, 3) + loaf(184, 72, 112, 84) +
   line(20, 158, 300, 158) + text(160, 36, "la masa crece mientras reposa", 16) + text(160, 186, "¿qué hay adentro?", 16)),
 "c2": svg("Una célula de levadura: un hongo de una sola célula, muy distinto de un champiñón con sombrero",
   BG + cell(84, 86, 34, False) + text(84, 148, "una sola célula", 16) +
   shape("M206 88 C206 40 286 40 286 88 Z", "as-svg__warm") + box(234, 88, 24, 42, "as-svg__soft", 4) +
   line(204, 44, 288, 132) + text(246, 150, "no es de sombrero", 16) + text(84, 180, "levadura", 16)),
 "c4": svg("La levadura come azúcar y produce dióxido de carbono y alcohol; el dióxido de carbono forma burbujas en la masa",
   BG + A + box(16, 74, 74, 40, "as-svg__warm", 6) + text(53, 100, "azúcar", 16) + arrow(L, 96, 94, 124, 94, 3) +
   cell(156, 94, 24, False) + arrow(L, 186, 84, 214, 62, 3) + arrow(L, 186, 104, 214, 126, 3) +
   text(262, 50, "dióxido de", 15) + text(262, 68, "carbono", 15) + text(262, 136, "alcohol", 15) +
   text(160, 28, "fermentación", 16) +
   '<circle cx="120" cy="170" r="10" class="as-svg__ink"/><circle cx="150" cy="176" r="7" class="as-svg__ink"/><circle cx="176" cy="168" r="11" class="as-svg__ink"/><circle cx="202" cy="176" r="6" class="as-svg__ink"/>' +
   text(66, 178, "burbujas", 15)),
 "c5": svg("Una red elástica de gluten atrapa las burbujas de gas dentro de la masa",
   BG + box(30, 44, 260, 110, "as-svg__warm", 22) +
   "".join(f'<path d="M{44 + i * 46} 50 C{70 + i * 46} 90 {30 + i * 46} 110 {60 + i * 46} 148" class="as-svg__ink"/>' for i in range(6)) +
   "".join(f'<path d="M36 {64 + i * 24} C110 {52 + i * 24} 200 {80 + i * 24} 284 {64 + i * 24}" class="as-svg__ink"/>' for i in range(4)) +
   dots([(88, 76), (150, 110), (214, 84), (240, 126), (110, 128)], 10, "as-svg__soft") +
   text(160, 28, "red de gluten", 17) + text(160, 182, "atrapa el gas", 17)),
 "c6": svg("Un pan entra al horno: ¿qué pasa con el alcohol que produjo la levadura?",
   BG + box(70, 40, 180, 120, "as-svg__warm", 10) + box(86, 56, 148, 88, "as-svg__soft", 6) + loaf(118, 88, 84, 50, "as-svg__fill") +
   line(92, 146, 228, 146) + text(160, 28, "en el horno", 16) + text(160, 184, "¿y el alcohol?", 17)),
 "c8": svg("Pan, cerveza y vino: se hacen con esta levadura desde hace miles de años",
   BG + loaf(28, 96, 76, 50) + box(130, 72, 56, 74, "as-svg__warm", 6) + '<path d="M186 90 C204 90 204 126 186 126" class="as-svg__ink"/>' +
   shape("M238 70 L280 70 C280 100 268 110 259 110 C250 110 238 100 238 70 Z", "as-svg__fill") + line(259, 110, 259, 140) + line(242, 144, 276, 144) +
   text(66, 170, "pan", 16) + text(158, 170, "cerveza", 16) + text(259, 170, "vino", 16) + text(160, 34, "desde hace miles de años", 16)),
}
LOTE.append(lesson(L, "Ciencia de la cocina", "cocina",
  "¿Qué hace la levadura dentro del pan?", "Un ser vivo diminuto llena la masa de burbujas.",
  [card("c1", "portada", titulo="¿Qué hace la levadura dentro del pan?", texto="Una masa de pan crece mientras reposa, y su textura queda más ligera. El trabajo lo hace la levadura, un ser vivo.", fuentes=["brit-levadura", "iowa-pan"]),
   card("c2", "idea", titulo="Un hongo de una sola célula", texto="La levadura de panadería es un hongo de una sola célula, no un hongo de sombrero como el champiñón.", fuentes=["buffalo-levadura"]),
   card("c3", "pregunta", pregunta="¿Qué gas de la levadura hace subir la masa?", correctaId="b", opciones=[
     ("a", "Oxígeno", "No: el gas que libera la levadura y forma las burbujas es el dióxido de carbono."),
     ("b", "Dióxido de carbono", "¡Correcto! Forma burbujas que expanden la masa."),
     ("c", "Helio", "No: la levadura libera dióxido de carbono.")], fuentes=["buffalo-levadura", "brit-levadura"]),
   card("c4", "idea", titulo="Come azúcar y suelta gas", texto="La levadura se alimenta de azúcar. Al fermentar, produce dióxido de carbono y alcohol, y el dióxido de carbono forma burbujas que expanden la masa.", fuentes=["brit-levadura", "buffalo-levadura"]),
   card("c5", "idea", titulo="Una red que atrapa el gas", texto="Al amasar se estiran las proteínas del gluten, que forman una red elástica. Esa red atrapa el gas dentro de la masa.", fuentes=["wsu-horno", "iowa-pan"]),
   card("c6", "revelar", titulo="¿Y en el horno?", texto="La levadura también produjo alcohol. ¿Qué pasa con él en el horno, y con la levadura?",
        revelado="El calor mata la levadura y evapora el alcohol.", fuentes=["ucsb-levadura"]),
   card("c7", "pregunta", pregunta="¿Por qué una receta de pan pide líquido tibio y no muy caliente?", correctaId="c", opciones=[
     ("a", "Para que no se queme la harina", "No: la razón es que la levadura es un ser vivo."),
     ("b", "Para que el gluten se derrita", "No: el cuidado es con la levadura, que muere con demasiado calor."),
     ("c", "Porque el calor excesivo mata la levadura", "¡Así es! Y con frío trabaja lento.")], fuentes=["iowa-pan"]),
   card("c8", "dato", texto="Esta levadura se usa desde hace miles de años para hacer pan, cerveza y vino. Es uno de los microorganismos domesticados más antiguos.", fuentes=["brit-levadura"])],
  ("La levadura", ["Es un hongo de una sola célula que se alimenta de azúcar.",
                   "Al fermentar produce dióxido de carbono, y las burbujas hacen crecer la masa.",
                   "La red de gluten atrapa el gas; en el horno, el calor mata la levadura y evapora el alcohol."]),
  [src("brit-levadura", "Encyclopaedia Britannica", "Baker's yeast", "https://www.britannica.com/science/bakers-yeast", "Texto principal",
       ["La levadura de panadería es un hongo unicelular que hace subir los productos horneados", "Convierte azúcares en dióxido de carbono y alcohol; el dióxido de carbono expande la masa y da una textura más ligera", "Se usa desde hace miles de años en panadería, cerveza y vino; es uno de los microorganismos domesticados más antiguos"],
       ["c1", "c3", "c4", "c8"], HOY),
   src("buffalo-levadura", "University at Buffalo", "Meet baker's yeast, the budding, single-celled fungus that fluffs your bread", "https://www.buffalo.edu/ubnow/stories/2020/07/yeast.html", "Texto principal",
       ["Es un hongo unicelular, no un hongo con sombrero como los champiñones", "Se alimenta de azúcar y libera dióxido de carbono, que forma burbujas que expanden la masa"],
       ["c2", "c3", "c4"], HOY),
   src("wsu-horno", "Washington State University, Ask Dr. Universe", "Why does bread expand in the oven?", "https://askdruniverse.wsu.edu/2026/04/30/bread-expand-oven/", "Texto principal",
       ["Al amasar se estiran las proteínas del gluten, que forman una red que atrapa los gases"],
       ["c5"], HOY),
   src("iowa-pan", "Iowa State University Extension", "Yeast Bread Baking: A Kitchen Science Drama", "https://blogs.extension.iastate.edu/answerline/2021/01/12/yeast-bread-baking-a-kitchen-science-drama/", "Texto principal",
       ["La levadura es un organismo vivo que consume azúcar y libera dióxido de carbono", "Amasar desarrolla el gluten, una red elástica que atrapa el gas y hace subir la masa", "La levadura trabaja lento con frío y muere con temperaturas demasiado altas"],
       ["c1", "c5", "c7"], HOY),
   src("ucsb-levadura", "University of California, Santa Barbara, ScienceLine", "Respuesta sobre la levadura y el pan", "https://scienceline.ucsb.edu/getkey.php?key=692", "Respuesta a la pregunta",
       ["El calor del horno mata la levadura y evapora el alcohol"],
       ["c6"], HOY)]))

# =================================================================== 16-11 estaciones-ano (astronomía)
L = "estaciones-ano"; A = arrow_def(L)
sol = lambda x, y, r=26: disc(x, y, r, "as-svg__sun")
VIS[L] = {
 "c1": svg("El Sol y la Tierra en su órbita: en Chile, verano en diciembre e invierno en junio",
   BG + sol(160, 84) + '<ellipse cx="160" cy="84" rx="120" ry="44" class="as-svg__muted" stroke-dasharray="4 6"/>' +
   disc(40, 84, 13, "as-svg__cool") + disc(280, 84, 13, "as-svg__cool") +
   text(160, 24, "en Chile", 16) + text(64, 160, "diciembre", 16) + text(64, 180, "verano", 16) + text(256, 160, "junio", 16) + text(256, 180, "invierno", 16)),
 "c3": svg("En enero la Tierra está más cerca del Sol y en el hemisferio norte es invierno",
   BG + A + sol(50, 96, 30) + arrow(L, 86, 96, 186, 96, 3) + disc(226, 96, 32, "as-svg__cool") +
   '<line x1="194" y1="96" x2="258" y2="96" class="as-svg__ink"/>' + text(226, 88, "norte", 15) +
   text(160, 30, "enero: más cerca del Sol", 17) + text(160, 170, "y aun así, invierno en el norte", 16)),
 "c4": svg("La Tierra en dos puntos de su órbita con el eje inclinado unos 23,5 grados, apuntando siempre hacia el mismo lado",
   BG + sol(160, 84, 20) + earth(58, 84, 26) + earth(262, 84, 26) +
   text(160, 28, "eje inclinado unos 23,5 grados", 16) + text(160, 158, "apunta siempre hacia", 16) + text(160, 180, "la misma dirección", 16)),
 "c5": svg("Dos linternas: de frente la luz se concentra en poca superficie; de lado se reparte en más superficie",
   BG + '<path d="M60 40 L34 130 L94 130 Z" class="as-svg__warm"/>' + box(46, 26, 28, 18, "as-svg__fill", 3) +
   '<path d="M220 40 L180 130 L306 130 Z" class="as-svg__soft"/><path d="M220 40 L180 130 L306 130 Z" class="as-svg__ink"/>' + box(206, 26, 28, 18, "as-svg__fill", 3) +
   line(20, 130, 110, 130, 'stroke-width="3"') + line(170, 130, 310, 130, 'stroke-width="3"') +
   text(64, 156, "de frente", 16) + text(64, 178, "menos superficie", 15) + text(240, 156, "de lado", 16) + text(240, 178, "más superficie", 15)),
 "c7": svg("Dos fechas en el calendario, cerca del 21 de marzo y del 21 de septiembre, con un signo de pregunta",
   BG + box(46, 54, 96, 90, "as-svg__warm", 8) + box(46, 54, 96, 24, "as-svg__fill", 8) + text(94, 118, "21", 26) + text(94, 170, "marzo", 16) +
   box(178, 54, 96, 90, "as-svg__warm", 8) + box(178, 54, 96, 24, "as-svg__fill", 8) + text(226, 118, "21", 26) + text(226, 170, "septiembre", 16) +
   text(160, 34, "cerca de estas fechas", 17)),
 "c8": svg("En el hemisferio norte, el día más largo llega en junio, pero julio y agosto suelen ser más calurosos",
   BG + A + box(26, 62, 76, 56, "as-svg__warm", 6) + text(64, 96, "junio", 16) + arrow(L, 110, 90, 144, 90, 3) +
   box(152, 62, 70, 56, "as-svg__fill", 6) + text(187, 96, "julio", 16) + box(230, 62, 72, 56, "as-svg__fill", 6) + text(266, 96, "agosto", 16) +
   text(64, 142, "día más largo", 15) + text(226, 142, "más calurosos", 15) + text(160, 34, "hemisferio norte", 16) + text(160, 180, "el aire y el agua tardan", 16)),
}
LOTE.append(lesson(L, "Astronomía", "astronomia",
  "¿Por qué hay estaciones del año?", "No es por estar más cerca del Sol.",
  [card("c1", "portada", titulo="¿Por qué hay estaciones del año?", texto="En Chile, diciembre trae el verano y junio trae el invierno. ¿Será porque la Tierra se acerca y se aleja del Sol?", fuentes=["noaa-estaciones", "openstax-estaciones"]),
   card("c2", "pregunta", pregunta="¿En qué mes está la Tierra más cerca del Sol?", correctaId="a", opciones=[
     ("a", "En enero", "¡Exacto! Es verano en Chile, pero en el hemisferio norte es invierno."),
     ("b", "En julio", "No: en julio está en el punto más lejano."),
     ("c", "Está siempre a la misma distancia", "No: su órbita es levemente elíptica, y el punto más cercano llega en enero.")], fuentes=["noaa-estaciones"]),
   card("c3", "idea", titulo="No es la distancia", texto="En enero, cuando la Tierra está más cerca del Sol, es invierno en el hemisferio norte. Además, si la distancia fuera la causa, los dos hemisferios no tendrían estaciones opuestas.", fuentes=["noaa-estaciones", "openstax-estaciones"]),
   card("c4", "idea", titulo="Un eje inclinado", texto="El eje de la Tierra está inclinado unos 23,5 grados y apunta siempre hacia la misma dirección. Por eso, a lo largo del año, los rayos más directos llegan a distintas partes del planeta.", fuentes=["noaa-estaciones", "openstax-estaciones"]),
   card("c5", "idea", titulo="Como una linterna", texto="En el hemisferio inclinado hacia el Sol, los rayos llegan más de frente y se reparten en menos superficie, como una linterna apuntada de frente. Además, el Sol pasa más horas sobre el horizonte.", fuentes=["openstax-estaciones"]),
   card("c6", "pregunta", pregunta="En diciembre es verano en Chile. ¿Qué estación hay en el hemisferio norte?", correctaId="b", opciones=[
     ("a", "También verano", "No: las estaciones de los dos hemisferios son opuestas."),
     ("b", "Invierno", "¡Correcto! En diciembre, el Polo Sur se inclina hacia el Sol."),
     ("c", "Otoño", "No: en diciembre es invierno en el norte.")], fuentes=["noaa-estaciones"]),
   card("c7", "revelar", titulo="Dos días parejos", texto="Cerca del 21 de marzo y del 21 de septiembre ocurre algo en todo el planeta. ¿Qué es?",
        revelado="Son los equinoccios: cada lugar de la Tierra recibe unas 12 horas de luz y unas 12 de noche.", fuentes=["openstax-estaciones"]),
   card("c8", "dato", texto="En el hemisferio norte, el día más largo llega en junio, pero julio y agosto suelen ser más calurosos: el aire y el agua tardan en absorber el calor.", fuentes=["openstax-estaciones"])],
  ("Las estaciones", ["Las estaciones no se deben a la distancia al Sol: la Tierra está más cerca en enero.",
                      "La causa es el eje inclinado unos 23,5 grados, que apunta siempre hacia la misma dirección.",
                      "El hemisferio inclinado hacia el Sol recibe rayos más directos y más horas de luz."]),
  [src("noaa-estaciones", "NOAA, National Environmental Satellite, Data, and Information Service", "Why Does Earth Have Seasons?", "https://www.nesdis.noaa.gov/about/k-12-education/understanding-our-planet/why-does-earth-have-seasons", "Texto principal",
       ["El eje está inclinado 23,45 grados y apunta siempre en la misma dirección, así que distintas partes reciben los rayos más directos", "En junio es verano en el norte e invierno en el sur; en diciembre, lo contrario, con el Polo Sur inclinado hacia el Sol", "La órbita es levemente elíptica: el punto más cercano es en enero y el más lejano en julio; esto no causa las estaciones"],
       ["c1", "c2", "c3", "c4", "c6"], HOY),
   src("openstax-estaciones", "OpenStax, Rice University", "Astronomy, 4.2 The Seasons", "https://openstax.org/books/astronomy/pages/4-2-the-seasons", "Texto principal",
       ["La causa es la inclinación del eje de 23,5 grados, no la distancia al Sol", "Si la distancia fuera la causa, los dos hemisferios no tendrían estaciones opuestas", "Los rayos llegan más perpendiculares y se reparten en menos superficie, como una linterna; en verano el Sol está más tiempo sobre el horizonte", "En los equinoccios, cerca del 21 de marzo y de septiembre, cada lugar recibe unas 12 horas de luz y 12 de noche", "En el norte, julio y agosto suelen ser más calurosos que junio porque el aire y el agua tardan en absorber el calor", "En Chile, junio es frío y oscuro; las estaciones del hemisferio sur son opuestas"],
       ["c1", "c3", "c4", "c5", "c7", "c8"], HOY)]))

# =================================================================== 17-11 rebaja-alza (matemática)
L = "rebaja-alza"; A = arrow_def(L)
def bar(y, w, s, cls="as-svg__warm", x=24):
    return box(x, y, w, 30, cls, 4) + text(x + w / 2, y + 21, s, 16)
VIS[L] = {
 "c1": svg("Un precio baja 20 por ciento y luego sube 20 por ciento, pero no vuelve al mismo lugar",
   BG + A + box(26, 64, 70, 44, "as-svg__warm", 6) + text(61, 92, "precio", 16) + arrow(L, 104, 80, 146, 120, 3) +
   box(150, 112, 46, 34, "as-svg__soft", 6) + arrow(L, 200, 118, 236, 88, 3) + box(240, 74, 58, 44, "as-svg__warm", 6) + text(269, 102, "?", 20) +
   text(112, 128, "−20 %", 16, "end") + text(214, 74, "+20 %", 16, "end") + '<line x1="26" y1="60" x2="298" y2="60" class="as-svg__ink" stroke-dasharray="6 5"/>' +
   text(160, 186, "no vuelve al mismo lugar", 16)),
 "c3": svg("Una rebaja de 20 por ciento sobre 10.000 pesos quita 2.000 y deja 8.000",
   BG + bar(50, 272, "$10.000 precio original") + bar(104, 218, "$8.000", "as-svg__soft") + box(242, 104, 54, 30, "as-svg__fill", 4) + text(269, 125, "$2.000", 15) +
   text(160, 34, "20 % del precio original", 16) + text(160, 172, "la rebaja quita $2.000", 16)),
 "c4": svg("El alza de 20 por ciento se calcula sobre 8.000 pesos: suma 1.600 y llega a 9.600",
   BG + bar(50, 218, "$8.000") + box(242, 50, 54, 30, "as-svg__fill", 4) + text(269, 71, "$1.600", 15) +
   bar(104, 272, "$9.600", "as-svg__soft") +
   text(160, 34, "20 % del precio que quedó", 16) + text(160, 172, "el alza suma $1.600", 16)),
 "c5": svg("La rebaja quitó 2.000 pesos y el alza devolvió 1.600: faltan 400",
   BG + box(40, 40, 100, 100, "as-svg__warm", 4) + box(190, 60, 80, 80, "as-svg__fill", 4) +
   text(90, 96, "$2.000", 17) + text(230, 106, "$1.600", 16) + text(90, 162, "quitó", 16) + text(230, 162, "devolvió", 16) + text(160, 28, "mismo 20 %", 16) +
   text(160, 192, "faltan $400", 17)),
 "c7": svg("Para volver de 8.000 a 10.000 pesos hay que sumar 2.000: ¿qué porcentaje es?",
   BG + A + box(30, 70, 90, 50, "as-svg__warm", 6) + text(75, 101, "$8.000", 17) + arrow(L, 128, 95, 188, 95, 3) +
   box(196, 70, 96, 50, "as-svg__soft", 6) + text(244, 101, "$10.000", 17) + text(158, 76, "¿?", 18) + text(160, 36, "volver al precio original", 16) + text(160, 158, "¿cuánto debe subir?", 16)),
 "c8": svg("Un alza de 50 por ciento seguida de una baja de 50 por ciento deja el precio en 75 por ciento del original",
   BG + A + box(30, 60, 80, 80, "as-svg__warm", 4) + text(70, 106, "100 %", 16) + arrow(L, 116, 84, 136, 84, 3) +
   box(140, 30, 80, 110, "as-svg__soft", 4) + text(180, 90, "150 %", 16) + arrow(L, 226, 84, 246, 84, 3) +
   box(250, 80, 50, 60, "as-svg__fill", 4) + text(275, 116, "75 %", 15) +
   text(160, 164, "+50 % y luego −50 %", 16) + text(160, 186, "queda en 75 % del original", 16)),
}
LOTE.append(lesson(L, "Matemática cotidiana", "matematica",
  "¿Por qué una rebaja seguida de un alza igual no devuelve el precio inicial?", "Un porcentaje depende del número sobre el que se calcula.",
  [card("c1", "portada", titulo="¿Por qué una rebaja seguida de un alza igual no devuelve el precio inicial?", texto="Un precio baja 20 % y después sube 20 %. Parece que todo vuelve a su lugar, pero no. ¿Qué pasó?", fuentes=["omc-porcentajes"]),
   card("c2", "pregunta", pregunta="Un producto de $10.000 baja 20 % y luego sube 20 %. ¿En cuánto queda?", correctaId="b", opciones=[
     ("a", "$10.000", "Eso parece, pero el 20 % del alza se calcula sobre un precio menor."),
     ("b", "$9.600", "¡Exacto! Las próximas tarjetas muestran por qué."),
     ("c", "$10.400", "No: queda bajo el precio inicial, no sobre él.")], fuentes=["openstax-descuentos"]),
   card("c3", "idea", titulo="La rebaja mira el precio original", texto="Una rebaja se calcula sobre el precio original. Un 20 % de $10.000 son $2.000, y el precio queda en $8.000.", fuentes=["openstax-descuentos"]),
   card("c4", "idea", titulo="El alza parte más abajo", texto="El segundo porcentaje se calcula sobre el precio que quedó, no sobre el original. Un 20 % de $8.000 son $1.600, y el precio llega a $9.600.", fuentes=["openstax-descuentos"]),
   card("c5", "idea", titulo="Mismo porcentaje, distinta plata", texto="La rebaja quitó $2.000 y el alza devolvió solo $1.600. Por eso faltan $400: el mismo 20 % vale menos sobre un precio más bajo.", fuentes=["openstax-descuentos"]),
   card("c6", "pregunta", pregunta="¿Y si es al revés? Un producto de $10.000 sube 20 % y luego baja 20 %. ¿En cuánto queda?", correctaId="c", opciones=[
     ("a", "$10.000", "No: subir y bajar el mismo porcentaje no se cancela."),
     ("b", "$10.400", "No: sube a $12.000, y el 20 % de eso son $2.400."),
     ("c", "$9.600", "¡Correcto! Sube a $12.000, baja $2.400 y queda en $9.600.")], fuentes=["openstax-descuentos", "omc-porcentajes"]),
   card("c7", "revelar", titulo="Volver al precio original", texto="Para que el precio vuelva de $8.000 a $10.000, ¿cuánto debe subir?",
        revelado="Un 25 %. Hay que sumar $2.000, y $2.000 es la cuarta parte de $8.000.", fuentes=["openstax-descuentos"]),
   card("c8", "dato", texto="Con porcentajes mayores se nota más: un alza de 50 % seguida de una baja de 50 % deja el precio en 75 % del original.", fuentes=["omc-porcentajes"])],
  ("Rebajas y alzas", ["Cada porcentaje se calcula sobre el precio que hay en ese momento.",
                       "Por eso $10.000 con una baja de 20 % y un alza de 20 % queda en $9.600.",
                       "Para deshacer una baja de 20 % hace falta un alza de 25 %."]),
  [src("openstax-descuentos", "OpenStax, Rice University", "Contemporary Mathematics, 6.2 Discounts, Markups, and Sales Tax", "https://openstax.org/books/contemporary-mathematics/pages/6-2-discounts-markups-and-sales-tax", "Secciones sobre descuentos y aumentos",
       ["El descuento es el porcentaje multiplicado por el precio original", "En porcentajes sucesivos, el segundo se calcula sobre el precio que quedó tras el primero", "Un porcentaje de aumento se obtiene dividiendo el aumento por el precio de partida", "Cálculos propios: 20 % de $10.000 = $2.000; 20 % de $8.000 = $1.600; $8.000 + $1.600 = $9.600; $10.000 − $9.600 = $400; 20 % de $12.000 = $2.400; $2.000 ÷ $8.000 = 25 %"],
       ["c2", "c3", "c4", "c5", "c6", "c7"], HOY),
   src("omc-porcentajes", "One Mathematical Cat, Please! (sitio educativo de matemática)", "More practice with percents: percent increase and decrease", "https://www.onemathematicalcat.org/OneMathematicalCat_Offline/Algebra1/more_prob_percent_inc_decOffline.htm", "Problemas de aumento seguido de disminución",
       ["El cambio final se obtiene multiplicando los factores, no sumando los porcentajes", "Un aumento de 50 % y luego una disminución de 50 %: (0,5)(1,5) = 0,75, es decir, 75 % del original"],
       ["c1", "c6", "c8"], HOY)]))

# Agrega las ilustraciones a la portada y a las tarjetas idea, revelar y dato.
for L_ in LOTE:
    for c in L_["tarjetas"]:
        if c["tipo"] in ("portada", "idea", "revelar", "dato"):
            c["visual"] = VIS[L_["id"]][c["id"]]

if __name__ == "__main__":
    for L_ in LOTE:
        validate_visuals(L_)
    for lid, rev, sha in write("lote5", LOTE):
        print(f"{lid} r{rev}  {sha[:12]}")
