# Lote 1, REVISIÓN 2 (ajustes de ChatGPT N°16). BORRADORES para verificación de ChatGPT. Esquema 2.0, sin ilustraciones finales.
# No entran al catálogo, al calendario ni al registro de aprobaciones. Salida: borradores/lote1/
import json, hashlib, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "borradores", "lote1_r2")
os.makedirs(OUT, exist_ok=True)
HOY = "2026-10-20"

def card(id, tipo, **k):
    c = {"id": id, "tipo": tipo}
    for key in ("titulo", "texto", "revelado", "pregunta", "correctaId"):
        if k.get(key) is not None: c[key] = k[key]
    if "opciones" in k: c["opciones"] = [dict(id=o[0], texto=o[1], retro=o[2]) for o in k["opciones"]]
    c["fuenteIds"] = k.get("fuentes", [])
    return c

def src(id, entidad, titulo, url, ubicacion, afirmaciones, respalda, consultada=HOY):
    return dict(id=id, entidad=entidad, titulo=titulo, url=url, ubicacion=ubicacion,
                afirmaciones=afirmaciones, respalda=respalda, consultadaEl=consultada)

def lesson(id, fecha, disciplina, familia, titulo, subtitulo, idea, tarjetas, resumen, fuentes):
    return fecha, idea, {"schemaVersion": "2.0", "id": id, "revision": 2, "idioma": "es-CL",
        "disciplina": disciplina, "familia": familia, "titulo": titulo, "subtitulo": subtitulo,
        "minutosEstimados": 5, "tarjetas": tarjetas,
        "resumen": {"titulo": resumen[0], "puntos": resumen[1]}, "fuentes": fuentes,
        "controlEditorial": {"estado": "borrador", "revisadoPor": None, "fechaRevision": None}}

LOTE = []

# ------------------------------------------------------------------ 28-10 pan duro
LOTE.append(lesson("pan-duro", "2026-10-28", "Cocina y ciencia", "quimica",
  "¿Por qué el pan se pone duro?", "No es solo que se seque.",
  "El pan se endurece sobre todo porque el almidón de la miga se reordena al enfriarse, no solo porque pierda agua.",
  [card("c1", "portada", titulo="¿Por qué el pan se pone duro?", texto="La marraqueta de la mañana, en la tarde ya no es la misma. ¿Se secó? No exactamente.", fuentes=["asb-staling"]),
   card("c2", "pregunta", pregunta="¿Qué crees que hace que el pan se ponga duro?", correctaId="b", opciones=[
     ("a", "Que pierde agua y se seca", "Es lo que casi todos pensamos, pero no es la causa principal: el pan puede endurecerse incluso sin perder agua."),
     ("b", "Un cambio en el almidón de la miga", "¡Así es! El responsable principal es el almidón, que se reordena después del horneado."),
     ("c", "Que le entra aire", "El aire no es el responsable principal: lo es un cambio en el almidón de la miga.")], fuentes=["asb-staling"]),
   card("c3", "idea", titulo="El responsable es el almidón", texto="Cuando el pan se enfría después del horneado, el almidón de la miga se va reordenando de a poco. Ese cambio es el que pone firme la miga.", fuentes=["asb-staling", "millingmea-staling"]),
   card("c4", "revelar", titulo="Un descubrimiento antiguo", texto="Hace más de 150 años se comprobó algo curioso sobre el pan duro. ¿Qué crees que fue?",
        revelado="Que el pan duro no es solo pan seco. El endurecimiento puede ocurrir aunque la miga no pierda agua, porque el cambio pasa dentro de ella.", fuentes=["asb-staling"]),
   card("c5", "idea", titulo="El refrigerador lo empeora", texto="Guardar el pan en el refrigerador, entre 0 y 10 grados, acelera el endurecimiento de la miga.", fuentes=["millingmea-staling"]),
   card("c6", "idea", titulo="El congelador lo retrasa", texto="La congelación retrasa la reorganización del almidón y ayuda a conservar la textura del pan. Así, el endurecimiento de la miga se demora más.", fuentes=["asb-staling", "millingmea-staling"]),
   card("c7", "pregunta", pregunta="Compraste pan para tres días. ¿Dónde se endurece más rápido?", correctaId="a", opciones=[
     ("a", "En el refrigerador", "Correcto: el frío del refrigerador acelera el endurecimiento."),
     ("b", "En el congelador", "Al revés: congelarlo retrasa el endurecimiento."),
     ("c", "Da lo mismo", "No da lo mismo: el refrigerador lo acelera y el congelador lo retrasa.")], fuentes=["millingmea-staling", "asb-staling"]),
   card("c8", "dato", texto="Calentar el pan duro lo ablanda por un rato, pero no lo deja igual que recién horneado: el cambio del almidón no se deshace del todo.", fuentes=["millingmea-staling"])],
  ("El pan duro", ["El pan se pone duro sobre todo porque el almidón de la miga se reordena al enfriarse, no solo porque se seque.",
                   "El refrigerador acelera el endurecimiento; el congelador lo retrasa.",
                   "Calentarlo lo ablanda por un rato, pero no lo deja como recién hecho."]),
  [src("asb-staling", "American Society of Baking", "Staling", "https://asbe.org/article/staling/", "Texto principal",
       ["El endurecimiento hace que los productos horneados pierdan su frescura", "Se creía que se debía solo a la pérdida de humedad; eso se descartó hace más de 150 años", "Se asocia a la retrogradación o recristalización del almidón y puede ocurrir sin pérdida de agua de la miga", "Congelar detiene el movimiento molecular y evita que el almidón cristalice"],
       ["c1", "c2", "c3", "c4", "c6", "c7"]),
   src("millingmea-staling", "Milling Middle East & Africa (William Gatama, tecnólogo en panificación)", "Baking technology: Staling", "https://millingmea.com/baking-technology-staling/", "Texto principal",
       ["El endurecimiento resulta de la retrogradación del almidón, que ocurre después de que el pan se enfría; no es mera pérdida de humedad", "La refrigeración (0–10 °C) acelera la recristalización y el endurecimiento de la miga", "Congelar reduce la movilidad molecular y retrasa la retrogradación", "Recalentar puede ablandar temporalmente la miga, pero no restaura la organización original"],
       ["c3", "c5", "c6", "c7", "c8"])]))

# ------------------------------------------------------------------ 29-10 temblores en Chile
LOTE.append(lesson("temblores-chile", "2026-10-29", "Geografía", "geografia",
  "¿Por qué tiembla tanto en Chile?", "La respuesta está bajo el mar, frente a la costa.",
  "Frente a Chile, la placa de Nazca se hunde bajo la placa Sudamericana, y ese choque lento genera los terremotos.",
  [card("c1", "portada", titulo="¿Por qué tiembla tanto en Chile?", texto="Si vives en Chile, sabes lo que es un temblor. La razón está bajo el mar, frente a nuestra costa.", fuentes=["usgs-nazca"]),
   card("c2", "idea", titulo="Dos placas que se encuentran", texto="Frente a Chile se juntan dos enormes placas de roca: la placa de Nazca, bajo el océano Pacífico, y la placa Sudamericana, donde está el continente.", fuentes=["usgs-nazca"]),
   card("c3", "idea", titulo="Una se mete debajo de la otra", texto="La placa de Nazca se mete lentamente bajo Sudamérica; a eso se le llama subducción. Las dos placas se acercan entre 6,5 y 8 centímetros por año.", fuentes=["usgs-nazca"]),
   card("c4", "pregunta", pregunta="¿Qué hace la placa de Nazca frente a Chile?", correctaId="a", opciones=[
     ("a", "Se hunde lentamente bajo la placa Sudamericana", "¡Exacto! Eso es la subducción."),
     ("b", "Se aleja de Chile hacia el oeste", "No: avanza hacia el continente y se mete por debajo."),
     ("c", "Está quieta", "No está quieta: las placas se acercan varios centímetros cada año.")], fuentes=["usgs-nazca"]),
   card("c5", "idea", titulo="Por eso tiembla", texto="Los bordes de las placas son ásperos y se quedan trabados, mientras el resto sigue moviéndose. La energía se acumula hasta que los bordes se destraban de golpe: esa liberación repentina es el terremoto.", fuentes=["usgs-sismos"]),
   card("c6", "revelar", titulo="El más grande", texto="En Chile ocurrió el terremoto más grande registrado en el siglo XX. ¿Sabes cuál fue?",
        revelado="El de Valdivia, el 22 de mayo de 1960, de magnitud 9,5. Se produjo donde la placa de Nazca se hunde bajo Sudamérica.", fuentes=["britannica-1960", "csn-terremotos"]),
   card("c7", "pregunta", pregunta="Un amigo extranjero te pregunta por qué en Chile tiembla tanto. ¿Qué le dices?", correctaId="a", opciones=[
     ("a", "Porque frente a la costa una placa se mete bajo la otra, y sus bordes se traban y se destraban de golpe", "¡Así es! Ese encuentro de placas es la causa de fondo."),
     ("b", "Por los volcanes", "Los volcanes también nacen del encuentro de las placas, pero la causa de fondo de los temblores es ese encuentro."),
     ("c", "Porque el país es muy largo", "El largo del país no es la causa: lo es el encuentro de las placas frente a la costa.")], fuentes=["usgs-nazca", "usgs-sismos"]),
   card("c8", "dato", texto="El tsunami del terremoto de 1960 cruzó el océano Pacífico: unas 15 horas después llegó a Hawái, y también causó daños en Japón.", fuentes=["britannica-1960"])],
  ("Chile y los temblores", ["Frente a Chile, la placa de Nazca se hunde lentamente bajo la placa Sudamericana.",
                             "Los bordes de las placas se traban y acumulan energía; cuando se destraban de golpe, se produce el terremoto.",
                             "El terremoto de Valdivia de 1960, de magnitud 9,5, fue el más grande registrado en el siglo XX."]),
  [src("usgs-nazca", "U.S. Geological Survey", "Seismicity of the Earth 1900–2013: Seismotectonics of South America (Nazca Plate Region)", "https://www.usgs.gov/publications/seismicity-earth-1900-2013-seismotectonics-south-america-nazca-plate-region", "Resumen de la publicación",
       ["La corteza y litosfera oceánica de la placa de Nazca comienzan su descenso al manto bajo Sudamérica", "Convergencia de aproximadamente 80 mm/año en el sur a aproximadamente 65 mm/año en el norte", "La subducción influye en la actividad volcánica, la deformación de la corteza y la generación de terremotos; es responsable del levantamiento de los Andes y de la cadena volcánica activa"],
       ["c1", "c2", "c3", "c4", "c7"]),
   src("usgs-sismos", "U.S. Geological Survey", "The Science of Earthquakes", "https://www.usgs.gov/programs/earthquake-hazards/science-earthquakes", "Texto principal",
       ["Como los bordes de las placas son ásperos, se traban mientras el resto de la placa sigue moviéndose", "Mientras los bordes están trabados, se va almacenando la energía", "Cuando la fuerza vence la fricción y la falla se destraba, toda esa energía se libera", "La energía se irradia en forma de ondas sísmicas"],
       ["c5", "c7"]),
   src("britannica-1960", "Encyclopaedia Britannica", "Chile earthquake of 1960", "https://www.britannica.com/print/article/1421130", "Artículo completo",
       ["Se originó frente a la costa sur de Chile el 22 de mayo de 1960", "La mayoría de las fuentes le asignan magnitud 9,5", "El terremoto más grande registrado en el siglo XX", "La ruptura ocurrió donde la placa de Nazca subduce bajo la placa Sudamericana", "Las olas llegaron a Hawái unas 15 horas después; en Japón destruyeron más de 1.600 viviendas"],
       ["c6", "c8"], "2026-10-19"),
   src("csn-terremotos", "Centro Sismológico Nacional, Universidad de Chile", "Grandes terremotos en Chile", "https://www.csn.uchile.cl/sismologia/grandes-terremotos-en-chile/", "Tabla de sismos importantes o destructivos",
       ["Valdivia, 22/05/1960: Mw 9,5"], ["c6"])]))

# ------------------------------------------------------------------ 30-10 UF
LOTE.append(lesson("unidad-fomento", "2026-10-30", "Economía cotidiana", "economia",
  "¿Qué cambia cuando un precio está en UF?", "Arriendos, créditos y seguros: por qué no en pesos.",
  "La UF es una unidad cuyo valor en pesos cambia cada día siguiendo al IPC; por eso lo que está en UF sube en pesos cuando suben los precios.",
  [card("c1", "portada", titulo="¿Qué es la UF?", texto="Créditos y seguros pueden estar expresados en UF. ¿Por qué no simplemente en pesos?", fuentes=["bcch-uf"]),
   card("c2", "idea", titulo="Medir cuánto cambian los precios", texto="Cada mes, el INE mide cuánto cambian los precios de una canasta de productos y servicios que compran los hogares. Ese índice se llama IPC.", fuentes=["ine-ipc"]),
   card("c3", "idea", titulo="La UF sigue al IPC", texto="La UF es una unidad que calcula el Banco Central. Su valor en pesos se reajusta diariamente según el IPC del mes anterior.", fuentes=["bcch-uf"]),
   card("c4", "pregunta", pregunta="Si el IPC del mes anterior subió, ¿qué pasa con el valor de la UF en pesos?", correctaId="a", opciones=[
     ("a", "Sube un poco cada día, desde el día 10", "¡Exacto! La UF se reajusta cada día, desde el 10 de un mes hasta el 9 del siguiente, según el IPC del mes anterior."),
     ("b", "Baja", "Al revés: si el IPC del mes anterior subió, la UF sube en pesos."),
     ("c", "Cambia al instante con los precios de hoy", "No: la UF sigue el IPC del mes anterior, que ya fue medido; no reacciona a los precios de hoy.")], fuentes=["bcch-uf"]),
   card("c5", "idea", titulo="Un arriendo en UF", texto="Si el contrato mantiene el arriendo en 10 UF, cada mes pagas 10 UF. Pero si el IPC del mes anterior subió, esas 10 UF equivalen a un poco más de pesos.", fuentes=["bcch-uf"]),
   card("c6", "revelar", titulo="¿Para qué sirve en un crédito?", texto="Si un crédito está expresado en UF, ¿qué le pasa a la deuda en pesos?",
        revelado="Se reajusta según el IPC del mes anterior. El Banco Central explica que la UF sirve como índice de reajuste para créditos en moneda nacional de bancos y cooperativas, y que también la usan cajas de compensación y compañías de seguros.", fuentes=["bcch-uf"]),
   card("c7", "pregunta", pregunta="Te ofrecen dos arriendos: uno en pesos fijos por dos años y otro que se mantiene en UF. Si el IPC viene subiendo, ¿cuál sube en pesos?", correctaId="a", opciones=[
     ("a", "El que está en UF", "Correcto: como la UF se reajusta según el IPC del mes anterior, el monto en pesos sube."),
     ("b", "El de pesos fijos", "El de pesos fijos se mantiene en el mismo monto en pesos."),
     ("c", "Ninguno de los dos", "El que está en UF sí cambia en pesos, porque la UF se reajusta según el IPC del mes anterior.")], fuentes=["bcch-uf"]),
   card("c8", "dato", texto="El valor de la UF se conoce por adelantado: a más tardar el día 9 de cada mes se publican en el Diario Oficial los valores de cada día, desde el 10 de ese mes hasta el 9 del siguiente.", fuentes=["bcch-uf"])],
  ("La UF", ["La UF es una unidad que calcula el Banco Central; su valor en pesos se reajusta cada día.",
             "El reajuste sigue el IPC del mes anterior, el índice que mide cuánto cambiaron los precios.",
             "Por eso, un monto en UF equivale a más pesos cuando el IPC del mes anterior subió."]),
  [src("bcch-uf", "Banco Central de Chile", "Unidad de Fomento (UF): nota metodológica", "https://si3.bcentral.cl/estadisticas/Principal1/Metodologias/EMF/UF.pdf", "Texto completo",
       ["La UF es un índice de reajustabilidad, calculado y autorizado por el Banco Central de Chile", "Se reajusta en forma diaria desde el día 10 de cada mes hasta el día 9 del mes siguiente, de acuerdo con la variación del IPC", "Se usa como índice de reajuste para créditos en moneda nacional de bancos y cooperativas, y en otras entidades como cajas de compensación y compañías de seguros", "El valor diario se publica en el Diario Oficial a más tardar el día 9 de cada mes"],
       ["c1", "c3", "c4", "c5", "c6", "c7", "c8"]),
   src("ine-ipc", "Instituto Nacional de Estadísticas", "Índice de Precios al Consumidor", "https://www.ine.gob.cl/estadisticas/economia/indices-de-precio-e-inflacion/indice-de-precios-al-consumidor", "Definición",
       ["El IPC mide mes a mes la variación de los precios de una canasta de bienes y servicios representativa del consumo de los hogares urbanos"], ["c2"])]))

# ------------------------------------------------------------------ 31-10 Luna
LOTE.append(lesson("fases-luna", "2026-10-31", "Astronomía", "astronomia",
  "¿Por qué cambia la forma de la Luna?", "La Luna no cambia: cambia lo que vemos de ella.",
  "El Sol siempre ilumina la mitad de la Luna; las fases son la parte de esa mitad que vemos desde la Tierra.",
  [card("c1", "portada", titulo="¿Por qué cambia la forma de la Luna?", texto="A veces es un círculo completo y a veces una tajada fina. Pero la Luna no cambia: cambia lo que vemos de ella.", fuentes=["nasa-fases"]),
   card("c2", "idea", titulo="La Luna no tiene luz propia", texto="La Luna no produce la luz que vemos: refleja la luz del Sol.", fuentes=["nasa-fases"]),
   card("c3", "idea", titulo="Siempre hay una mitad iluminada", texto="El Sol ilumina siempre la mitad de la Luna. Lo que cambia es cuánto de esa mitad vemos desde la Tierra mientras la Luna da su vuelta.", fuentes=["nasa-fases"]),
   card("c4", "pregunta", pregunta="¿Qué causa las fases de la Luna?", correctaId="a", opciones=[
     ("a", "Cuánto vemos de la mitad que el Sol ilumina", "¡Exacto! La mitad iluminada siempre está; cambia cuánto de ella vemos."),
     ("b", "Que la Luna se achica y se agranda", "La Luna no cambia de tamaño: cambia la parte iluminada que vemos."),
     ("c", "Que la Luna se apaga de a poco", "La Luna no tiene luz propia que se apague: la ilumina el Sol.")], fuentes=["nasa-fases"]),
   card("c5", "idea", titulo="Un ciclo de casi un mes", texto="El ciclo completo de fases se repite más o menos una vez al mes: cada 29 días y medio.", fuentes=["nasa-fases"]),
   card("c6", "revelar", titulo="Una ayuda para Chile", texto="En el hemisferio sur, cuando la Luna se ve como una tajada fina, ¿cómo saber si está creciendo o menguando?",
        revelado="Una ayuda visual: al sur del ecuador, la tajada de Luna creciente suele parecerse a una C, y la menguante, a una D. Muchas veces se ve un poco inclinada.", fuentes=["ou-hemisferio"]),
   card("c7", "pregunta", pregunta="Esta noche, en Coquimbo, ves una tajada fina de Luna con forma de C. Usando la ayuda visual, ¿va creciendo o menguando?", correctaId="a", opciones=[
     ("a", "Creciendo", "Correcto: en el hemisferio sur, la tajada creciente suele parecerse a una C."),
     ("b", "Menguando", "En el hemisferio sur, la tajada menguante suele parecerse a una D."),
     ("c", "Es luna llena", "La luna llena se ve como un círculo completo.")], fuentes=["ou-hemisferio"]),
   card("c8", "dato", texto="Las fases de la Luna son ocho: luna nueva, creciente, cuarto creciente, gibosa creciente, luna llena, gibosa menguante, cuarto menguante y menguante.", fuentes=["nasa-fases"])],
  ("Las fases de la Luna", ["La Luna no tiene luz propia: refleja la luz del Sol, que siempre ilumina una mitad de ella.",
                            "Las fases son la parte de esa mitad iluminada que vemos desde la Tierra; el ciclo dura unos 29 días y medio.",
                            "En Chile, una ayuda visual: la tajada creciente suele parecerse a una C, y la menguante, a una D."]),
  [src("nasa-fases", "NASA Science", "Moon Phases", "https://science.nasa.gov/moon/moon-phases/", "Texto principal",
       ["La Luna no produce su propia luz; la luz de la Luna es luz del Sol reflejada", "El Sol siempre ilumina la mitad de la Luna; cuánto vemos de esa mitad cambia a medida que recorre su órbita", "El ciclo se repite más o menos una vez al mes (cada 29,5 días)", "Las ocho fases, en orden: nueva, creciente, cuarto creciente, gibosa creciente, llena, gibosa menguante, cuarto menguante y menguante"],
       ["c1", "c2", "c3", "c4", "c5", "c8"]),
   src("ou-hemisferio", "The Open University (OpenLearn)", "Moons of our Solar System, semana 1, 2.11 How the Moon's phases look from the Earth", "https://www.open.edu/openlearn/mod/oucontent/view.php?id=69107&section=3.11", "Párrafo sobre el hemisferio sur",
       ["Al sur del ecuador, la Luna crece como una C y mengua como una D, con la curva levemente inclinada"], ["c6", "c7"])]))

# ------------------------------------------------------------------ 01-11 Gabriela Mistral
LOTE.append(lesson("gabriela-mistral", "2026-11-01", "Literatura", "literatura",
  "¿Quién fue Gabriela Mistral?", "La maestra de Vicuña que ganó el Nobel.",
  "Gabriela Mistral fue poeta y maestra; nació en Vicuña y en 1945 recibió el primer Nobel de Literatura para las letras latinoamericanas.",
  [card("c1", "portada", titulo="¿Quién fue Gabriela Mistral?", texto="Nació en Vicuña, en el Valle del Elqui, y en 1945 ganó el Premio Nobel de Literatura.", fuentes=["memoria-mistral"]),
   card("c2", "idea", titulo="Lucila, la maestra", texto="Fue bautizada como Lucila de María Godoy Alcayaga. Nació en Vicuña el 7 de abril de 1889 y empezó a trabajar en una escuela antes de cumplir 16 años.", fuentes=["memoria-mistral"]),
   card("c3", "idea", titulo="Un nombre para su obra", texto="Gabriela Mistral fue el nombre con que firmó sus poemas. Hoy se la considera uno de los principales referentes de la literatura chilena.", fuentes=["memoria-mistral"]),
   card("c4", "pregunta", pregunta="¿Por qué crees que se recuerda a Gabriela Mistral?", correctaId="a", opciones=[
     ("a", "Por su poesía y por su trabajo como maestra", "¡Así es! Fue poeta y maestra; en 1922 incluso fue invitada a México a colaborar en una reforma educacional."),
     ("b", "Por haber sido presidenta de Chile", "No: se la recuerda por su poesía y por su trabajo como maestra."),
     ("c", "Por haber escrito solo novelas", "Su obra más conocida es poesía: publicó cuatro libros de poemas.")], fuentes=["memoria-mistral"]),
   card("c5", "idea", titulo="Los primeros premios y libros", texto="En 1914 ganó el premio principal de los Juegos Florales con sus «Sonetos de la muerte». En 1922 publicó su primer libro, «Desolación».", fuentes=["memoria-mistral"]),
   card("c6", "idea", titulo="Poemas para niños", texto="También escribió canciones y poemas para niños, como los de «Ternura», de 1924. Por eso muchas personas la recuerdan como madre y maestra.", fuentes=["memoria-mistral"]),
   card("c7", "revelar", titulo="1945", texto="En 1945 recibió un premio que la Academia Sueca nunca antes había dado a las letras latinoamericanas. ¿Cuál fue?",
        revelado="El Premio Nobel de Literatura. Fue el primer reconocimiento de la Academia Sueca a las letras latinoamericanas.", fuentes=["memoria-mistral"]),
   card("c8", "pregunta", pregunta="¿Qué logró Gabriela Mistral en 1945?", correctaId="a", opciones=[
     ("a", "Ganó el Premio Nobel de Literatura, el primero para las letras latinoamericanas", "¡Exacto! Fue un reconocimiento histórico."),
     ("b", "Publicó su primer libro", "Su primer libro, «Desolación», es de 1922."),
     ("c", "Ganó los Juegos Florales", "Los Juegos Florales los ganó en 1914.")], fuentes=["memoria-mistral"])],
  ("Gabriela Mistral", ["Gabriela Mistral, bautizada Lucila de María Godoy Alcayaga, nació en Vicuña en 1889 y fue maestra desde muy joven.",
                        "Escribió poemas y también canciones para niños, como los de «Ternura».",
                        "En 1945 ganó el Premio Nobel de Literatura: el primero de la Academia Sueca para las letras latinoamericanas."]),
  [src("memoria-mistral", "Memoria Chilena, Biblioteca Nacional de Chile", "Gabriela Mistral (1889-1957)", "https://www.memoriachilena.gob.cl/602/w3-article-3429.html", "Presentación y cronología",
       ["La poeta Gabriela Mistral es considerada uno de los principales referentes de la literatura chilena", "Nació en Vicuña el 7 de abril de 1889; fue bautizada como Lucila de María Godoy Alcayaga", "Hacia 1905, cuando iba a cumplir 16 años, inició su carrera docente como ayudante en la Escuela de La Compañía Baja (la cronología la fecha en 1904)", "En 1922 fue invitada a México a colaborar en la reforma educacional", "Con los «Sonetos de la muerte» obtuvo el premio principal de los Juegos Florales de 1914", "«Desolación» (Nueva York, 1922) fue su primer libro; «Ternura: canciones de niños» (Madrid, 1924); publicó cuatro libros de poesía", "Su imagen pública destacó su figura de madre y maestra", "El Nobel de 1945 constituye el primer reconocimiento de la Academia Sueca a las letras latinoamericanas"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"])]))

# ------------------------------------------------------------------ 02-11 GPS
LOTE.append(lesson("como-funciona-gps", "2026-11-02", "Tecnología", "tecnologia",
  "¿Cómo sabe el GPS dónde estoy?", "El punto azul del mapa, explicado.",
  "El receptor GPS compara cuándo salió y cuándo llegó la señal de cada satélite, y con la distancia a cuatro o más calcula su posición.",
  [card("c1", "portada", titulo="¿Cómo sabe el GPS dónde estoy?", texto="Abres el mapa del celular y aparece un punto justo donde estás. Una parte de esa respuesta viene del espacio.", fuentes=["gps-poster"]),
   card("c2", "idea", titulo="Satélites alrededor de la Tierra", texto="El sistema GPS mantiene al menos 24 satélites funcionando, a unos 20.200 kilómetros de altura.", fuentes=["gps-espacio"]),
   card("c3", "idea", titulo="Señales con la hora exacta", texto="Cada satélite envía señales de radio con la hora exacta de sus relojes atómicos. El receptor anota cuándo llega cada señal y, comparando las horas, calcula a qué distancia está cada satélite.", fuentes=["gps-poster", "britannica-gps"]),
   card("c4", "pregunta", pregunta="¿Qué compara el receptor GPS para saber a qué distancia está cada satélite?", correctaId="a", opciones=[
     ("a", "La hora en que salió la señal y la hora en que llegó", "¡Exacto! Con esa diferencia calcula la distancia."),
     ("b", "La fuerza del viento", "El viento no tiene que ver: el GPS usa la hora de las señales de radio de los satélites."),
     ("c", "La temperatura del aire", "No: el GPS calcula distancias con la hora de salida y de llegada de las señales.")], fuentes=["gps-poster", "britannica-gps"]),
   card("c5", "idea", titulo="Con cuatro basta", texto="Cuando conoce su distancia a por lo menos cuatro satélites, el receptor calcula su posición en tres dimensiones.", fuentes=["gps-poster", "britannica-gps"]),
   card("c6", "revelar", titulo="¿Funciona en todas partes?", texto="¿Crees que el GPS funciona igual de bien dentro de un edificio que en un lugar abierto?",
        revelado="No siempre. La constelación está distribuida para ofrecer cobertura desde prácticamente toda la Tierra, pero para recibir bien las señales ayuda tener el cielo despejado: los edificios, los puentes y los árboles pueden bloquearlas.", fuentes=["gps-espacio", "gps-precision"]),
   card("c7", "pregunta", pregunta="Para calcular una posición en tres dimensiones usando GPS, ¿de cuántos satélites necesita conocer la distancia un receptor, como mínimo?", correctaId="a", opciones=[
     ("a", "Cuatro", "Correcto: necesita la distancia a por lo menos cuatro satélites."),
     ("b", "Uno", "Con uno solo no le alcanza: necesita por lo menos cuatro."),
     ("c", "Veinticuatro", "Hay al menos 24 en órbita, pero para calcular la posición le basta con cuatro o más.")], fuentes=["gps-poster", "gps-espacio"]),
   card("c8", "dato", texto="Cada satélite GPS da dos vueltas completas a la Tierra por día.", fuentes=["gps-espacio"])],
  ("Cómo funciona el GPS", ["El GPS usa al menos 24 satélites que envían señales de radio con la hora de sus relojes atómicos.",
                            "El receptor compara cuándo salió y cuándo llegó cada señal, y así calcula su distancia a cada satélite.",
                            "Con la distancia a por lo menos cuatro satélites calcula su posición; los edificios y los árboles pueden bloquear las señales."]),
  [src("gps-poster", "GPS.gov (Gobierno de los Estados Unidos)", "How GPS Works (póster, versión de texto)", "https://www.gps.gov/multimedia/poster/poster.txt", "Sección sobre el funcionamiento del receptor",
       ["Los satélites GPS transmiten señales de radio con su ubicación, su estado y la hora precisa (t1) de sus relojes atómicos", "El receptor registra la hora exacta de llegada (t2) de cada señal y, comparándola con la hora de emisión, calcula su distancia a cada satélite", "Cuando conoce su distancia a por lo menos cuatro satélites, puede calcular su posición tridimensional en la Tierra"],
       ["c1", "c3", "c4", "c5", "c7"]),
   src("britannica-gps", "Encyclopaedia Britannica", "GPS", "https://www.britannica.com/technology/GPS", "Resumen inicial",
       ["El receptor mide el tiempo que tardan las señales de radio de cuatro o más satélites, calcula la distancia a cada uno y con ello determina la posición"],
       ["c3", "c4", "c5"]),
   src("gps-espacio", "GPS.gov (Gobierno de los Estados Unidos)", "Space Segment", "https://www.gps.gov/systems/gps/space/", "Constelación y órbitas",
       ["Se comprometen a mantener al menos 24 satélites GPS operativos el 95 % del tiempo", "Los satélites operan a aproximadamente 20.200 km de altura", "Cada satélite da dos vueltas a la Tierra por día", "La disposición permite ver al menos cuatro satélites desde prácticamente cualquier punto del planeta"],
       ["c2", "c6", "c7", "c8"]),
   src("gps-precision", "GPS.gov (Gobierno de los Estados Unidos)", "GPS Accuracy", "https://www.gps.gov/gps-accuracy", "Causas comunes de pérdida de precisión",
       ["El bloqueo de las señales por edificios, puentes, árboles, etc., y el uso en interiores o bajo tierra degradan la precisión", "La precisión de los teléfonos empeora cerca de edificios, puentes y árboles"],
       ["c6"])]))

# ------------------------------------------------------------------ 03-11 mar salado
LOTE.append(lesson("mar-salado", "2026-11-03", "Ciencias de la Tierra", "geografia",
  "¿Por qué el mar es salado?", "La sal viaja desde las rocas hasta el océano.",
  "La mayor parte de la sal del mar viene de las rocas de la tierra firme: la lluvia las desgasta y los ríos llevan esos minerales al océano.",
  [card("c1", "portada", titulo="¿Por qué el mar es salado?", texto="Al mar le llega el agua de los ríos. Entonces, ¿de dónde sale tanta sal?", fuentes=["noaa-sal"]),
   card("c2", "pregunta", pregunta="¿De dónde crees que viene la mayor parte de la sal del mar?", correctaId="a", opciones=[
     ("a", "De las rocas de la tierra firme", "¡Así es! Las rocas en tierra firme son la principal fuente de las sales del mar."),
     ("b", "De los peces", "No: la principal fuente son las rocas de la tierra firme."),
     ("c", "De las nubes", "No: la mayor parte llega desde las rocas de la tierra firme.")], fuentes=["noaa-sal"]),
   card("c3", "idea", titulo="La lluvia desgasta las rocas", texto="El agua de lluvia es levemente ácida y va desgastando las rocas. Así se desprenden minerales que quedan disueltos en el agua.", fuentes=["noaa-sal"]),
   card("c4", "idea", titulo="Los ríos los llevan al mar", texto="Esos minerales disueltos viajan por arroyos y ríos hasta llegar al océano.", fuentes=["noaa-sal", "usgs-sal"]),
   card("c5", "idea", titulo="También desde el fondo del mar", texto="Otra parte de las sales viene del propio fondo del océano: de grietas calentadas por el magma y de volcanes submarinos.", fuentes=["noaa-sal"]),
   card("c6", "revelar", titulo="¿Cuánta sal tiene?", texto="Si tomaras un kilo de agua de mar, ¿cuánta sal crees que tendría?",
        revelado="En promedio, unos 35 gramos: cerca del 3,5 % del peso del agua de mar son sales disueltas. La cantidad cambia de un lugar a otro.", fuentes=["noaa-sal", "usgs-sal"]),
   card("c7", "pregunta", pregunta="Un niño te pregunta de dónde sale la sal del mar. ¿Qué le dices?", correctaId="a", opciones=[
     ("a", "La lluvia desgasta las rocas y los ríos llevan esos minerales al mar", "¡Exacto! Ese es el camino principal de la sal."),
     ("b", "La ponen los peces", "No: los peces no son la fuente; lo son sobre todo las rocas de la tierra firme."),
     ("c", "Cae con la lluvia directo al mar", "La lluvia ayuda, pero desgastando las rocas en tierra: los ríos llevan después esos minerales al mar.")], fuentes=["noaa-sal"]),
   card("c8", "dato", texto="Entre las sales disueltas del mar predominan el sodio y el cloruro: juntos representan cerca del 85 % de los iones disueltos.", fuentes=["noaa-sal"])],
  ("La sal del mar", ["La mayor parte de la sal del mar viene de las rocas de la tierra firme, que la lluvia desgasta.",
                      "Los ríos llevan esos minerales disueltos al océano; otra parte sale de grietas y volcanes del fondo marino.",
                      "En promedio, cada kilo de agua de mar tiene unos 35 gramos de sales."]),
  [src("noaa-sal", "NOAA National Ocean Service", "Why is the ocean salty?", "https://oceanservice.noaa.gov/facts/whysalty.html", "Texto principal",
       ["Las rocas en tierra son la principal fuente de las sales disueltas en el agua de mar", "La lluvia es levemente ácida y erosiona las rocas, liberando iones que van a arroyos y ríos que desembocan en el océano", "El agua del océano se filtra por grietas del fondo y es calentada por el magma; algunas sales provienen de erupciones volcánicas submarinas", "Cloruro y sodio forman cerca del 85 % de los iones disueltos", "Salinidad promedio de unas 35 partes por mil: cerca del 3,5 % del peso del agua de mar son sales disueltas", "La salinidad varía con la temperatura, la evaporación y la precipitación"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]),
   src("usgs-sal", "U.S. Geological Survey", "Why is the ocean salty?", "https://www.usgs.gov/faqs/why-ocean-salty", "Respuesta principal",
       ["Los iones de la escorrentía son llevados a arroyos y ríos y luego al océano", "La salinidad del agua de mar es de unas 35 partes por mil; cerca del 3,5 % de su peso son sales disueltas"],
       ["c4", "c6"])]))

# ------------------------------------------------------------------ escritura e índice
rows = []
def words(L):
    n = 0
    for t in L["tarjetas"]:
        for k in ("titulo", "texto", "revelado", "pregunta"):
            n += len(t.get(k, "").split())
        for o in t.get("opciones", []): n += len(o["texto"].split()) + len(o["retro"].split())
    n += sum(len(p.split()) for p in L["resumen"]["puntos"]) + len(L["resumen"]["titulo"].split())
    return n
for fecha, idea, L in LOTE:
    for f in L["fuentes"]:
        for c in f["respalda"]: assert f["id"] in next(t for t in L["tarjetas"] if t["id"] == c)["fuenteIds"], (L["id"], f["id"], c)
    assert 6 <= len(L["tarjetas"]) <= 9 and any(t["tipo"] == "pregunta" for t in L["tarjetas"]) and 2 <= len(L["resumen"]["puntos"]) <= 3
    ids = {f["id"] for f in L["fuentes"]}
    for t in L["tarjetas"]:
        assert t["fuenteIds"], ("tarjeta sin fuente", L["id"], t["id"])
        assert set(t["fuenteIds"]) <= ids, (L["id"], t["id"])
        for f in L["fuentes"]:
            if f["id"] in t["fuenteIds"]: assert t["id"] in f["respalda"], (L["id"], t["id"], f["id"])
    data = json.dumps(L, ensure_ascii=False, indent=2).encode("utf-8")
    fn = f"{L['id']}.r2.json"; open(os.path.join(OUT, fn), "wb").write(data)
    rows.append((fecha, L, idea, hashlib.sha256(data).hexdigest(), fn, words(L)))
md = ["# Lote 1, revisión 2 — borradores para verificación (esquema 2.0)", "",
      "Generado por Claude el 20-10-2026. Sin ilustraciones finales, sin publicación, sin calendario definitivo y sin registro de aprobación.", "",
      "| Fecha propuesta | Tema | Familia | Pregunta cotidiana | Idea central | Fuentes principales | Tarjetas | Palabras | Archivo | SHA-256 |",
      "|---|---|---|---|---|---|---|---|---|---|"]
for fecha, L, idea, sha, fn, w in rows:
    d = "-".join(reversed(fecha.split("-")))
    md.append(f"| {d} | {L['disciplina']} | {L['familia']} | {L['titulo']} | {idea} | {'; '.join(f['entidad'] for f in L['fuentes'])} | {len(L['tarjetas'])} | {w} | {fn} | `{sha}` |")
md += ["", "Palabras: títulos, textos, revelaciones, preguntas, opciones, retroalimentaciones y resumen de cada lección."]
open(os.path.join(OUT, "INDICE_LOTE1.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
for r in rows: print(r[0], r[1]["id"], len(r[1]["tarjetas"]), r[5], r[3][:12])
