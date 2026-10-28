# Lote 3 (opción A, 26-10-2026): ilustraciones SVG para las lecciones programadas del 26-10 al 03-11.
# Aprobado por Max el 26-10-2026 ("si perfecto"). Son REVISIONES NUEVAS: el texto, las preguntas, el resumen y las
# fuentes se copian sin cambios desde la revisión publicada; solo se agrega "visual" a la portada y a las tarjetas
# idea, revelar y dato. Cada dibujo representa únicamente lo que ya dice el texto de su tarjeta.
# Salida: borradores/lote3/
import copy, json, os, sys
HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "visuales"))
from almanaque_lib import write
from svgkit import svg, BG, arrow_def, arrow, text, poly, moon, arch, sat, phone, book, waves

ROOT = os.path.join(HERE, "..", "..")
def base(lid, rev):
    return json.load(open(os.path.join(ROOT, "data", "lessons", f"{lid}.r{rev}.json"), encoding="utf-8"))

V = {}

# ------------------------------------------------------------------ arco-panteon (r4 -> r5)
L = "arco-panteon"; A = arrow_def(L)
door = '<rect x="110" y="150" width="100" height="40" class="as-svg__soft"/>'
V[L] = {
 "c1": svg("Un arco de piedra sobre una puerta, cargando el peso de lo que tiene encima",
   BG + A + arch(160, 175, 55, 85) + '<rect x="70" y="40" width="180" height="30" rx="4" class="as-svg__ink"/>' +
   text(160, 61, "peso de arriba") + arrow(L, 160, 72, 160, 86)),
 "c2": svg("Un arco hecho de piedras en forma de cuña; la del centro, arriba, es la clave",
   BG + A + arch(160, 185, 60, 100) + text(160, 34, "clave", 17) + arrow(L, 160, 40, 160, 78) +
   text(40, 120, "dovela", 17, "start") + arrow(L, 66, 128, 84, 140)),
 "c3": svg("El peso viaja por la curva del arco y aprieta unas piedras contra otras",
   BG + A + arch(160, 185, 60, 100) +
   '<path d="M160 72 C120 72 96 96 86 140" class="as-svg__ink as-svg__accent" stroke-width="3" marker-end="url(#arco-panteon-ah)"/>'
   '<path d="M160 72 C200 72 224 96 234 140" class="as-svg__ink as-svg__accent" stroke-width="3" marker-end="url(#arco-panteon-ah)"/>' +
   text(160, 30, "el peso viaja por la curva", 16)),
 "c5": svg("La base del arco empuja hacia afuera y los muros de los lados resisten ese empuje",
   BG + A + arch(160, 175, 50, 80) +
   '<rect x="20" y="95" width="56" height="80" class="as-svg__fill"/><rect x="20" y="95" width="56" height="80" class="as-svg__ink"/>'
   '<rect x="244" y="95" width="56" height="80" class="as-svg__fill"/><rect x="244" y="95" width="56" height="80" class="as-svg__ink"/>' +
   arrow(L, 110, 160, 82, 160, 3) + arrow(L, 210, 160, 238, 160, 3) +
   text(160, 34, "empuja hacia afuera") + text(160, 56, "y el edificio lo resiste", 15, muted=True)),
 "c6": svg("Corte de la cúpula del Panteón: el ancho interior y la altura miden lo mismo, 43,2 metros; cabría una esfera",
   BG + A + '<path d="M90 110 A70 70 0 0 1 230 110 L230 180 L90 180 Z" class="as-svg__warm"/><path d="M90 110 A70 70 0 0 1 230 110 L230 180 L90 180 Z" class="as-svg__ink"/>'
   '<circle cx="160" cy="110" r="70" class="as-svg__ink" stroke-dasharray="5 5"/>' +
   '<line x1="90" y1="192" x2="230" y2="192" class="as-svg__ink"/>' + text(160, 30, "43,2 m de ancho y de alto", 16) +
   text(160, 120, "cabría una esfera", 15)),
 "c8": svg("En la cima de la cúpula está el óculo, por donde entra la luz",
   BG + '<path d="M60 170 A100 100 0 0 1 145 72 L175 72 A100 100 0 0 1 260 170 Z" class="as-svg__warm"/>'
   '<path d="M60 170 A100 100 0 0 1 145 72 M175 72 A100 100 0 0 1 260 170 L60 170" class="as-svg__ink"/>'
   '<path d="M150 72 L130 170 M160 72 L160 170 M170 72 L190 170" class="as-svg__coolline" stroke-dasharray="6 6"/>'
   '<circle cx="160" cy="34" r="16" class="as-svg__sun"/>' + text(206, 66, "óculo", 17, "start")),
}

# ------------------------------------------------------------------ temblores-chile (r2 -> r3)
L = "temblores-chile"; A = arrow_def(L)
sea = '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'
V[L] = {
 "c1": svg("La costa de Chile: el mar a la izquierda, la cordillera a la derecha y la tierra que se sacude",
   sea + '<path d="M0 120 L150 120 L150 200 L0 200 Z" class="as-svg__cool"/>' + waves(10, 140, 112) +
   '<path d="M150 120 L190 90 L220 110 L260 60 L300 100 L320 90 L320 200 L150 200 Z" class="as-svg__warm"/><path d="M150 120 L190 90 L220 110 L260 60 L300 100 L320 90" class="as-svg__ink"/>' +
   '<path d="M170 40 q4 -6 0 -12 M178 44 q8 -12 0 -24 M290 40 q-4 -6 0 -12 M282 44 q-8 -12 0 -24" class="as-svg__ink"/>' + text(250, 160, "Chile", 18) + text(70, 160, "Pacífico", 16)),
 "c2": svg("Corte de la tierra frente a Chile: la placa de Nazca bajo el océano y la placa Sudamericana bajo el continente",
   BG + A + '<path d="M10 90 L160 90 L160 150 L10 150 Z" class="as-svg__fill"/><path d="M10 90 L160 90 L160 150 L10 150 Z" class="as-svg__ink"/>'
   '<path d="M164 70 L310 70 L310 150 L164 150 Z" class="as-svg__warm"/><path d="M164 70 L310 70 L310 150 L164 150 Z" class="as-svg__ink"/>' +
   waves(14, 150, 80) + text(85, 175, "placa de Nazca", 15) + text(237, 175, "placa Sudamericana", 15) +
   arrow(L, 110, 40, 150, 40) + arrow(L, 214, 40, 174, 40) + text(162, 26, "se juntan", 15)),
 "c3": svg("La placa de Nazca se mete por debajo de la placa Sudamericana: subducción",
   BG + A + '<path d="M10 80 L170 80 L300 170 L300 190 L170 100 L10 100 Z" class="as-svg__fill"/><path d="M10 80 L170 80 L300 170 L300 190 L170 100 L10 100 Z" class="as-svg__ink"/>'
   '<path d="M170 78 L310 78 L310 160 Z" class="as-svg__warm"/><path d="M170 78 L310 78 L310 160 Z" class="as-svg__ink"/>' +
   arrow(L, 60, 64, 140, 64, 3) + text(100, 50, "6,5 a 8 cm por año", 15) + text(304, 94, "Sudamérica", 15, "end") + text(70, 128, "Nazca", 16)),
 "c5": svg("Los bordes ásperos de las placas quedan trabados, acumulan energía y se destraban de golpe",
   BG + A + '<path d="M20 60 L150 60 L140 80 L160 95 L140 110 L160 125 L150 140 L20 140 Z" class="as-svg__fill"/><path d="M20 60 L150 60 L140 80 L160 95 L140 110 L160 125 L150 140 L20 140 Z" class="as-svg__ink"/>'
   '<path d="M300 60 L170 60 L160 80 L180 95 L160 110 L180 125 L170 140 L300 140 Z" class="as-svg__warm"/><path d="M300 60 L170 60 L160 80 L180 95 L160 110 L180 125 L170 140 L300 140 Z" class="as-svg__ink"/>' +
   '<path d="M160 20 l6 14 l14 -6 l-8 13 l12 9 l-15 1 l2 15 l-11 -10 l-11 10 l2 -15 l-15 -1 l12 -9 l-8 -13 l14 6 Z" class="as-svg__sun"/>' +
   text(160, 175, "trabados... y se destraban de golpe", 15)),
 "c6": svg("Un sismograma con un salto enorme: Valdivia, 22 de mayo de 1960, magnitud 9,5",
   BG + '<path d="M10 120 L60 120 L66 112 L72 128 L78 120 L120 120 L126 60 L134 180 L142 30 L150 190 L158 50 L166 160 L174 90 L182 140 L190 120 L310 120" class="as-svg__ink" stroke-width="2"/>' +
   text(240, 60, "Valdivia, 1960", 17) + text(240, 84, "magnitud 9,5", 17)),
 "c8": svg("El tsunami de 1960 cruzó el Pacífico: desde Chile llegó a Hawái unas 15 horas después y también a Japón",
   BG + A + '<rect x="290" y="70" width="14" height="110" rx="4" class="as-svg__warm"/>' + text(297, 192, "Chile", 14) +
   '<circle cx="160" cy="70" r="6" class="as-svg__fill"/>' + text(160, 56, "Hawái", 15) +
   '<rect x="16" y="40" width="14" height="40" rx="4" class="as-svg__warm"/>' + text(23, 98, "Japón", 14) +
   '<path d="M286 130 C240 110 200 90 170 74" class="as-svg__coolline" marker-end="url(#temblores-chile-ah)"/>'
   '<path d="M150 72 C110 60 70 56 36 58" class="as-svg__coolline" marker-end="url(#temblores-chile-ah)"/>' + text(236, 140, "unas 15 horas", 15)),
}

# ------------------------------------------------------------------ unidad-fomento (r2 -> r3)
L = "unidad-fomento"; A = arrow_def(L)
def coin(x, y, r, label):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="as-svg__warm"/><circle cx="{x}" cy="{y}" r="{r}" class="as-svg__ink"/>' + text(x, y + 7, label, 20)
V[L] = {
 "c1": svg("Una moneda con la sigla UF junto a billetes en pesos, con un signo de pregunta",
   BG + coin(100, 100, 46, "UF") + '<rect x="180" y="70" width="90" height="50" rx="6" class="as-svg__fill"/><rect x="180" y="70" width="90" height="50" rx="6" class="as-svg__ink"/>' +
   text(225, 102, "$", 24) + text(160, 180, "¿por qué no en pesos?", 16)),
 "c2": svg("Una canasta con productos y servicios de los hogares: el INE mide cada mes cuánto cambian sus precios (IPC)",
   BG + '<path d="M90 90 L230 90 L215 160 L105 160 Z" class="as-svg__warm"/><path d="M90 90 L230 90 L215 160 L105 160 Z" class="as-svg__ink"/>'
   '<path d="M120 90 C120 50 200 50 200 90" class="as-svg__ink"/><circle cx="130" cy="82" r="12" class="as-svg__fill"/><rect x="150" y="64" width="18" height="28" rx="3" class="as-svg__cool"/><circle cx="190" cy="80" r="10" class="as-svg__fill"/>' +
   text(160, 135, "IPC", 22) + text(160, 190, "el INE lo mide cada mes", 15)),
 "c3": svg("El IPC del mes anterior reajusta día a día el valor de la UF en pesos",
   BG + A + '<rect x="24" y="60" width="96" height="80" rx="8" class="as-svg__fill"/><rect x="24" y="60" width="96" height="80" rx="8" class="as-svg__ink"/>' +
   text(72, 96, "IPC", 20) + text(72, 120, "mes anterior", 13) + arrow(L, 130, 100, 186, 100, 3) + coin(240, 100, 40, "UF") +
   text(240, 170, "en $, día a día", 15) + text(72, 170, "Banco Central", 14, muted=True)),
 "c5": svg("Un arriendo de 10 UF: cada mes son las mismas 10 UF, pero equivalen a un poco más de pesos si el IPC subió",
   BG + ''.join(f'<rect x="{50 + i * 60}" y="{140 - (60 + i * 6)}" width="40" height="{60 + i * 6}" rx="4" class="as-svg__warm"/><rect x="{50 + i * 60}" y="{140 - (60 + i * 6)}" width="40" height="{60 + i * 6}" rx="4" class="as-svg__ink"/>'
               + text(70 + i * 60, 132, "10", 15) for i in range(4)) +
   text(160, 34, "siempre 10 UF", 16) + text(160, 166, "un poco más de pesos", 15) + text(160, 188, "si el IPC subió", 14, muted=True)),
 "c6": svg("Un crédito en UF: la deuda en pesos se reajusta según el IPC del mes anterior",
   BG + A + '<rect x="40" y="40" width="90" height="120" rx="6" class="as-svg__warm"/><rect x="40" y="40" width="90" height="120" rx="6" class="as-svg__ink"/>' +
   text(85, 80, "crédito", 15) + text(85, 108, "en UF", 18) + '<line x1="56" y1="126" x2="114" y2="126" class="as-svg__ink"/><line x1="56" y1="140" x2="100" y2="140" class="as-svg__ink"/>' +
   arrow(L, 142, 100, 192, 100, 3) + text(250, 96, "deuda en $", 16) + text(250, 120, "se reajusta", 15)),
 "c8": svg("A más tardar el día 9 de cada mes se publican los valores de la UF desde el 10 hasta el 9 del mes siguiente",
   BG + A + '<rect x="30" y="50" width="100" height="100" rx="8" class="as-svg__ink"/><rect x="30" y="50" width="100" height="24" rx="8" class="as-svg__fill"/>' +
   text(80, 120, "día 9", 22) + text(80, 175, "se publican", 15) + arrow(L, 140, 100, 176, 100, 3) +
   '<rect x="186" y="70" width="110" height="60" rx="8" class="as-svg__warm"/><rect x="186" y="70" width="110" height="60" rx="8" class="as-svg__ink"/>' +
   text(241, 98, "del 10", 15) + text(241, 118, "al 9 siguiente", 14)),
}

# ------------------------------------------------------------------ fases-luna (r2 -> r3)
L = "fases-luna"; A = arrow_def(L)
V[L] = {
 "c1": svg("La Luna en distintas fases: tajada, mitad y círculo completo",
   BG + moon(70, 90, 34, "creciente") + moon(160, 90, 34, "cuarto-c") + moon(250, 90, 34, "llena") + text(160, 170, "cambia lo que vemos", 16)),
 "c2": svg("El Sol ilumina a la Luna y la Luna refleja esa luz hacia la Tierra",
   BG + A + '<circle cx="40" cy="70" r="26" class="as-svg__sun"/>' + text(40, 120, "Sol", 15) +
   moon(170, 70, 20, "llena") + text(170, 110, "Luna", 15) +
   '<circle cx="270" cy="150" r="22" class="as-svg__cool"/><circle cx="270" cy="150" r="22" class="as-svg__ink"/>' + text(270, 190, "Tierra", 15) +
   arrow(L, 70, 70, 144, 70) + arrow(L, 188, 84, 250, 134) + text(220, 48, "refleja la luz", 15)),
 "c3": svg("El Sol ilumina siempre la mitad de la Luna que mira hacia él; desde la Tierra vemos más o menos de esa mitad",
   BG + '<circle cx="28" cy="100" r="20" class="as-svg__sun"/>' + text(28, 140, "Sol", 14) +
   '<circle cx="190" cy="100" r="18" class="as-svg__cool"/><circle cx="190" cy="100" r="18" class="as-svg__ink"/>' +
   '<circle cx="190" cy="100" r="62" class="as-svg__muted" stroke-dasharray="4 6"/>' +
   ''.join(f'<path d="M{x} {y - 12} A12 12 0 0 0 {x} {y + 12} Z" class="as-svg__sun"/><circle cx="{x}" cy="{y}" r="12" class="as-svg__ink"/>' for x, y in [(128, 100), (190, 38), (252, 100), (190, 162)]) +
   text(190, 196, "siempre una mitad iluminada", 14)),
 "c5": svg("Una flecha circular: el ciclo de fases se repite cada 29 días y medio",
   BG + A + '<path d="M160 40 A60 60 0 1 1 100 100" class="as-svg__ink as-svg__accent" stroke-width="3" marker-end="url(#fases-luna-ah)"/>' +
   moon(160, 40, 12, "llena") + text(160, 106, "29,5", 26) + text(160, 128, "días", 16)),
 "c6": svg("En el hemisferio sur, la Luna creciente suele parecerse a una C y la menguante a una D",
   BG + moon(95, 85, 40, "creciente") + moon(225, 85, 40, "menguante") +
   text(95, 155, "C", 26) + text(95, 182, "creciente", 15) + text(225, 155, "D", 26) + text(225, 182, "menguante", 15)),
 "c8": svg("Las ocho fases de la Luna, de luna nueva a luna llena y de vuelta",
   BG + ''.join(moon(42 + i * 79, 62, 22, k) for i, k in enumerate(["nueva", "creciente", "cuarto-c", "gibosa-c"])) +
   ''.join(moon(42 + i * 79, 140, 22, k) for i, k in enumerate(["llena", "gibosa-m", "cuarto-m", "menguante"])) +
   text(160, 194, "8 fases", 15)),
}

# ------------------------------------------------------------------ gabriela-mistral (r3 -> r4)
L = "gabriela-mistral"; A = arrow_def(L)
V[L] = {
 "c1": svg("Los cerros del Valle del Elqui, un libro abierto y el año 1945",
   BG + '<path d="M0 150 L60 90 L110 130 L170 70 L230 120 L270 95 L320 135 L320 200 L0 200 Z" class="as-svg__fill"/>'
   '<path d="M110 150 C130 140 150 140 160 150 C170 140 190 140 210 150 L210 186 C190 176 170 176 160 186 C150 176 130 176 110 186 Z" class="as-svg__warm"/>'
   '<path d="M110 150 C130 140 150 140 160 150 C170 140 190 140 210 150 L210 186 C190 176 170 176 160 186 C150 176 130 176 110 186 Z M160 150 L160 186" class="as-svg__ink"/>' +
   text(60, 40, "Vicuña", 17) + text(260, 40, "1945", 20)),
 "c2": svg("Una pizarra de escuela: Lucila nació en Vicuña en 1889 y fue maestra desde muy joven",
   BG + '<rect x="50" y="40" width="220" height="110" rx="6" class="as-svg__fill"/><rect x="50" y="40" width="220" height="110" rx="6" class="as-svg__ink"/>'
   '<rect x="60" y="50" width="200" height="90" rx="4" class="as-svg__warm"/>' + text(160, 90, "Lucila", 22) + text(160, 120, "Vicuña, 1889", 16) +
   '<line x1="90" y1="150" x2="80" y2="185" class="as-svg__ink"/><line x1="230" y1="150" x2="240" y2="185" class="as-svg__ink"/>'),
 "c3": svg("Una pluma firmando: Gabriela Mistral fue el nombre con que firmó sus poemas",
   BG + '<line x1="40" y1="140" x2="280" y2="140" class="as-svg__ink"/>' + text(150, 128, "Gabriela Mistral", 22) +
   '<path d="M250 40 C280 50 290 80 270 110 L262 126 L256 122 L260 104 C240 90 238 60 250 40 Z" class="as-svg__fill"/><path d="M250 40 C280 50 290 80 270 110 L262 126 L256 122 L260 104 C240 90 238 60 250 40 Z" class="as-svg__ink"/>' +
   text(160, 180, "su nombre para firmar", 15, muted=True)),
 "c5": svg("Una cinta de premio de 1914 y el libro Desolación de 1922",
   BG + '<circle cx="90" cy="80" r="34" class="as-svg__sun"/><circle cx="90" cy="80" r="34" class="as-svg__ink"/><path d="M74 110 L66 160 L90 146 L114 160 L106 110" class="as-svg__fill"/>' +
   text(90, 88, "1914", 18) + book(190, 50, 80, 100) + text(234, 96, "Deso-", 15) + text(234, 116, "lación", 15) + text(234, 182, "1922", 17)),
 "c6": svg("Un libro llamado Ternura, de 1924, con una luna y estrellas de canción de cuna",
   BG + book(110, 50, 100, 120, "as-svg__fill") + text(164, 112, "Ternura", 18) + text(164, 150, "1924", 16) +
   moon(60, 60, 20, "creciente") + '<path d="M260 50 l4 10 l10 1 l-8 6 l3 10 l-9 -6 l-9 6 l3 -10 l-8 -6 l10 -1 Z" class="as-svg__sun"/>'
   '<path d="M270 110 l3 7 l7 1 l-6 4 l2 7 l-6 -4 l-6 4 l2 -7 l-6 -4 l7 -1 Z" class="as-svg__sun"/>'),
 "c7": svg("Una medalla con el año 1945: el Premio Nobel de Literatura",
   BG + '<path d="M130 20 L150 90 L170 90 L190 20" class="as-svg__fill"/><circle cx="160" cy="120" r="50" class="as-svg__sun"/><circle cx="160" cy="120" r="50" class="as-svg__ink"/>'
   '<circle cx="160" cy="120" r="40" class="as-svg__ink"/>' + text(160, 116, "Nobel", 18) + text(160, 140, "1945", 18)),
}

# ------------------------------------------------------------------ como-funciona-gps (r3 -> r4)
L = "como-funciona-gps"; A = arrow_def(L)
V[L] = {
 "c1": svg("Un celular con un punto en el mapa y un satélite en el espacio enviándole señales",
   BG + sat(230, 50) + '<path d="M200 80 q-10 10 -20 0 M210 92 q-20 20 -40 0" class="as-svg__ink"/>' + phone(110, 120, 1.3)),
 "c2": svg("La Tierra con satélites en órbita: al menos 24, a unos 20.200 kilómetros de altura",
   BG + '<circle cx="160" cy="105" r="40" class="as-svg__cool"/><circle cx="160" cy="105" r="40" class="as-svg__ink"/>'
   '<ellipse cx="160" cy="105" rx="130" ry="70" class="as-svg__muted" stroke-dasharray="4 6"/>' +
   sat(40, 90, 0.55) + sat(280, 120, 0.55) + sat(160, 36, 0.55) + sat(160, 174, 0.55) +
   text(160, 110, "Tierra", 15) + text(160, 196, "al menos 24 · 20.200 km", 14)),
 "c3": svg("El satélite envía su señal con la hora exacta y el receptor anota a qué hora llega",
   BG + A + sat(70, 50) + text(70, 84, "hora de salida", 14) + arrow(L, 92, 70, 214, 130, 3) + phone(240, 140, 0.9, pin=False) +
   text(240, 194, "hora de llegada", 14) + '<circle cx="40" cy="160" r="20" class="as-svg__ink"/><line x1="40" y1="160" x2="40" y2="146" class="as-svg__ink"/><line x1="40" y1="160" x2="50" y2="160" class="as-svg__ink"/>'),
 "c5": svg("Cuatro satélites con líneas hacia un mismo punto: con cuatro distancias se calcula la posición",
   BG + ''.join(sat(x, y, 0.6) + f'<line x1="{x}" y1="{y}" x2="160" y2="150" class="as-svg__ink" stroke-dasharray="5 5"/>' for x, y in [(40, 40), (120, 26), (200, 26), (280, 40)]) +
   '<path d="M160 160 C150 148 150 136 160 136 C170 136 170 148 160 160 Z" class="as-svg__fill"/>' + text(160, 190, "4 distancias", 16)),
 "c6": svg("Un edificio bloquea la señal del satélite; en un lugar abierto la señal llega bien",
   BG + sat(160, 34, 0.8) + '<rect x="40" y="90" width="70" height="100" class="as-svg__fill"/><rect x="40" y="90" width="70" height="100" class="as-svg__ink"/>' +
   '<line x1="140" y1="50" x2="96" y2="92" class="as-svg__ink" stroke-dasharray="5 5"/>' + text(75, 80, "✗", 22) + phone(60, 170, 0.5, pin=False) +
   '<line x1="180" y1="50" x2="246" y2="140" class="as-svg__ink" stroke-dasharray="5 5"/>' + phone(250, 160, 0.6) + text(250, 116, "✓", 22)),
 "c8": svg("Un satélite GPS da dos vueltas completas a la Tierra cada día",
   BG + A + '<circle cx="160" cy="100" r="34" class="as-svg__cool"/><circle cx="160" cy="100" r="34" class="as-svg__ink"/>'
   '<path d="M160 30 A70 70 0 1 1 90 100" class="as-svg__ink as-svg__accent" stroke-width="3" marker-end="url(#como-funciona-gps-ah)"/>' +
   sat(160, 30, 0.5) + text(160, 106, "×2", 22) + text(160, 192, "dos vueltas por día", 15)),
}

# ------------------------------------------------------------------ mar-salado (r2 -> r3)
L = "mar-salado"; A = arrow_def(L)
dots = lambda pts: "".join(f'<circle cx="{x}" cy="{y}" r="4" class="as-svg__fill"/>' for x, y in pts)
V[L] = {
 "c1": svg("El mar con olas y un salero: ¿de dónde sale tanta sal?",
   BG + '<rect x="0" y="110" width="320" height="90" class="as-svg__cool"/>' + waves(0, 320, 110, 8, 32) +
   '<path d="M220 30 L260 30 L266 90 L214 90 Z" class="as-svg__warm"/><path d="M220 30 L260 30 L266 90 L214 90 Z" class="as-svg__ink"/>'
   '<circle cx="232" cy="42" r="2" class="as-svg__label"/><circle cx="240" cy="42" r="2" class="as-svg__label"/><circle cx="248" cy="42" r="2" class="as-svg__label"/>' +
   text(100, 70, "¿de dónde", 18) + text(100, 92, "sale la sal?", 18)),
 "c3": svg("La lluvia, levemente ácida, cae sobre las rocas y desprende minerales que quedan disueltos en el agua",
   BG + '<path d="M90 50 C70 50 60 30 80 22 C86 8 116 8 122 22 C140 18 150 36 136 50 Z" class="as-svg__ink"/>' +
   ''.join(f'<line x1="{x}" y1="60" x2="{x - 6}" y2="80" class="as-svg__coolline"/>' for x in (90, 110, 130)) +
   '<path d="M40 180 L80 110 L130 140 L180 100 L240 150 L280 120 L300 180 Z" class="as-svg__warm"/><path d="M40 180 L80 110 L130 140 L180 100 L240 150 L280 120 L300 180 Z" class="as-svg__ink"/>' +
   dots([(150, 150), (170, 160), (200, 150), (220, 165)]) + text(240, 60, "minerales", 16) + text(240, 82, "disueltos", 16)),
 "c4": svg("Un río lleva los minerales disueltos desde los cerros hasta el océano",
   BG + A + '<path d="M0 60 L60 20 L120 60 Z" class="as-svg__warm"/><path d="M0 60 L60 20 L120 60" class="as-svg__ink"/>'
   '<path d="M60 60 C80 100 140 90 170 130 C190 160 230 160 250 170" class="as-svg__coolline"/>' +
   '<rect x="240" y="150" width="80" height="50" class="as-svg__cool"/>' + dots([(90, 92), (150, 112), (200, 155)]) + text(282, 140, "océano", 15)),
 "c5": svg("En el fondo del océano, grietas calentadas por el magma y volcanes submarinos también aportan sales",
   BG + '<rect x="0" y="20" width="320" height="140" class="as-svg__cool"/>' + waves(0, 320, 20, 6, 32) +
   '<path d="M0 160 L120 160 L160 110 L200 160 L320 160 L320 200 L0 200 Z" class="as-svg__warm"/><path d="M0 160 L120 160 L160 110 L200 160 L320 160" class="as-svg__ink"/>' +
   '<path d="M160 110 q-6 -14 0 -28 q6 -14 0 -28" class="as-svg__warmline"/>' + dots([(150, 70), (172, 60), (162, 44)]) +
   text(60, 140, "volcán submarino", 14) + '<line x1="250" y1="160" x2="262" y2="190" class="as-svg__ink"/>' + text(262, 140, "grietas", 14)),
 "c6": svg("En promedio, un kilo de agua de mar tiene unos 35 gramos de sal: cerca del 3,5 %",
   BG + '<path d="M60 50 L140 50 L150 170 L50 170 Z" class="as-svg__cool"/><path d="M60 50 L140 50 L150 170 L50 170 Z" class="as-svg__ink"/>' +
   text(100, 120, "1 kg", 20) + '<path d="M200 170 L240 120 L280 170 Z" class="as-svg__warm"/><path d="M200 170 L240 120 L280 170 Z" class="as-svg__ink"/>' +
   text(240, 105, "35 g", 20) + text(160, 192, "en promedio · 3,5 %", 14)),
 "c8": svg("Entre las sales disueltas, el sodio y el cloruro son cerca del 85 %",
   BG + '<rect x="30" y="80" width="221" height="44" rx="6" class="as-svg__fill"/><rect x="251" y="80" width="39" height="44" rx="6" class="as-svg__warm"/>'
   '<rect x="30" y="80" width="260" height="44" rx="6" class="as-svg__ink"/>' + text(140, 108, "sodio + cloruro ≈ 85 %", 15) +
   text(270, 148, "otros", 14) + text(160, 52, "iones disueltos en el mar", 15)),
}

# ------------------------------------------------------------------ armar revisiones nuevas
REV = {"arco-panteon": 4, "pan-duro": 2, "temblores-chile": 2, "unidad-fomento": 2, "fases-luna": 2,
       "gabriela-mistral": 3, "como-funciona-gps": 3, "mar-salado": 2}
muestra = json.load(open(os.path.join(ROOT, "borradores", "muestra_visual", "pan-duro.r3.json"), encoding="utf-8"))
V["pan-duro"] = {c["id"]: c["visual"] for c in muestra["tarjetas"] if "visual" in c}

LOTE = []
for lid, rev in REV.items():
    L = copy.deepcopy(base(lid, rev))
    L["revision"] = rev + 1
    for c in L["tarjetas"]:
        if c["tipo"] in ("portada", "idea", "revelar", "dato"):
            c["visual"] = V[lid][c["id"]]
    LOTE.append(L)

if __name__ == "__main__":
    for lid, rev, sha in write("lote3", LOTE):
        print(f"{lid} r{rev}  {sha[:12]}")
