# Genera data/lessons/*.json, data/catalog.v1.json y data/calendar.v1.json
# Esquema de lección 1.0 acordado con ChatGPT (mensajes N°1–N°4).
import json, hashlib, os, math

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "data", "lessons")
os.makedirs(OUT, exist_ok=True)
HOY = "2026-10-19"

def svg(vb, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="as-svg" role="img">'
            f'<title>{title}</title>{body}</svg>')

def arrow_def(pid):
    return (f'<defs><marker id="{pid}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            f'<path d="M0 0L10 5L0 10z" class="as-svg__accent"/></marker></defs>')

def src(id, entidad, titulo, url, ubicacion, afirmaciones, consultada):
    return dict(id=id, entidad=entidad, titulo=titulo, url=url, ubicacion=ubicacion,
                afirmaciones=afirmaciones, consultadaEl=consultada)

def q(id, pregunta, opciones, correcta, fuentes):
    return dict(id=id, pregunta=pregunta,
                opciones=[dict(id=o[0], texto=o[1], retroalimentacion=o[2]) for o in opciones],
                correctaId=correcta, fuenteIds=fuentes)

def step(id, titulo, parrafos, fuentes, figura=None, actividad=None):
    s = dict(id=id, titulo=titulo, parrafos=parrafos, fuenteIds=fuentes)
    if figura: s["figura"] = figura
    if actividad: s["actividad"] = dict(tipo=actividad[0], pregunta=actividad[1], respuesta=actividad[2])
    return s

def fig(contenido, alt, pie):
    return dict(tipo="svg", contenido=contenido, alt=alt, pie=pie)

REVISION = {"numero-aureo": 2, "fases-lunares": 3}  # r1 enviada a revisión: inmutable; los cambios van en r2
def lesson(id, disciplina, familia, etiquetas, titulo, minutos, objetivos, entrada, pasos, quiz, repaso, cierre, fuentes):
    return {
        "schemaVersion": "1.0", "id": id, "revision": REVISION.get(id, 1), "idioma": "es-CL",
        "disciplina": disciplina, "familia": familia, "etiquetas": etiquetas,
        "titulo": titulo, "nivel": "introductorio", "minutosEstimados": minutos,
        "objetivos": objetivos, "prerrequisitos": [], "entrada": {"pregunta": entrada},
        "pasos": pasos, "quiz": quiz,
        "repaso": [dict(id=r[0], pregunta=r[1], respuesta=r[2]) for r in repaso],
        "cierre": cierre, "fuentes": fuentes,
        "controlEditorial": {"estado": "borrador", "revisadoPor": None, "fechaRevision": None},
    }

L = []

# ------------------------------------------------------------------ 1
rect = svg("0 0 324 201.8",
    '<rect x="2" y="2" width="320" height="197.771" class="as-svg__surface"/>'
    '<rect x="2" y="2" width="320" height="197.771" class="as-svg__ink"/>'
    '<line x1="199.771" y1="2" x2="199.771" y2="199.771" class="as-svg__ink"/>'
    '<line x1="199.771" y1="124.229" x2="322" y2="124.229" class="as-svg__ink"/>'
    '<line x1="246.458" y1="124.229" x2="246.458" y2="199.771" class="as-svg__ink"/>'
    '<path d="M2 199.771 A197.771 197.771 0 0 1 199.771 2 A122.229 122.229 0 0 1 322 124.229 A75.542 75.542 0 0 1 246.458 199.771" class="as-svg__ink as-svg__accent" stroke-width="2.5"/>'
    '<text x="100.885" y="130.885" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="12">cuadrado</text>'
    '<text x="260.885" y="93.115" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="11">cuadrado</text>'
    ,
    "Rectángulo áureo dividido en cuadrados sucesivos")
L.append(lesson("numero-aureo", "Matemática", "matematica", ["proporción", "Fibonacci", "irracionales"],
  "El número áureo", 12,
  ["Calcular φ a partir de su definición", "Relacionar φ con la sucesión de Fibonacci", "Distinguir datos comprobados de afirmaciones populares"],
  "Antes de leer: ¿crees que existe una proporción \"perfecta\"? ¿Dónde has escuchado que aparece?",
  [
    step("definicion", "La definición", [
      "Divide un segmento en dos partes, a (la mayor) y b (la menor), con a > b > 0, de modo que el todo sea a la parte mayor como la mayor es a la menor: (a + b) / a = a / b.",
      "Esa razón se llama φ (fi). Su valor exacto es φ = (1 + √5) / 2 = 1,6180339887… Es un número irracional: sus decimales no terminan ni forman un período repetitivo."],
      ["mathworld", "britannica-aureo", "mathworld-rect"],
      fig(rect, "Rectángulo de 320 × 197,77 unidades (razón φ) dividido en cuadrados sucesivos; cada resto vuelve a ser áureo. Un trazo curvo une arcos de cuarto de círculo.", "Al quitar un cuadrado a un rectángulo áureo, el resto vuelve a ser áureo. Los arcos aproximan una espiral; no son una espiral matemática exacta."),
      ("prediccion", "Si a = 1, ¿qué ecuación cumple b? Intenta plantearla antes de abrir la respuesta.", "Con a = 1: (1 + b) / 1 = 1 / b, entonces b + b² = 1, es decir b² + b − 1 = 0. La solución positiva es b = (√5 − 1) / 2 ≈ 0,618; la negativa se descarta porque b es una longitud. Además φ = 1 / b.")),
    step("fibonacci", "Fibonacci se acerca a φ", [
      "En la sucesión 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89… cada número es la suma de los dos anteriores.",
      "Si divides un término por el anterior, el cociente se acerca cada vez más a φ: 34 / 21 = 1,6190…; 55 / 34 = 1,6176…"],
      ["mathworld"], None,
      ("calculo", "Calcula 89 / 55 y compáralo con φ.", "89 / 55 = 1,61818… Coincide con φ = 1,61803… en los tres primeros decimales.")),
    step("mito", "Dato y leyenda", [
      "Según MathWorld, las afirmaciones sobre la presencia de φ en el arte y la arquitectura tienden a estar muy exageradas. Se repite, por ejemplo, que el Partenón se diseñó con φ. Encontrar dos medidas cuya razón se acerque a φ no demuestra que el edificio se diseñara usando esa proporción: para sostener esa conclusión también hace falta evidencia sobre el diseño.",
      "Para evaluar una afirmación así hay que preguntar qué medidas se tomaron, entre qué puntos de referencia y con qué incertidumbre."],
      ["mathworld"], None,
      ("explicacion", "Toma un objeto rectangular que tengas a mano (un libro, tu celular, una hoja). Antes de medir, decide qué dos medidas compararás. Luego mide y calcula la razón. ¿Qué cambiaría si eligieras las medidas después de ver el resultado?", "Si eliges los puntos de medición después de buscar una coincidencia, puedes favorecer el resultado que esperabas. Define qué medir antes y anota la incertidumbre de tu regla, por ejemplo ±1 mm.")),
  ],
  [
    q("q1", "¿Cuál es el valor exacto de φ?", [
      ("a", "(1 + √5) / 2", "Correcto: es la solución positiva de φ² = φ + 1."),
      ("b", "1,618 exactamente", "1,618 es una aproximación; φ es irracional y sus decimales no terminan."),
      ("c", "√2", "√2 ≈ 1,414 es otro irracional, pero no es la razón áurea.")], "a", ["mathworld"]),
    q("q2", "En Fibonacci, ¿cuál cociente queda más cerca de φ?", [
      ("a", "8 / 5", "8 / 5 = 1,6: todavía lejos. Los cocientes mejoran con términos más grandes."),
      ("b", "144 / 89", "Correcto: 144 / 89 = 1,61797…, más cerca de φ que los cocientes de términos menores."),
      ("c", "3 / 2", "3 / 2 = 1,5: es uno de los primeros cocientes, el más alejado de los tres.")], "b", ["mathworld"]),
    q("q3", "Un artículo dice que un edificio \"usa φ\". ¿Qué es lo primero que deberías preguntar?", [
      ("a", "Si el arquitecto era famoso", "La fama del autor no dice nada sobre las medidas."),
      ("b", "Qué medidas se tomaron, entre qué puntos y con qué incertidumbre", "Correcto: primero identifica las medidas, los puntos de referencia y la incertidumbre. Una coincidencia numérica, por sí sola, no demuestra intención del arquitecto."),
      ("c", "Si el edificio es bonito", "Que algo se vea armónico no demuestra una proporción concreta.")], "b", ["mathworld"]),
  ],
  [("r1", "Escribe la definición de φ con tus palabras y su valor aproximado.", "El todo es a la parte mayor como la mayor es a la menor; φ ≈ 1,618."),
   ("r2", "¿Qué relación hay entre Fibonacci y φ?", "El cociente entre términos consecutivos se acerca a φ.")],
  "Resume en una frase qué es φ y una razón para desconfiar de los \"φ en todas partes\".",
  [src("mathworld", "Wolfram MathWorld", "Golden Ratio", "https://mathworld.wolfram.com/GoldenRatio.html", "Definición y ecuaciones iniciales; sección sobre Fibonacci (límite de cocientes consecutivos); comentario final sobre afirmaciones exageradas", ["φ = (1 + √5) / 2", "φ es el límite de cocientes consecutivos de Fibonacci", "Las afirmaciones sobre φ en arte y arquitectura tienden a estar muy exageradas"], HOY),
   src("mathworld-rect", "Wolfram MathWorld", "Golden Rectangle", "https://mathworld.wolfram.com/GoldenRectangle.html", "Primer párrafo", ["Al dividir un rectángulo áureo en un cuadrado y un rectángulo, el nuevo rectángulo también es áureo"], HOY),
   src("britannica-aureo", "Encyclopaedia Britannica", "Golden ratio", "https://www.britannica.com/science/golden-ratio", "Párrafo inicial", ["φ es irracional y vale aproximadamente 1,618"], HOY)]))

# ------------------------------------------------------------------ 2
cur = svg("0 0 320 220",
    arrow_def("corriente-humboldt-f1-ah") +
    '<rect width="320" height="220" class="as-svg__surface"/>'
    '<path d="M230 0 C210 60 215 120 235 220" class="as-svg__ink"/>'
    '<text x="275" y="110" text-anchor="middle" class="as-svg__label">Chile</text>'
    '<path d="M170 210 C160 150 165 90 185 20" class="as-svg__ink as-svg__accent" stroke-width="2.5" marker-end="url(#corriente-humboldt-f1-ah)"/>'
    '<path d="M120 210 C110 150 115 90 140 20" class="as-svg__ink as-svg__accent" stroke-width="2.5" marker-end="url(#corriente-humboldt-f1-ah)"/>'
    '<path d="M215 150 L150 150" class="as-svg__muted" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#corriente-humboldt-f1-ah)"/>'
    '<text x="10" y="30" class="as-svg__label" font-size="10">hacia el norte</text>'
    '<text x="10" y="176" class="as-svg__label as-svg__muted" font-size="10">el viento</text>'
    '<text x="10" y="190" class="as-svg__label as-svg__muted" font-size="10">aleja el agua;</text>'
    '<text x="10" y="204" class="as-svg__label as-svg__muted" font-size="10">sube agua fría</text>',
    "Esquema de la corriente de Humboldt y la surgencia costera")
L.append(lesson("corriente-humboldt", "Geografía", "geografia", ["océano", "clima", "Coquimbo"],
  "La corriente de Humboldt y la camanchaca", 13,
  ["Explicar qué es la surgencia costera", "Relacionar el mar frío con la aridez y la niebla costera"],
  "Antes de leer: si la costa está junto al océano, ¿por qué llueve tan poco en el norte de Chile?",
  [
    step("corriente", "Un río frío dentro del mar", [
      "La corriente de Humboldt, también llamada corriente del Perú, es una corriente fría que avanza hacia el norte por la costa occidental de Sudamérica.",
      "El viento empuja el agua superficial mar adentro y desde abajo sube agua más fría para reemplazarla. Ese proceso se llama surgencia."],
      ["britannica-peru", "noaa"],
      fig(cur, "Mapa esquemático: dos flechas suben paralelas a la costa chilena y una flecha punteada sale de la costa hacia el mar.", "Esquema simplificado, sin escala."),
      ("prediccion", "Si el viento deja de soplar varios días, ¿qué esperas que pase con la temperatura del mar en la costa?", "Con menos viento hay menos surgencia: sube menos agua fría y el mar costero tiende a entibiarse.")),
    step("clima", "Mar frío, costa seca y con niebla", [
      "El mar frío enfría el aire que está en contacto con él. Ese aire frío y pesado queda bajo una capa de aire más tibio, que actúa como tapa: es una inversión térmica.",
      "Bajo esa tapa se forman nubes bajas y niebla costera, la camanchaca. Pero el aire no logra subir lo suficiente para producir lluvia, y la costa queda entre las más áridas del mundo."],
      ["britannica-peru"], None,
      ("explicacion", "Explica a otra persona por qué puede haber niebla todas las mañanas y, aun así, casi no llover.", "La niebla se forma bajo la inversión térmica; la lluvia necesitaría que el aire subiera mucho más, y la tapa de aire tibio lo impide.")),
    step("vida", "Agua fría, mar rico", [
      "El agua que sube por surgencia es rica en nutrientes. Funciona como fertilizante para el plancton, y por eso las aguas frente a Perú, Chile y Ecuador están entre las zonas de pesca más ricas del mundo.",
      "Durante un evento El Niño la corriente no es fría como de costumbre, y la pesca se resiente."],
      ["noaa", "britannica-peru"], None,
      ("prediccion", "Durante El Niño, ¿qué le pasa a la pesca de anchoveta y por qué?", "Disminuye: con menos agua fría y menos nutrientes hay menos plancton, que es la base de la cadena alimentaria.")),
  ],
  [
    q("q1", "¿Qué es la surgencia?", [
      ("a", "El ascenso de agua profunda y fría que reemplaza al agua superficial desplazada por el viento", "Correcto: el viento aleja el agua de superficie y sube agua profunda."),
      ("b", "Una ola gigante producida por sismos", "Eso es un tsunami, un fenómeno distinto."),
      ("c", "La llegada de agua dulce de los ríos al mar", "La surgencia viene del fondo del mar, no de los ríos.")], "a", ["noaa"]),
    q("q2", "Un año el mar frente a Coquimbo está más tibio de lo normal. ¿Qué esperas?", [
      ("a", "Más nutrientes y más pesca", "Al revés: el agua tibia indica menos surgencia y menos nutrientes."),
      ("b", "Menos nutrientes y pesca más pobre", "Correcto: es lo que ocurre durante El Niño."),
      ("c", "Ningún cambio", "La temperatura del agua es justamente la señal de que cambió la surgencia.")], "b", ["britannica-peru", "noaa"]),
    q("q3", "¿Por qué la camanchaca casi no produce lluvia?", [
      ("a", "Porque la inversión térmica impide que el aire suba lo suficiente", "Correcto: la tapa de aire tibio frena el ascenso."),
      ("b", "Porque la niebla es de agua salada", "La niebla es de agua dulce condensada; la sal no es el motivo."),
      ("c", "Porque solo aparece de noche", "Aparece sobre todo en la mañana, pero el horario no explica la falta de lluvia.")], "a", ["britannica-peru"]),
  ],
  [("r1", "Explica la surgencia en dos frases.", "El viento empuja el agua de superficie mar adentro; sube agua profunda, fría y rica en nutrientes."),
   ("r2", "¿Qué tienen en común la aridez costera y la camanchaca?", "Ambas se explican por el mar frío y la inversión térmica.")],
  "Anota una cosa del paisaje de la costa de Coquimbo que ahora puedes explicar.",
  [src("noaa", "NOAA National Ocean Service", "What is upwelling?", "https://oceanservice.noaa.gov/facts/upwelling.html", "Texto principal", ["El viento empuja el agua de superficie", "Sube agua fría y rica en nutrientes", "Las buenas zonas de pesca están donde la surgencia es común"], HOY),
   src("britannica-peru", "Encyclopaedia Britannica", "Peru Current", "https://www.britannica.com/place/Peru-Current", "Artículo completo", ["Corriente fría que fluye hacia el norte", "Trae niebla a la costa y contribuye a su aridez", "No es fría durante El Niño", "Aguas de Perú, Chile y Ecuador entre las más ricas en pesca"], HOY)]))

# ------------------------------------------------------------------ 3
import random
random.seed(7)
stars = "".join(f'<circle cx="{(i*73)%320}" cy="{(i*37)%90}" r="{1.6 if i%3==0 else 1}" class="as-svg__accent"/>' for i in range(40))
sky = svg("0 0 320 200",
    '<rect width="320" height="200" class="as-svg__surface"/>' + stars +
    '<path d="M0 200 L70 120 L110 150 L170 85 L230 140 L270 110 L320 160 L320 200Z" class="as-svg__ink"/>'
    '<rect y="150" width="320" height="22" class="as-svg__muted" stroke-dasharray="3 3"/>'
    '<circle cx="170" cy="82" r="5" class="as-svg__accent"/>'
    '<text x="180" y="78" class="as-svg__label" font-size="11">observatorio</text>'
    '<text x="10" y="166" class="as-svg__label as-svg__muted" font-size="11">capa de nubes bajas</text>',
    "Cumbres de cerros sobre una capa de nubes bajas, bajo un cielo estrellado")
L.append(lesson("cielos-coquimbo", "Astronomía", "astronomia", ["observatorios", "Coquimbo", "cielo nocturno"],
  "Por qué el norte de Chile mira al universo", 14,
  ["Identificar las condiciones que hacen bueno un sitio astronómico", "Ubicar observatorios de la Región de Coquimbo"],
  "Antes de leer: ¿qué necesitarías para ver estrellas muy débiles? Haz una lista de tres condiciones.",
  [
    step("condiciones", "Tres condiciones", [
      "Un buen sitio astronómico necesita muchas noches despejadas, aire seco y estable, y cielos oscuros, lejos de la contaminación lumínica.",
      "En el norte de Chile las nubes bajas de la costa suelen quedar bajo la inversión térmica; las cumbres de los cerros quedan por encima de ellas."],
      ["eso-lasilla"],
      fig(sky, "Silueta de cerros con un observatorio en la cumbre, sobre una franja de nubes bajas.", "Esquema sin escala: las cumbres sobresalen de la capa de nubes bajas."),
      ("prediccion", "¿Por qué crees que un observatorio prefiere estar en una cumbre y no en la costa?", "En la cumbre queda sobre las nubes bajas, con menos aire encima y menos humedad.")),
    step("cerros", "Los cerros de la región", [
      "La Silla, del Observatorio Europeo Austral (ESO), está a unos 2.400 metros de altitud y a unos 600 km al norte de Santiago. ESO lo describe como uno de los cielos nocturnos más oscuros de la Tierra.",
      "En la comuna de Vicuña están Cerro Tololo y Cerro Pachón, donde operan instalaciones de NOIRLab como el Observatorio Interamericano de Cerro Tololo, Gemini Sur y SOAR. En la cumbre de Cerro Pachón está el Observatorio Vera C. Rubin, que hará un sondeo del cielo nocturno durante diez años."],
      ["eso-lasilla", "noirlab-chile", "rubin"], None,
      ("explicacion", "Explica a otra persona por qué una ciudad que crece cerca de un observatorio es un problema.", "Su iluminación aclara el cielo y reduce el contraste; los objetos débiles dejan de verse.")),
    step("proteger", "Proteger la oscuridad", [
      "El D.S. N° 1/2022 del Ministerio del Medio Ambiente, norma de emisión de luminosidad artificial generada por alumbrados de exteriores, se publicó en el Diario Oficial el 18 de octubre de 2023. Protege tres objetivos: la observación astronómica, la biodiversidad y la salud.",
      "Desde el hemisferio sur, en una noche oscura, se puede observar la Gran Nube de Magallanes, una galaxia satélite de la Vía Láctea."],
      ["mma-luminica", "eso-lmc"], None,
      ("prediccion", "¿Por qué un astrónomo prefiere noches sin luna?", "La luz de la Luna ilumina la atmósfera y reduce el contraste, ocultando objetos débiles como galaxias y nebulosas.")),
  ],
  [
    q("q1", "¿Cuál de estas condiciones NO favorece la observación astronómica?", [
      ("a", "Aire seco", "El aire seco sí favorece: hay menos vapor que absorba luz."),
      ("b", "Contaminación lumínica", "Correcto: la luz artificial aclara el cielo y tapa los objetos débiles."),
      ("c", "Altura", "La altura sí favorece: hay menos atmósfera encima.")], "b", ["eso-lasilla"]),
    q("q2", "Una empresa quiere instalar un gran letrero luminoso en un cerro del Valle de Elqui. ¿Qué norma chilena es pertinente?", [
      ("a", "El D.S. N° 1/2022 del Ministerio del Medio Ambiente, sobre luminosidad artificial de alumbrados de exteriores", "Correcto: regula la luz que emiten los alumbrados de exteriores para proteger, entre otros objetivos, la observación astronómica."),
      ("b", "El Código del Trabajo", "Regula relaciones laborales, no la iluminación."),
      ("c", "Ninguna; la iluminación no está regulada", "Sí existe una norma específica.")], "a", ["mma-luminica"]),
    q("q3", "¿Qué es la Gran Nube de Magallanes?", [
      ("a", "Una nube de tormenta del extremo sur", "Su nombre confunde: no es una nube atmosférica."),
      ("b", "Una galaxia satélite de la Vía Láctea", "Correcto: es visible desde el hemisferio sur."),
      ("c", "Un cometa que vuelve cada año", "No es un cometa: es una galaxia, mucho más lejana que cualquier cometa.")], "b", ["eso-lmc"]),
  ],
  [("r1", "Nombra las tres condiciones de un buen sitio astronómico.", "Noches despejadas, aire seco y estable, cielo oscuro."),
   ("r2", "Nombra dos cerros con observatorios en la Región de Coquimbo.", "La Silla, Cerro Tololo o Cerro Pachón.")],
  "La próxima noche despejada, apaga las luces del patio cinco minutos y anota cuántas estrellas más ves.",
  [src("eso-lasilla", "European Southern Observatory", "La Silla", "https://www.eso.org/public/teles-instr/lasilla/", "Página del observatorio, párrafo inicial", ["Altitud de 2.400 m", "A unos 600 km al norte de Santiago", "Uno de los cielos nocturnos más oscuros de la Tierra"], HOY),
   src("rubin", "U.S. National Science Foundation", "NSF–DOE Vera C. Rubin Observatory", "https://www.nsf.gov/focus-areas/astronomy-space/rubin-observatory", "Párrafo inicial", ["El Observatorio Rubin está en la cumbre de Cerro Pachón, Chile", "Hará el Legacy Survey of Space and Time, un sondeo del cielo nocturno de diez años"], HOY),
   src("noirlab-chile", "NSF NOIRLab", "NOIRLab and Chile", "https://noirlab.edu/public/about/broader-impacts/chile", "Sección sobre las instalaciones en Chile", ["Cerro Tololo y Cerro Pachón están en Vicuña", "Instalaciones en Chile: CTIO, Gemini Sur, SOAR y Rubin"], HOY),
   src("mma-luminica", "Ministerio del Medio Ambiente", "Nueva Norma Lumínica (presentación)", "https://luminica.mma.gob.cl/wp-content/uploads/2024/09/01-Nueva-Norma-Luminica.pdf", "Portada y secciones de objetivos y vigencia", ["D.S. N° 1/2022 MMA, Norma de Emisión de Luminosidad Artificial Generada por Alumbrados de Exteriores", "Publicada en el Diario Oficial el 18-10-2023", "Objetivos: observación astronómica, biodiversidad y salud"], HOY),
   src("eso-lmc", "European Southern Observatory", "Large Magellanic Cloud (imagen)", "https://eso.org/public/images/magellan-ch17-bardon-cc", "Descripción de la imagen", ["La Gran Nube de Magallanes es una galaxia satélite de la Vía Láctea visible desde el hemisferio sur"], HOY)]))

# ------------------------------------------------------------------ 4
tipo = svg("0 0 240 180",
    '<rect x="70" y="30" width="100" height="130" class="as-svg__surface"/>'
    '<rect x="70" y="30" width="100" height="130" class="as-svg__ink"/>'
    '<rect x="70" y="10" width="100" height="22" class="as-svg__ink"/>'
    '<text x="120" y="28" text-anchor="middle" transform="translate(240 0) scale(-1 1)" class="as-svg__label as-svg__accent" font-size="22">R</text>'
    '<text x="120" y="100" text-anchor="middle" class="as-svg__label" font-size="11">cuerpo de metal</text>'
    '<text x="178" y="25" class="as-svg__label as-svg__muted" font-size="11">relieve</text>',
    "Un tipo móvil con la letra R en relieve e invertida")
L.append(lesson("imprenta-gutenberg", "Historia", "historia", ["imprenta", "Renacimiento", "tecnología"],
  "La imprenta de tipos móviles", 12,
  ["Describir los componentes del sistema de Gutenberg", "Explicar por qué abarató la copia de textos"],
  "Antes de leer: ¿cómo se copiaba un libro antes de la imprenta, y cuánto crees que tardaba?",
  [
    step("sistema", "Un sistema completo", [
      "Johannes Gutenberg, nacido y fallecido en Maguncia (Alemania), combinó varias técnicas en un sistema para imprimir con letras de metal reutilizables.",
      "El sistema incluía una aleación de metal duradera para fundir los tipos, una tinta de base oleosa y una prensa que aplicaba presión pareja sobre el papel."],
      ["britannica-gutenberg"],
      fig(tipo, "Bloque rectangular de metal con una letra R invertida en relieve en su extremo superior.", "La letra va invertida para que al imprimir quede al derecho."),
      ("prediccion", "¿Por qué la letra del tipo va al revés?", "Porque al presionar contra el papel la imagen se invierte; así queda legible.")),
    step("biblia", "La Biblia de 42 líneas", [
      "Su obra más conocida es la Biblia de 42 líneas, impresa en latín en columnas de 42 líneas y terminada hacia 1455 en Maguncia. Se conservan unos 40 ejemplares; no se sabe cuántos se imprimieron."],
      ["britannica-biblia"], None,
      ("calculo", "Si un copista escribía 3 páginas al día, ¿cuántos días tardaría en copiar una obra de 1.280 páginas?", "1.280 / 3 = 426,67 días, es decir, unos 427 días de trabajo para una sola copia.")),
    step("efectos", "Consecuencias", [
      "Con la imprenta, todas las copias de una edición decían exactamente lo mismo y producir una copia más costaba mucho menos que copiarla a mano.",
      "Eso facilitó la circulación de textos científicos, religiosos y políticos en Europa durante las décadas siguientes."],
      ["pendiente-efectos"], None,
      ("explicacion", "Compara la imprenta con internet: ¿qué abarataron ambos y qué problema común traen?", "Ambos abarataron copiar y distribuir textos; ambos facilitan también la difusión de información falsa.")),
  ],
  [
    q("q1", "¿Cuál de estos elementos formaba parte del sistema de Gutenberg?", [
      ("a", "Una tinta de base oleosa", "Correcto: necesitaba una tinta que se adhiriera al metal."),
      ("b", "Una máquina a vapor", "La máquina a vapor llegó siglos después."),
      ("c", "Papel de celulosa industrial", "El papel industrial moderno es muy posterior.")], "a", ["britannica-gutenberg"]),
    q("q2", "Un taller imprime 200 copias de un folleto. ¿Qué ventaja tiene sobre 200 copias manuscritas?", [
      ("a", "Son todas idénticas", "Correcto: las copias impresas no acumulan errores de copista."),
      ("b", "Duran más años", "La duración depende del papel y la tinta, no del método."),
      ("c", "Son más bonitas", "Hay manuscritos bellísimos; la ventaja clave es la uniformidad y el costo.")], "a", ["pendiente-efectos"]),
    q("q3", "¿Por qué la letra del tipo móvil está invertida?", [
      ("a", "Por tradición de los copistas", "No es una tradición: es una necesidad física."),
      ("b", "Para que al imprimir quede al derecho", "Correcto: la impresión invierte la imagen."),
      ("c", "Para ahorrar metal", "La orientación no cambia la cantidad de metal.")], "b", ["britannica-gutenberg"]),
  ],
  [("r1", "Nombra tres componentes del sistema de Gutenberg.", "Tipos de una aleación metálica, tinta oleosa y prensa."),
   ("r2", "¿Qué ventaja principal tiene una copia impresa frente a una manuscrita?", "Todas las copias son iguales y cada copia adicional cuesta mucho menos.")],
  "Piensa en un documento de tu trabajo que dependa de que todas las copias sean idénticas.",
  [src("britannica-gutenberg", "Encyclopaedia Britannica", "Johannes Gutenberg", "https://www.britannica.com/biography/Johannes-Gutenberg", "Resumen inicial y sección sobre la invención", ["Nació y murió en Maguncia", "Aleación metálica duradera, tinta oleosa y prensa de presión pareja"], HOY),
   src("britannica-biblia", "Encyclopaedia Britannica", "Gutenberg Bible", "https://www.britannica.com/topic/Gutenberg-Bible", "Artículo principal", ["Completada hacia 1455 en Maguncia", "Impresa en columnas de 42 líneas", "Se conservan unos 40 ejemplares; se desconoce el número impreso"], HOY),
   src("pendiente-efectos", "Por definir", "Fuente sobre efectos de la imprenta", "https://www.britannica.com/technology/printing-publishing", "Pendiente de localizar", ["La imprenta uniformó las copias y abarató la reproducción de textos"], None)]))

# ------------------------------------------------------------------ 5
lines = "".join(f'<line x1="{x}" y1="{80-(160-x)*0.375:.1f}" x2="{x}" y2="{80+(160-x)*0.75:.1f}" class="as-svg__muted"/>'
                f'<line x1="{320-x}" y1="{80-(160-x)*0.375:.1f}" x2="{320-x}" y2="{80+(160-x)*0.75:.1f}" class="as-svg__muted"/>' for x in (40, 80, 115, 140))
persp = svg("0 0 320 200",
    '<rect width="320" height="200" class="as-svg__surface"/>'
    '<line x1="0" y1="80" x2="320" y2="80" class="as-svg__muted" stroke-dasharray="4 4"/>'
    '<line x1="160" y1="80" x2="0" y2="200" class="as-svg__ink"/><line x1="160" y1="80" x2="320" y2="200" class="as-svg__ink"/>'
    '<line x1="160" y1="80" x2="0" y2="20" class="as-svg__ink"/><line x1="160" y1="80" x2="320" y2="20" class="as-svg__ink"/>' + lines +
    '<circle cx="160" cy="80" r="4" class="as-svg__accent"/>'
    '<text x="160" y="56" text-anchor="middle" class="as-svg__label as-svg__accent" font-size="10">punto de fuga</text>',
    "Calle en perspectiva con un punto de fuga")
L.append(lesson("perspectiva-lineal", "Arte", "arte", ["Renacimiento", "geometría", "dibujo"],
  "La perspectiva lineal", 11,
  ["Ubicar el punto de fuga y la línea de horizonte en una imagen", "Explicar el origen renacentista del método"],
  "Antes de leer: mira un pasillo largo. ¿Qué le pasa al ancho del pasillo a medida que se aleja?",
  [
    step("fuga", "El punto de fuga", [
      "En la perspectiva lineal, las líneas paralelas que se alejan del observador convergen en un único punto de fuga situado sobre la línea del horizonte.",
      "La línea del horizonte de una imagen está a la altura de los ojos de quien mira."],
      ["britannica-persp"],
      fig(persp, "Cuatro líneas que parten de las esquinas convergen en un punto central sobre una línea horizontal punteada; líneas verticales representan fachadas que se achican.", "La línea punteada es el horizonte; las paralelas convergen en el punto de fuga."),
      ("prediccion", "Si el fotógrafo se agacha, ¿dónde queda la línea del horizonte en la foto?", "Más abajo: el horizonte siempre queda a la altura de la cámara u ojo.")),
    step("origen", "Florencia, siglo XV", [
      "Se considera que el sistema fue ideado hacia 1415 y se atribuye a Filippo Brunelleschi.",
      "En 1435, Leon Battista Alberti documentó el método en su tratado sobre la pintura (Della pittura en su versión italiana)."],
      ["britannica-persp"], None,
      ("explicacion", "Toma una foto de una calle recta y prolonga sus bordes con una regla. ¿Dónde se cruzan?", "En un punto sobre la línea del horizonte, a la altura de la cámara.")),
    step("atmosfera", "Más allá de la regla", [
      "Los pintores combinan la perspectiva lineal con la perspectiva atmosférica: a gran distancia los contrastes entre luz y sombra son menos marcados, los colores oscuros tienden al azul y los bordes se ven menos nítidos. Por eso las montañas lejanas se ven azuladas."],
      ["britannica-aerea"], None,
      ("prediccion", "En una foto del Valle de Elqui, ¿qué cerros se ven más azulados: los cercanos o los lejanos?", "Los lejanos: entre ellos y la cámara hay más aire que dispersa la luz.")),
  ],
  [
    q("q1", "En perspectiva lineal, ¿dónde convergen las líneas paralelas que se alejan?", [
      ("a", "En el punto de fuga, sobre el horizonte", "Correcto."),
      ("b", "En el borde inferior del cuadro", "Se acercan entre sí a medida que se alejan, hacia el horizonte, no hacia abajo."),
      ("c", "Siempre en el centro exacto del cuadro", "El punto de fuga puede estar en cualquier lugar del horizonte.")], "a", ["britannica-persp"]),
    q("q2", "Dibujas una línea férrea recta vista desde el andén. ¿Qué haces con los rieles?", [
      ("a", "Los dibujo paralelos", "Así no se percibe profundidad."),
      ("b", "Los hago converger hacia un punto del horizonte", "Correcto: es el principio de la perspectiva lineal."),
      ("c", "Los separo a medida que se alejan", "Eso invierte el efecto de la distancia.")], "b", ["britannica-persp"]),
    q("q3", "¿Quién documentó por escrito el método en 1435?", [
      ("a", "Leon Battista Alberti", "Correcto."),
      ("b", "Filippo Brunelleschi", "A Brunelleschi se le atribuye haberlo ideado hacia 1415; el tratado de 1435 es de Alberti."),
      ("c", "Leonardo da Vinci", "Leonardo nació en 1452, después del tratado.")], "a", ["britannica-persp"]),
  ],
  [("r1", "¿Qué es el punto de fuga?", "El punto del horizonte donde parecen converger las paralelas que se alejan."),
   ("r2", "¿A qué altura está la línea del horizonte en una imagen?", "A la altura de los ojos del observador o de la cámara.")],
  "Busca en tu celular una foto con un punto de fuga claro y márcalo con el dedo.",
  [src("britannica-persp", "Encyclopaedia Britannica", "Linear perspective", "https://www.britannica.com/art/linear-perspective", "Párrafo inicial", ["Paralelas convergen en un único punto de fuga sobre el horizonte", "Ideado hacia 1415, atribuido a Brunelleschi", "Documentado por Alberti en 1435 (Della pittura)"], HOY),
   src("britannica-aerea", "Encyclopaedia Britannica", "Aerial perspective", "https://www.britannica.com/art/aerial-perspective", "Definición y párrafo siguiente", ["Contrastes de luz y sombra menos extremos a gran distancia", "Los colores oscuros lejanos tienden al azul; montañas lejanas azuladas", "Bordes y contornos menos nítidos"], HOY)]))

# ------------------------------------------------------------------ 6
bau = svg("0 0 330 120",
    '<polygon points="50,105 95,15 140,105" class="as-svg__accent"/>'
    '<rect x="160" y="20" width="85" height="85" class="as-svg__ink" stroke-width="3"/>'
    '<circle cx="292" cy="62" r="30" class="as-svg__muted" stroke-width="3"/>',
    "Triángulo, cuadrado y círculo, formas básicas del curso preliminar")
L.append(lesson("bauhaus", "Diseño", "arte", ["diseño", "siglo XX", "retícula"],
  "La Bauhaus y la forma útil", 12,
  ["Ubicar la Bauhaus en el tiempo y sus sedes", "Reconocer la retícula en interfaces actuales"],
  "Antes de leer: piensa en una silla que te parezca \"moderna\". ¿Qué tiene y qué no tiene?",
  [
    step("escuela", "Arte y oficio juntos", [
      "La Bauhaus fue una escuela alemana de diseño fundada en 1919 en Weimar por el arquitecto Walter Gropius. Se trasladó a Dessau y luego a Berlín, donde cerró en 1933 bajo la presión del régimen nazi.",
      "Su idea central fue unir artes y oficios y diseñar objetos pensados para la producción industrial."],
      ["pendiente-bauhaus"],
      fig(bau, "Un triángulo relleno, un cuadrado y un círculo dibujados con trazo grueso.", "Formas básicas, ejercicio típico del curso preliminar."),
      ("prediccion", "¿Por qué una escuela de diseño empezaría con triángulos, cuadrados y círculos?", "Son las formas mínimas; dominarlas permite componer cualquier objeto sin depender del adorno.")),
    step("reticula", "La retícula", [
      "Ordenar una página o una pantalla con una grilla invisible da coherencia: cada elemento se alinea con algo.",
      "Esa disciplina, desarrollada después por el diseño gráfico del siglo XX, está detrás de la mayoría de las aplicaciones y sitios web actuales."],
      ["pendiente-reticula"], None,
      ("explicacion", "Abre la app de tu banco o de correo. Señala dos márgenes o columnas que se repitan.", "Casi siempre hay márgenes laterales iguales, íconos del mismo tamaño y textos alineados a una misma línea.")),
    step("legado", "El legado", [
      "Muebles de tubo de acero, tipografías sin serifa y edificios de volúmenes simples con grandes ventanales son herencias asociadas a la Bauhaus.",
      "La lección práctica: antes de decorar, pregunta para qué sirve cada elemento."],
      ["pendiente-bauhaus"], None,
      ("explicacion", "Elige un objeto de tu escritorio y nombra un elemento que sobra y uno que no puede faltar.", "La respuesta es personal; lo importante es justificar cada elemento por su función.")),
  ],
  [
    q("q1", "¿En qué ciudad se fundó la Bauhaus?", [
      ("a", "Weimar", "Correcto: en 1919."),
      ("b", "Dessau", "Dessau fue su segunda sede."),
      ("c", "París", "La Bauhaus fue una escuela alemana.")], "a", ["pendiente-bauhaus"]),
    q("q2", "Diseñas una planilla de rendiciones. ¿Qué principio de la Bauhaus aplicas?", [
      ("a", "Agregar adornos para que se vea profesional", "Es lo contrario del principio de la forma útil."),
      ("b", "Alinear columnas en una retícula y quitar lo que no cumple función", "Correcto."),
      ("c", "Usar muchos colores distintos", "El color sin función agrega ruido.")], "b", ["pendiente-reticula"]),
    q("q3", "¿Por qué cerró la Bauhaus en 1933?", [
      ("a", "Por falta de alumnos", "No fue esa la causa."),
      ("b", "Por la presión del régimen nazi", "Correcto."),
      ("c", "Porque Gropius se jubiló", "Gropius había dejado la dirección antes, pero no fue la causa del cierre.")], "b", ["pendiente-bauhaus"]),
  ],
  [("r1", "Nombra las tres sedes de la Bauhaus en orden.", "Weimar, Dessau y Berlín."),
   ("r2", "¿Qué es una retícula en diseño?", "Una grilla invisible que ordena y alinea los elementos.")],
  "Revisa un documento tuyo y alinea todo a dos márgenes comunes.",
  [src("pendiente-bauhaus", "Encyclopaedia Britannica", "Bauhaus", "https://www.britannica.com/topic/Bauhaus-German-school-of-design", "Pendiente de localizar (la consulta falló el 2026-10-19)", ["Fundada en 1919 en Weimar por Walter Gropius", "Sedes posteriores en Dessau y Berlín", "Cerró en 1933 bajo presión del régimen nazi", "Buscaba unir artes y oficios y diseñar para la industria"], None),
   src("pendiente-reticula", "Por definir", "Fuente sobre la retícula tipográfica", "https://www.britannica.com/topic/graphic-design", "Pendiente de localizar", ["La retícula ordena y alinea elementos en páginas e interfaces"], None)]))

# ------------------------------------------------------------------ 7
dov = ""
for i in range(9):
    a1 = math.pi - i*math.pi/9; a2 = math.pi - (i+1)*math.pi/9
    R, r, cx, cy = 110, 75, 160, 180
    pts = [(cx+R*math.cos(a1), cy-R*math.sin(a1)), (cx+R*math.cos(a2), cy-R*math.sin(a2)), (cx+r*math.cos(a2), cy-r*math.sin(a2)), (cx+r*math.cos(a1), cy-r*math.sin(a1))]
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    dov += f'<polygon points="{p}" class="{"as-svg__accent" if i == 4 else "as-svg__surface"}"/><polygon points="{p}" class="as-svg__ink"/>'
arch = svg("0 0 320 200",
    arrow_def("arco-panteon-f1-ah") + dov +
    '<line x1="45" y1="175" x2="15" y2="175" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#arco-panteon-f1-ah)"/>'
    '<line x1="275" y1="175" x2="305" y2="175" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#arco-panteon-f1-ah)"/>'
    '<text x="160" y="58" text-anchor="middle" class="as-svg__label as-svg__accent" font-size="11">clave</text>'
    '<text x="160" y="196" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">empuje lateral</text>',
    "Arco de medio punto formado por nueve dovelas")
L.append(lesson("arco-panteon", "Arquitectura", "arte", ["Roma", "estructuras", "hormigón"],
  "El arco, la bóveda y el Panteón", 14,
  ["Explicar por qué un arco de piedra trabaja a compresión", "Describir cómo se aligeró la cúpula del Panteón"],
  "Antes de leer: ¿por qué un puente de piedra antiguo puede seguir en pie después de 2.000 años?",
  [
    step("compresion", "El arco trabaja a compresión", [
      "Las piedras de un arco, llamadas dovelas, se empujan unas a otras. La piedra resiste muy bien la compresión, aunque se quiebra con facilidad si se la dobla.",
      "La dovela central superior se llama clave. El arco empuja hacia los lados, y ese empuje debe contenerse con muros o contrafuertes."],
      ["britannica-arco", "pendiente-arco"],
      fig(arch, "Nueve bloques en forma de cuña forman un semicírculo; el bloque central está destacado; dos flechas en la base apuntan hacia afuera.", "Arco de medio punto: dovelas, clave y empuje lateral."),
      ("prediccion", "¿Qué pasa si quitas el muro que contiene el empuje lateral de un arco?", "Los apoyos se abren hacia afuera y el arco colapsa.")),
    step("cupula", "Del arco a la cúpula", [
      "Si giras un arco sobre su eje vertical obtienes una cúpula. El Panteón de Roma fue reconstruido por completo durante el reinado de Adriano (117–138 d. C.); los sellos de sus ladrillos datan la mayor parte de la obra a comienzos de la década de 120. Su cúpula de hormigón, sin acero, tiene una luz interior de 43,2 metros.",
      "La altura interior es igual a esa luz: cabría una esfera completa."],
      ["uw-panteon"], None,
      ("calculo", "Si la luz interior es 43,2 m, ¿qué volumen tendría la esfera que cabe en el interior?", "V = (4/3) × π × r³ con r = 21,6 m: (4/3) × 3,1416 × 10.077,696 = 42.213,5 m³ (cálculo con π = 3,1416, redondeado a un decimal).")),
    step("trucos", "Cómo se aligeró", [
      "En la base se usó basalto, pesado, y arriba piedra pómez, liviana. Por fuera, la cúpula sube en escalones concéntricos.",
      "En la cima, el óculo de 8,2 metros es la única fuente de luz del interior. Los casetones del cielo de la cúpula se asocian también con la reducción de peso."],
      ["uw-panteon", "pendiente-casetones"], None,
      ("explicacion", "Explica por qué conviene que lo más liviano esté arriba.", "Cada parte de la cúpula carga con todo lo que está encima; si arriba pesa menos, abajo hay menos esfuerzo.")),
  ],
  [
    q("q1", "¿A qué esfuerzo trabaja principalmente un arco de piedra?", [
      ("a", "Compresión", "Correcto: las dovelas se empujan unas a otras."),
      ("b", "Tracción", "La piedra resiste mal la tracción; el arco está diseñado para evitarla."),
      ("c", "Torsión", "Un arco bien cargado no trabaja a torsión.")], "a", ["pendiente-arco"]),
    q("q2", "Debes reforzar un muro antiguo que sostiene un arco. ¿Qué empuje debes contener?", [
      ("a", "El empuje lateral hacia afuera", "Correcto: el arco tiende a abrir sus apoyos."),
      ("b", "Un empuje hacia arriba", "El peso del arco empuja hacia abajo y hacia los lados, no hacia arriba."),
      ("c", "Ninguno; el arco se sostiene solo", "Sin apoyos que contengan el empuje, el arco se abre.")], "a", ["pendiente-arco"]),
    q("q3", "¿Qué material se usó en la parte alta de la cúpula del Panteón para aligerarla?", [
      ("a", "Basalto", "El basalto, pesado, se usó en la base."),
      ("b", "Piedra pómez", "Correcto: es liviana y se usó arriba."),
      ("c", "Acero", "El Panteón es de hormigón, sin acero.")], "b", ["uw-panteon"]),
  ],
  [("r1", "¿Qué es la clave de un arco?", "La dovela central superior del arco."),
   ("r2", "Nombra dos recursos con que se aligeró la cúpula del Panteón.", "Piedra pómez arriba y basalto en la base, escalones concéntricos y óculo.")],
  "Busca un arco en un edificio de tu ciudad e identifica dónde está su clave.",
  [src("britannica-arco", "Encyclopaedia Britannica", "Arch (architecture)", "https://britannica.com/technology/arch-architecture", "Resumen y pies de los diagramas", ["La construcción del arco depende de la cuña", "Dovelas en forma de cuña forman la curva; la clave está arriba al centro", "Las fuerzas de compresión recorren la estructura"], HOY),
   src("pendiente-arco", "Por definir", "Fuente sobre el empuje lateral de los arcos", "https://britannica.com/technology/arch-architecture", "Pendiente de localizar", ["El arco produce empuje lateral que deben contener muros o contrafuertes"], None),
   src("uw-panteon", "University of Washington, Honors Program in Rome", "The Pantheon", "https://depts.washington.edu/hrome/Authors/zinnia/Pantheon/pub_zbarticle_view_printable.html", "Artículo completo (autor: zinnia, 09-04-2005)", ["Reconstruido por completo bajo Adriano (117–138); sellos de ladrillos de comienzos de la década de 120", "Luz interior de 43,2 m; altura igual a la luz", "Óculo de 8,2 m, única fuente de luz", "Basalto en la base y piedra pómez arriba", "Íntegramente de hormigón, sin acero"], HOY),
   src("pendiente-casetones", "Por definir", "Fuente sobre la función de los casetones", "https://www.britannica.com/topic/Pantheon-building-Rome", "Pendiente de localizar", ["Los casetones reducen el peso de la cúpula"], None)]))

# ------------------------------------------------------------------ 8 (ejemplo de ChatGPT, corregido)
def moon(cx, cy, lit_side):  # lit_side: 'right','left','full','new'
    base = f'<circle cx="{cx}" cy="{cy}" r="14" class="as-svg__ink"/>'
    if lit_side == "full":
        return f'<circle cx="{cx}" cy="{cy}" r="14" class="as-svg__accent"/>' + base
    if lit_side == "new":
        return base
    sweep = 1 if lit_side == "right" else 0
    return f'<path d="M{cx} {cy-14} A14 14 0 0 {sweep} {cx} {cy+14} Z" class="as-svg__accent"/>' + base
orbit = svg("0 0 340 220",
    arrow_def("fases-lunares-f1-ah") +
    '<text x="8" y="20" class="as-svg__label" font-size="11">Luz solar</text>'
    '<line x1="8" y1="30" x2="60" y2="30" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#fases-lunares-f1-ah)"/>'
    '<line x1="8" y1="190" x2="60" y2="190" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#fases-lunares-f1-ah)"/>'
    '<circle cx="170" cy="110" r="70" class="as-svg__muted" stroke-dasharray="4 4"/>'
    '<circle cx="170" cy="110" r="22" class="as-svg__surface"/><circle cx="170" cy="110" r="22" class="as-svg__ink"/>'
    '<text x="170" y="114" text-anchor="middle" class="as-svg__label" font-size="10">Tierra</text>'
    # posiciones: izquierda (hacia el Sol) nueva, abajo, derecha llena, arriba
    + f'<circle cx="100" cy="110" r="14" class="as-svg__surface"/><path d="M100 96 A14 14 0 0 0 100 124 Z" class="as-svg__accent"/><circle cx="100" cy="110" r="14" class="as-svg__ink"/>'
    + f'<circle cx="240" cy="110" r="14" class="as-svg__surface"/><path d="M240 96 A14 14 0 0 0 240 124 Z" class="as-svg__accent"/><circle cx="240" cy="110" r="14" class="as-svg__ink"/>'
    + f'<circle cx="170" cy="40" r="14" class="as-svg__surface"/><path d="M170 26 A14 14 0 0 0 170 54 Z" class="as-svg__accent"/><circle cx="170" cy="40" r="14" class="as-svg__ink"/>'
    + f'<circle cx="170" cy="180" r="14" class="as-svg__surface"/><path d="M170 166 A14 14 0 0 0 170 194 Z" class="as-svg__accent"/><circle cx="170" cy="180" r="14" class="as-svg__ink"/>'
    '<text x="100" y="140" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">nueva</text>'
    '<text x="240" y="140" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">llena</text>'
    '<text x="200" y="44" class="as-svg__label as-svg__muted" font-size="10">cuarto</text>'
    '<text x="200" y="184" class="as-svg__label as-svg__muted" font-size="10">cuarto</text>',
    "Órbita de la Luna con cuatro posiciones, siempre iluminada desde la izquierda")
seen = svg("0 0 360 80",
    moon(40, 40, "new") + moon(130, 40, "left") + moon(220, 40, "full") + moon(310, 40, "right") +
    '<text x="40" y="74" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">nueva</text>'
    '<text x="130" y="74" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">cuarto creciente</text>'
    '<text x="220" y="74" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">llena</text>'
    '<text x="310" y="74" text-anchor="middle" class="as-svg__label as-svg__muted" font-size="10">cuarto menguante</text>',
    "Cuatro fases de la Luna vistas desde la Tierra")
L.append(lesson("fases-lunares", "Astronomía", "astronomia", ["Luna", "luz", "geometría"],
  "¿Quién cambia la cara de la Luna?", 12,
  ["Explicar las fases usando un modelo", "Distinguir una fase de un eclipse"],
  "Antes de leer: ¿qué crees que produce las fases de la Luna?",
  [
    step("luz", "La mitad que ilumina el Sol", [
      "Salvo durante los eclipses lunares, el Sol ilumina aproximadamente la mitad de la superficie lunar. La otra mitad no recibe luz solar directa.",
      "En el esquema, la luz llega desde la izquierda: en las cuatro posiciones de la órbita, la mitad iluminada mira al Sol."],
      ["nasa-fases", "nasa-eclipses"],
      fig(orbit, "Tierra al centro y la Luna en cuatro posiciones sobre su órbita circular; en todas, la mitad izquierda de la Luna está iluminada.", "Vista desde arriba, sin escala y sin eclipses. La mitad iluminada mira al Sol."),
      ("prediccion", "En la posición de la derecha, ¿qué parte de la mitad iluminada ve alguien en la Tierra?", "Toda: la mitad iluminada mira hacia la Tierra. Es la Luna llena.")),
    step("modelo", "Cambia el punto de vista", [
      "Lo que cambia mientras la Luna orbita es cuánto de esa mitad iluminada vemos desde la Tierra. El ciclo completo se repite cada unos 29,5 días.",
      "NASA nombra ocho fases: nueva, luna creciente, cuarto creciente, gibosa creciente, llena, gibosa menguante, cuarto menguante y luna menguante."],
      ["nasa-fases", "ou-hemisferio"],
      fig(seen, "Cuatro círculos: uno vacío, uno con la mitad izquierda clara, uno completamente claro y uno con la mitad derecha clara.", "Orientación esquemática para el hemisferio sur. La inclinación aparente cambia según el lugar y el momento de observación."),
      ("explicacion", "En una habitación con luz tenue, deja una linterna fija. Sostén una pelota con el brazo estirado, algo por encima de tu cabeza para no taparla con la sombra de tu cuerpo, y gira lentamente en el lugar. Dibuja cuatro vistas.", "Aproximadamente la mitad de la pelota sigue iluminada; cambia cuánto de ella ves. Si la pelota entra en la sombra de tu cabeza, acabas de simular un eclipse, no una fase.")),
    step("eclipse", "La sombra terrestre es otro fenómeno", [
      "La órbita de la Luna está inclinada unos 5 grados respecto de la órbita de la Tierra. Por eso, cuando pasa entre nosotros y el Sol, vista desde la Tierra suele pasar arriba o abajo del Sol. Las fases no se deben a la sombra de la Tierra.",
      "Cuando la Tierra queda exactamente entre el Sol y la Luna, su sombra cae sobre la superficie lunar: es un eclipse lunar, que ocurre en fase de Luna llena."],
      ["nasa-eclipses"], None,
      ("explicacion", "Explica a otra persona la diferencia entre una Luna menguante y un eclipse lunar.", "La menguante es parte del ciclo de iluminación visto desde la Tierra; el eclipse ocurre cuando la sombra de la Tierra cae sobre la Luna.")),
  ],
  [
    q("q1", "¿Qué explica las fases de la Luna?", [
      ("a", "La porción de la mitad iluminada que vemos desde la Tierra", "Correcto: cambia con la posición de la Luna en su órbita."),
      ("b", "La sombra de la Tierra", "La sombra terrestre produce eclipses, no las fases."),
      ("c", "Cambios en el tamaño de la Luna", "Las variaciones de tamaño aparente no explican las fases.")], "a", ["nasa-fases", "nasa-eclipses"]),
    q("q2", "Hoy hay Luna llena. ¿En qué posición está la Luna?", [
      ("a", "Entre la Tierra y el Sol", "En esa posición vemos el lado oscuro: es Luna nueva."),
      ("b", "Al lado opuesto del Sol, visto desde la Tierra", "Correcto: vemos toda su mitad iluminada."),
      ("c", "Justo encima del polo norte", "La posición relevante es respecto del Sol, no de los polos.")], "b", ["nasa-fases"]),
    q("q3", "¿Cuándo oscurece la sombra terrestre a la Luna?", [
      ("a", "En cada Luna menguante", "La menguante es una fase de iluminación, no una sombra."),
      ("b", "Todas las noches", "No ocurre a diario."),
      ("c", "Durante un eclipse lunar", "Correcto: ocurre cuando la Tierra queda exactamente entre el Sol y la Luna.")], "c", ["nasa-eclipses"]),
  ],
  [("r1", "Explica una fase sin usar la expresión \"sombra de la Tierra\".", "Vemos una porción variable de la mitad de la Luna iluminada por el Sol."),
   ("r2", "¿Cada cuántos días se repite el ciclo de fases?", "Cada unos 29,5 días.")],
  "Repite tus dibujos iniciales y anota qué corregiste.",
  [src("nasa-fases", "NASA", "Moon Phases", "https://science.nasa.gov/moon/moon-phases/", "Introducción y sección All Moon Phases", ["El Sol ilumina la mitad de la Luna", "Cambia cuánto de esa mitad vemos al orbitar", "El ciclo se repite cada unos 29,5 días", "Las ocho fases"], HOY),
   src("nasa-eclipses", "NASA", "Eclipses and the Moon", "https://science.nasa.gov/moon/eclipses/", "Secciones Lunar Eclipse Basics, Types of Lunar Eclipses y The Moon's Tilted Orbit", ["Los eclipses lunares ocurren en fase de Luna llena", "Cuando la Tierra queda exactamente entre la Luna y el Sol, su sombra cae sobre la Luna", "La órbita lunar está inclinada unos 5 grados respecto de la órbita terrestre", "Vista desde la Tierra, la Luna suele pasar arriba o abajo del Sol cuando pasa entre nosotros y el Sol"], HOY),
   src("ou-hemisferio", "The Open University (OpenLearn)", "Moons of our Solar System, semana 1, 2.11 How the Moon's phases look from the Earth", "https://www.open.edu/openlearn/mod/oucontent/view.php?id=69107&section=3.11", "Figura 33 y párrafo que comienza \"Therefore, for observers…\"", ["Al sur del ecuador la Luna crece como una C y mengua como una D: la creciente se ve iluminada a la izquierda y la menguante a la derecha"], HOY)]))

exec(open(os.path.join(os.path.dirname(__file__), "lessons_r2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(__file__), "lote_v11.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(__file__), "lote_v2.py"), encoding="utf-8").read())

# ------------------------------------------------------------------ escritura
APROB = json.load(open(os.path.join(ROOT, "data", "aprobaciones.v1.json"), encoding="utf-8"))["registros"]
def estado_de(id, rev, sha):
    for r in APROB:
        if r["id"] == id and r["revision"] == rev and r["sha256"] == sha:
            v = r.get("verificacion", {}); ok = v.get("resultado") == "aprobado" or v.get("estado") == "verificado"
            if r.get("vb") and ok: return "publicado"
            if ok: return "verificado"
    return "borrador"
catalog = []
for les in L:
    data = json.dumps(les, ensure_ascii=False, indent=2).encode("utf-8")
    fn = f"{les['id']}.r{les['revision']}.json"
    open(os.path.join(OUT, fn), "wb").write(data)
    catalog.append({"id": les["id"], "revision": les["revision"], "schemaVersion": les["schemaVersion"], "titulo": les["titulo"],
                    "disciplina": les["disciplina"], "familia": les["familia"],
                    "minutosEstimados": les["minutosEstimados"], "estado": estado_de(les["id"], les["revision"], hashlib.sha256(data).hexdigest()),
                    "archivo": f"data/lessons/{fn}", "sha256": hashlib.sha256(data).hexdigest()})
# Borradores verificados por ChatGPT (N°17–N°18), solo para vista previa: se copian byte a byte, sin calendario ni registro.
BORRADORES = [(x["carpeta"], x["id"], x["revision"]) for x in json.load(open(os.path.join(ROOT, "tools", "manifiesto_publicacion.json"), encoding="utf-8"))["lecciones"]]
for carpeta, lid, rev in BORRADORES:
    data = open(os.path.join(ROOT, carpeta, f"{lid}.r{rev}.json"), "rb").read()
    les = json.loads(data); assert les["id"] == lid and les["revision"] == rev
    fn = f"{lid}.r{rev}.json"; open(os.path.join(OUT, fn), "wb").write(data)
    sha = hashlib.sha256(data).hexdigest()
    catalog.append({"id": lid, "revision": rev, "schemaVersion": les["schemaVersion"], "titulo": les["titulo"],
                    "disciplina": les["disciplina"], "familia": les["familia"], "minutosEstimados": les["minutosEstimados"],
                    "estado": estado_de(lid, rev, sha), "archivo": f"data/lessons/{fn}", "sha256": sha})
open(os.path.join(ROOT, "data", "catalog.v1.json"), "w", encoding="utf-8").write(
    json.dumps({"version": 1, "generado": HOY, "lecciones": catalog}, ensure_ascii=False, indent=2))

orden = ["numero-aureo", "imprenta-gutenberg", "fases-lunares", "cielos-coquimbo", "perspectiva-lineal", "corriente-humboldt", "bauhaus", "arco-panteon"]
import datetime
d0 = datetime.date(2026, 10, 19)
entries = [{"fecha": (d0 + datetime.timedelta(days=i)).isoformat(), "id": lid, "revision": REVISION.get(lid, 1)} for i, lid in enumerate(orden)]
# Interfaz v3 (tarjetas): calendario acordado con ChatGPT N°12–N°13
entries.append({"fecha": "2026-10-27", "id": "cielo-azul", "revision": 3})
# Lecciones en tarjetas del manifiesto (lote 1 con V°B° de Max; desde el lote 2, opción A)
for x in json.load(open(os.path.join(ROOT, "tools", "manifiesto_publicacion.json"), encoding="utf-8"))["lecciones"]:
    entries.append({"fecha": x["fecha"], "id": x["id"], "revision": x["revision"]})
open(os.path.join(ROOT, "data", "calendar.v1.json"), "w", encoding="utf-8").write(
    json.dumps({"version": 1, "zonaHoraria": "America/Santiago", "entradas": entries}, ensure_ascii=False, indent=2))
for c in catalog: print(c["id"], c["sha256"][:12])
