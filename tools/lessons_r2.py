# Revisiones r2 de seis lecciones, según el informe de ChatGPT N°7 (19-10-2026).
# Se ejecuta dentro de gen_lessons.py (comparte helpers y figuras). Las r1 quedan intactas en disco.
R2_IDS = {"corriente-humboldt", "cielos-coquimbo", "imprenta-gutenberg", "perspectiva-lineal", "bauhaus", "arco-panteon"}
L[:] = [x for x in L if x["id"] not in R2_IDS]
for _id in R2_IDS: REVISION[_id] = 3  # r3 según ChatGPT N°9; Humboldt queda en r2 (aprobada)
REVISION["corriente-humboldt"] = 2

# ------------------------------------------------------------------ corriente-humboldt r2
L.append(lesson("corriente-humboldt", "Geografía", "geografia", ["océano", "clima", "Coquimbo"],
  "La corriente de Humboldt y la camanchaca", 13,
  ["Explicar qué es la surgencia costera", "Relacionar el mar frío con la niebla costera y la escasa lluvia"],
  "Antes de leer: si la costa está junto al océano, ¿por qué llueve tan poco en el norte de Chile?",
  [
    step("corriente", "Un río frío dentro del mar", [
      "La corriente de Humboldt, también llamada corriente del Perú, es una corriente fría que avanza hacia el norte por la costa occidental de Sudamérica.",
      "El viento empuja el agua superficial mar adentro y sube agua desde mayor profundidad, más fría, para reemplazarla. Ese proceso se llama surgencia."],
      ["britannica-peru", "noaa"],
      fig(cur, "Mapa esquemático: dos flechas suben paralelas a la costa chilena y una flecha punteada sale de la costa hacia el mar.", "Esquema simplificado, sin escala."),
      ("prediccion", "Si disminuyen los vientos favorables a la surgencia y las demás condiciones son semejantes, ¿qué esperas que pase con la temperatura del mar en la costa?", "Que suba menos agua fría desde la profundidad, de modo que el mar costero tendería a entibiarse.")),
    step("clima", "Mar frío, cielo estable", [
      "El océano frío favorece una capa de aire fresco y húmedo cerca de la superficie. Más arriba, el aire descendente del anticiclón del Pacífico contribuye a mantener condiciones estables y una inversión térmica.",
      "La inversión limita el desarrollo vertical de las nubes. Puede haber nubes bajas y niebla costera, la camanchaca, con poca precipitación. La aridez regional depende también de otros factores."],
      ["britannica-peru", "osses-1998"], None,
      ("explicacion", "Explica a otra persona por qué puede haber nubes bajas en la costa y, aun así, llover poco.", "La inversión térmica limita el crecimiento vertical de las nubes; sin ese desarrollo es difícil que produzcan lluvia abundante.")),
    step("vida", "Agua fría, mar productivo", [
      "El agua que sube por surgencia es rica en nutrientes. Fertiliza las aguas superficiales y favorece el crecimiento del fitoplancton; por eso las buenas zonas de pesca suelen estar donde la surgencia es común.",
      "Durante El Niño la surgencia se debilita o se detiene y llegan menos nutrientes. Puede haber menos fitoplancton, lo que afecta a los peces que se alimentan de él y a quienes se alimentan de esos peces."],
      ["noaa", "noaa-nino", "britannica-peru"], None,
      ("prediccion", "Si durante El Niño llegan menos nutrientes a la superficie, ¿qué puede pasar con la cadena alimentaria marina?", "Puede haber menos fitoplancton, y eso puede afectar la distribución y disponibilidad de los peces que dependen de él.")),
  ],
  [
    q("q1", "¿Qué es la surgencia costera?", [
      ("a", "El ascenso de agua más profunda y fría que reemplaza al agua superficial desplazada por el viento", "Correcto: el viento aleja el agua de superficie y sube agua desde mayor profundidad."),
      ("b", "Una ola gigante producida por sismos", "Eso es un tsunami, un fenómeno distinto."),
      ("c", "La llegada de agua dulce de los ríos al mar", "La surgencia trae agua desde la profundidad del océano, no desde los ríos.")], "a", ["noaa"]),
    q("q2", "Disminuye el aporte de agua rica en nutrientes en la costa. ¿Qué efecto puede tener sobre el fitoplancton?", [
      ("a", "Puede disminuir, porque recibe menos nutrientes", "Correcto: el fitoplancton depende de esos nutrientes."),
      ("b", "Siempre aumenta", "Con menos nutrientes no hay razón para esperar un aumento."),
      ("c", "No cambia, porque solo depende de la luz", "La luz importa, pero los nutrientes también limitan su crecimiento.")], "a", ["noaa", "noaa-nino"]),
    q("q3", "¿Qué papel cumple la inversión térmica en la costa norte?", [
      ("a", "Limita el desarrollo vertical de las nubes", "Correcto: por eso puede haber nubes bajas con poca lluvia."),
      ("b", "Calienta el agua del mar", "La inversión es una característica del aire, no calienta el océano."),
      ("c", "Produce las mareas", "Las mareas se deben sobre todo a la atracción de la Luna y el Sol.")], "a", ["osses-1998"]),
  ],
  [("r1", "Explica la surgencia en dos frases.", "El viento empuja el agua de superficie mar adentro. Sube agua más profunda, fría y rica en nutrientes."),
   ("r2", "¿Por qué la costa norte puede tener nubes bajas y poca lluvia?", "Porque la inversión térmica, favorecida por el mar frío y el anticiclón, limita el desarrollo vertical de las nubes.")],
  "Anota una cosa del paisaje de la costa de Coquimbo que ahora puedes explicar.",
  [src("noaa", "NOAA National Ocean Service", "What is upwelling?", "https://oceanservice.noaa.gov/facts/upwelling.html", "Texto principal", ["El viento empuja el agua de superficie", "Sube agua más fría y rica en nutrientes", "Esos nutrientes fertilizan las aguas superficiales", "Las buenas zonas de pesca suelen estar donde la surgencia es común"], HOY),
   src("noaa-nino", "NOAA National Ocean Service", "What are El Niño and La Niña?", "https://oceanservice.noaa.gov/facts/ninonina.html", "Sección El Niño, párrafo sobre vida marina", ["Durante El Niño la surgencia se debilita o se detiene", "Hay menos fitoplancton, lo que afecta a los peces y a quienes se alimentan de ellos"], HOY),
   src("britannica-peru", "Encyclopaedia Britannica", "Peru Current", "https://www.britannica.com/place/Peru-Current", "Artículo completo", ["Corriente fría que fluye hacia el norte por la costa occidental de Sudamérica", "Trae niebla a la costa y contribuye a su aridez", "Aguas de Perú, Chile y Ecuador entre las más ricas en pesca"], HOY),
   src("osses-1998", "Revista de Geografía Norte Grande, 25: 7-13 (1998)", "Osses, Cereceda, Schemenauer, Larrain y Lazaro: Diferencias y similitudes de la niebla entre Iquique (Chile) y Mejía (Perú)", "https://analesliteraturachilena.letras.uc.cl/index.php/RGNG/article/download/42185/34205/107509", "Resultados, a) Factores a escala planetaria, página 8", ["Influencia conjunta del Anticiclón del Pacífico Suroriental y de la Corriente de Humboldt", "Una fuerte inversión térmica impide el desarrollo vertical del estratocúmulo"], HOY)]))

# ------------------------------------------------------------------ cielos-coquimbo r2
L.append(lesson("cielos-coquimbo", "Astronomía", "astronomia", ["observatorios", "Coquimbo", "cielo nocturno"],
  "Por qué el norte de Chile mira al universo", 14,
  ["Identificar condiciones que favorecen un sitio astronómico", "Ubicar observatorios de la Región de Coquimbo"],
  "Antes de leer: ¿qué necesitarías para ver estrellas muy débiles? Haz una lista de tres condiciones.",
  [
    step("condiciones", "Condiciones favorables", [
      "Un buen sitio astronómico necesita muchas noches despejadas, aire seco y estable, y cielos oscuros, lejos de la contaminación lumínica.",
      "Algunas cumbres utilizadas por observatorios pueden quedar por encima de la nubosidad costera baja; ESO muestra un ejemplo de nubes situadas bajo el observatorio de La Silla. Esto ayuda, pero no garantiza una noche despejada."],
      ["eso-lasilla", "eso-nubes"],
      fig(sky, "Silueta de cerros con un observatorio en la cumbre, sobre una franja de nubes bajas.", "Una situación posible en determinados observatorios: la cumbre sobre la nubosidad baja. Esquema sin escala."),
      ("prediccion", "¿Qué ventaja puede tener un observatorio en una cumbre respecto de uno en la costa?", "Puede quedar sobre parte de la nubosidad baja y tener menos aire encima; aun así, eso no asegura un cielo despejado todas las noches.")),
    step("cerros", "Los cerros de la región", [
      "La Silla, del Observatorio Europeo Austral (ESO), está a unos 2.400 metros de altitud y a unos 600 km al norte de Santiago. ESO lo describe como uno de los cielos nocturnos más oscuros de la Tierra.",
      "En la comuna de Vicuña están Cerro Tololo y Cerro Pachón, donde NOIRLab opera instalaciones como el Observatorio Interamericano de Cerro Tololo, Gemini Sur y SOAR. En la cumbre de Cerro Pachón está el Observatorio Vera C. Rubin, cuyo programa LSST contempla un sondeo del cielo nocturno de diez años."],
      ["eso-lasilla", "noirlab-chile", "rubin"], None,
      ("explicacion", "Explica a otra persona por qué una ciudad que crece cerca de un observatorio puede ser un problema.", "Su iluminación puede aclarar el cielo y reducir el contraste, de modo que los objetos débiles se vuelven más difíciles de ver.")),
    step("proteger", "Proteger la oscuridad", [
      "El D.S. N° 1/2022 del Ministerio del Medio Ambiente establece la norma de emisión de luminosidad artificial generada por alumbrados de exteriores. Se publicó en el Diario Oficial el 18 de octubre de 2023.",
      "Según su artículo 1, su objetivo es controlar las emisiones del alumbrado de exteriores para prevenir la contaminación por luminosidad artificial, protegiendo la calidad astronómica de los cielos nocturnos, la salud de las personas y la biodiversidad. Según su artículo 2, se aplica en todo el territorio nacional.",
      "Desde el hemisferio sur, en una noche oscura, se puede observar la Gran Nube de Magallanes, una galaxia satélite de la Vía Láctea."],
      ["ds1-2022", "mma-luminica", "eso-lmc"], None,
      ("prediccion", "¿Por qué un astrónomo suele preferir noches sin luna?", "La luz de la Luna ilumina la atmósfera y reduce el contraste, lo que dificulta ver objetos débiles como galaxias y nebulosas.")),
  ],
  [
    q("q1", "¿Cuál de estas condiciones NO favorece la observación astronómica?", [
      ("a", "Aire seco", "El aire seco sí favorece la observación."),
      ("b", "Contaminación lumínica", "Correcto: la luz artificial aclara el cielo y dificulta ver objetos débiles."),
      ("c", "Altura", "La altura sí suele favorecer: hay menos atmósfera encima.")], "b", ["eso-lasilla"]),
    q("q2", "¿Qué norma chilena regula la luz que emiten los alumbrados de exteriores?", [
      ("a", "El D.S. N° 1/2022 del Ministerio del Medio Ambiente", "Correcto: es la norma de emisión de luminosidad artificial generada por alumbrados de exteriores."),
      ("b", "El Código del Trabajo", "Regula relaciones laborales, no la iluminación exterior."),
      ("c", "Ninguna; la iluminación exterior no está regulada", "Sí existe una norma específica, aplicable en todo el territorio nacional.")], "a", ["ds1-2022"]),
    q("q3", "¿Qué es la Gran Nube de Magallanes?", [
      ("a", "Una nube de tormenta del extremo sur", "Su nombre confunde: no es una nube atmosférica."),
      ("b", "Una galaxia satélite de la Vía Láctea", "Correcto: es visible desde el hemisferio sur."),
      ("c", "Un cometa que vuelve cada año", "No es un cometa: es una galaxia, mucho más lejana que cualquier cometa.")], "b", ["eso-lmc"]),
  ],
  [("r1", "Nombra tres condiciones que favorecen un sitio astronómico.", "Noches despejadas, aire seco y estable, cielo oscuro."),
   ("r2", "Nombra dos cerros con observatorios en la Región de Coquimbo.", "La Silla, Cerro Tololo o Cerro Pachón.")],
  "La próxima noche despejada, compara cuántas estrellas ves con las luces del patio encendidas y luego apagadas durante cinco minutos.",
  [src("eso-lasilla", "European Southern Observatory", "La Silla", "https://www.eso.org/public/teles-instr/lasilla/", "Presentación del observatorio", ["Altitud de 2.400 m", "A unos 600 km al norte de Santiago", "Uno de los cielos nocturnos más oscuros de la Tierra"], HOY),
   src("eso-nubes", "European Southern Observatory", "Sitting at the top of a cloud (Picture of the Week potw1449a, 08-12-2014)", "https://www.eso.org/public/images/potw1449a/", "Descripción de la imagen", ["ESO muestra un ejemplo de nubes situadas bajo el observatorio de La Silla"], HOY),
   src("rubin", "U.S. National Science Foundation", "NSF–DOE Vera C. Rubin Observatory", "https://www.nsf.gov/focus-areas/astronomy-space/rubin-observatory", "Párrafo inicial, presentación de LSST", ["El Observatorio Rubin está en la cumbre de Cerro Pachón, Chile", "El Legacy Survey of Space and Time es un sondeo del cielo nocturno de diez años"], HOY),
   src("noirlab-chile", "NSF NOIRLab", "NOIRLab and Chile", "https://noirlab.edu/public/about/broader-impacts/chile", "Párrafo sobre las instalaciones en Chile (\"the two summits in Vicuña: Cerro Tololo and the neighboring mountaintop of Cerro Pachón\") y lista de instalaciones", ["Cerro Tololo y Cerro Pachón están en Vicuña", "Instalaciones en Chile: CTIO, Gemini Sur, SOAR y Rubin"], HOY),
   src("ds1-2022", "Diario Oficial de la República de Chile, edición N° 43.679", "D.S. N° 1, de 2022, del Ministerio del Medio Ambiente: Establece norma de emisión de luminosidad artificial generada por alumbrados de exteriores", "https://www.diariooficial.interior.gob.cl/publicaciones/2023/10/18/43679/01/2391423.pdf", "Encabezado; artículo 1 (objetivo); artículo 2 (ámbito territorial)", ["Decreto N° 1, Santiago, 5 de enero de 2022, publicado el 18-10-2023", "Objetivo: controlar las emisiones del alumbrado de exteriores protegiendo la calidad astronómica de los cielos nocturnos, la salud de las personas y la biodiversidad", "Se aplica en todo el territorio nacional"], HOY),
   src("mma-luminica", "Ministerio del Medio Ambiente", "Nueva Norma Lumínica (presentación)", "https://luminica.mma.gob.cl/wp-content/uploads/2024/09/01-Nueva-Norma-Luminica.pdf", "Portada y secciones de objetivos y vigencia", ["Fecha de publicación en el Diario Oficial: 18-10-2023"], HOY),
   src("eso-lmc", "European Southern Observatory", "Large Magellanic Cloud (imagen)", "https://eso.org/public/images/magellan-ch17-bardon-cc", "Descripción de la imagen", ["La Gran Nube de Magallanes es una galaxia satélite de la Vía Láctea visible desde el hemisferio sur"], HOY)]))

# ------------------------------------------------------------------ imprenta-gutenberg r2
L.append(lesson("imprenta-gutenberg", "Historia", "historia", ["imprenta", "Renacimiento", "tecnología"],
  "La imprenta de tipos móviles", 12,
  ["Describir los componentes del sistema de Gutenberg", "Explicar qué cambió al poder reutilizar una composición tipográfica"],
  "Antes de leer: ¿cómo se copiaba un libro antes de la imprenta, y cuánto crees que tardaba?",
  [
    step("sistema", "Un sistema completo", [
      "Johannes Gutenberg, nacido y fallecido en Maguncia (Alemania), combinó varias técnicas en un sistema para imprimir con letras de metal reutilizables.",
      "Según Britannica, el sistema incluía una aleación duradera para los tipos, una tinta de base oleosa y una prensa que aplicaba presión pareja sobre la superficie de impresión."],
      ["britannica-gutenberg"],
      fig(tipo, "Bloque rectangular de metal con una letra R invertida en relieve en su extremo superior.", "La letra va invertida para que al imprimir quede al derecho."),
      ("prediccion", "¿Por qué la letra del tipo va al revés?", "Porque al presionar contra el papel la imagen se invierte; así queda legible.")),
    step("biblia", "La Biblia de Gutenberg", [
      "Su obra más conocida es la Biblia de Gutenberg, en latín, terminada hacia 1455. Se la llama también Biblia de 42 líneas porque se imprimió en columnas de 42 líneas.",
      "Según la Biblioteca Estatal de Baviera, se conservan 49 ejemplares más o menos completos. Se cree que se imprimieron unos 180, pero esa cifra es una estimación basada en una sola carta de la época."],
      ["britannica-biblia", "bsb-biblia"], None,
      ("calculo", "Ejercicio hipotético: si un copista escribiera 3 páginas al día, ¿cuántos días tardaría en copiar una obra de 1.280 páginas?", "1.280 / 3 = 426,67 días, es decir, unos 427 días de trabajo para una sola copia. Es un supuesto para comparar, no un dato histórico.")),
    step("efectos", "Qué cambió", [
      "La composición tipográfica permitía reproducir muchas veces un mismo texto sin copiar cada ejemplar a mano. Esto favorecía una mayor uniformidad, aunque había diferencias de impresión, correcciones y acabados hechos a mano: los tres ejemplares de la Morgan Library tienen distintos niveles de ornamentación."],
      ["morgan-ornamentacion"], None,
      ("explicacion", "Como comparación, no como equivalencia histórica: ¿en qué se parece la imprenta a internet en cuanto a copiar y difundir textos?", "Ambos permiten reproducir y difundir un texto a gran escala. La imprenta requiere una composición material; internet utiliza archivos digitales.")),
  ],
  [
    q("q1", "¿Cuál de estos elementos formaba parte del sistema de Gutenberg?", [
      ("a", "Una tinta de base oleosa", "Correcto: Britannica la menciona entre los componentes del sistema."),
      ("b", "Una máquina a vapor", "La máquina a vapor llegó siglos después."),
      ("c", "Papel de celulosa industrial", "El papel industrial moderno es muy posterior.")], "a", ["britannica-gutenberg"]),
    q("q2", "¿Qué ventaja daba la composición con tipos móviles frente a la copia manuscrita?", [
      ("a", "Reutilizar la misma composición para producir muchas copias", "Correcto: el texto se componía una vez y se imprimía muchas veces."),
      ("b", "Que cada ejemplar quedara decorado a mano de forma idéntica", "La decoración a mano variaba entre ejemplares."),
      ("c", "Que el papel durara más", "La duración depende del papel y de la tinta, no del método de composición.")], "a", ["morgan-ornamentacion"]),
    q("q3", "¿Por qué la letra del tipo móvil está invertida?", [
      ("a", "Por tradición de los copistas", "No es una tradición: es una necesidad física."),
      ("b", "Para que al imprimir quede al derecho", "Correcto: la impresión invierte la imagen."),
      ("c", "Para ahorrar metal", "La orientación no cambia la cantidad de metal.")], "b", ["britannica-gutenberg"]),
  ],
  [("r1", "Nombra tres componentes del sistema de Gutenberg.", "Tipos de una aleación metálica, tinta oleosa y prensa."),
   ("r2", "¿Qué permitía la composición tipográfica?", "Reproducir muchas veces un mismo texto sin copiar cada ejemplar a mano, con mayor uniformidad aunque no igualdad absoluta.")],
  "Piensa en un documento de tu trabajo que se reproduce muchas veces. ¿Qué partes deben ser idénticas y cuáles se completan a mano?",
  [src("britannica-gutenberg", "Encyclopaedia Britannica", "Johannes Gutenberg", "https://www.britannica.com/biography/Johannes-Gutenberg", "Resumen inicial y sección sobre la invención", ["Nació y murió en Maguncia", "Aleación metálica duradera, tinta oleosa y prensa de presión pareja"], HOY),
   src("britannica-biblia", "Encyclopaedia Britannica", "Gutenberg Bible", "https://www.britannica.com/topic/Gutenberg-Bible", "Artículo principal", ["Completada hacia 1455 en Maguncia", "Impresa en columnas de 42 líneas"], HOY),
   src("bsb-biblia", "Bayerische Staatsbibliothek (MDZ, Digitale Sammlungen)", "Gutenberg Bible", "https://www.digitale-sammlungen.de/en/gutenberg-bible", "Texto descriptivo de la página", ["Se conservan 49 ejemplares más o menos completos (12 en vitela y 37 en papel)", "Se cree que se imprimieron 180, según una sola carta de Enea Silvio Piccolomini", "La terminación hacia 1455 se basa en una anotación de la encuadernación del ejemplar en papel de París"], HOY),
   src("morgan-ornamentacion", "The Morgan Library & Museum", "Gutenberg Bible: ornamentation", "https://www.themorgan.org/collections/works/gutenberg/ornamentation", "Texto sobre la ornamentación de los ejemplares", ["Los tres ejemplares de la Morgan tienen distintos niveles de ornamentación"], HOY)]))

# ------------------------------------------------------------------ perspectiva-lineal r2
L.append(lesson("perspectiva-lineal", "Arte", "arte", ["Renacimiento", "geometría", "dibujo"],
  "La perspectiva lineal", 11,
  ["Ubicar el punto de fuga y el horizonte en una perspectiva de un punto", "Explicar el origen renacentista del método"],
  "Antes de leer: mira un pasillo largo. ¿Qué le pasa al ancho del pasillo a medida que se aleja?",
  [
    step("fuga", "El punto de fuga", [
      "En este ejemplo de perspectiva de un punto, los bordes horizontales paralelos que se alejan en la misma dirección convergen hacia un punto del horizonte. Otras direcciones pueden tener otros puntos de fuga: también existen perspectivas de dos y tres puntos.",
      "El horizonte de los planos horizontales corresponde a la altura de los ojos de quien observa. Dónde aparece esa línea dentro de una fotografía depende además de hacia dónde apunte la cámara."],
      ["britannica-persp", "getty-2p", "getty-3p"],
      fig(persp, "Cuatro líneas que parten de las esquinas convergen en un punto central sobre una línea horizontal punteada; líneas verticales representan fachadas que se achican.", "Ejemplo de perspectiva de un punto: la línea punteada es el horizonte y las paralelas horizontales convergen en el punto de fuga."),
      ("prediccion", "Si bajas los ojos, ¿cómo cambia la altura desde la que observas el pasillo?", "Cambia tu nivel de observación. La ubicación del horizonte dentro de una foto depende además de dónde apunte la cámara.")),
    step("origen", "Florencia, siglo XV", [
      "Según Britannica, el sistema se habría ideado hacia 1415 y se atribuye a Filippo Brunelleschi. El Metropolitan Museum señala que la perspectiva lineal pudo haber sido desarrollada primero por él.",
      "Leon Battista Alberti explicó sus principios en su tratado sobre la pintura (Della pittura en italiano), que Britannica fecha en 1435 y que el Metropolitan describe como un manual fundamental para artistas."],
      ["britannica-persp", "met-renacimiento"], None,
      ("explicacion", "Toma una foto de una calle recta y plana, con la cámara horizontal, y prolonga sus bordes con una regla. ¿Dónde se cruzan?", "Cerca de un punto sobre el horizonte. Si la calle sube, baja o la cámara se inclina, el resultado cambia.")),
    step("atmosfera", "Más allá de la regla", [
      "Los pintores combinan la perspectiva lineal con la perspectiva atmosférica. A gran distancia, los contrastes entre luz y sombra suelen verse menos marcados, los colores oscuros tienden al azul y los bordes se ven menos nítidos. Por eso las montañas lejanas pueden verse azuladas."],
      ["britannica-aerea"], None,
      ("prediccion", "En una foto del Valle de Elqui, ¿qué cerros suelen verse más azulados: los cercanos o los lejanos?", "Los lejanos suelen verse más azulados y con menos contraste, aunque depende de la luz y de las condiciones del aire.")),
  ],
  [
    q("q1", "En una perspectiva de un punto, ¿dónde convergen los bordes horizontales paralelos que se alejan?", [
      ("a", "En el punto de fuga, sobre el horizonte", "Correcto, para ese caso y esas direcciones."),
      ("b", "En el borde inferior del cuadro", "Se acercan entre sí hacia el horizonte, no hacia abajo."),
      ("c", "Siempre en el centro exacto del cuadro", "El punto de fuga puede estar en cualquier lugar del horizonte.")], "a", ["britannica-persp"]),
    q("q2", "Dibujas en perspectiva de un punto una línea férrea recta y plana vista desde el andén, mirando a lo largo de la vía. ¿Qué haces con los rieles?", [
      ("a", "Los dibujo paralelos en el papel", "En este dibujo perspectivo, mantenerlos paralelos no representa cómo se alejan."),
      ("b", "Los hago converger hacia un punto del horizonte", "Correcto: es el principio de la perspectiva de un punto."),
      ("c", "Los separo a medida que se alejan", "Eso invierte el efecto de la distancia.")], "b", ["britannica-persp"]),
    q("q3", "¿Quién explicó por escrito los principios de la perspectiva lineal en un tratado sobre la pintura?", [
      ("a", "Leon Battista Alberti", "Correcto: su tratado Della pittura explica esos principios."),
      ("b", "Filippo Brunelleschi", "A Brunelleschi se le atribuye haberlo desarrollado primero; el tratado es de Alberti."),
      ("c", "Leonardo da Vinci", "Leonardo nació en 1452, después del tratado.")], "a", ["britannica-persp", "met-renacimiento"]),
  ],
  [("r1", "En una perspectiva de un punto, ¿qué es el punto de fuga?", "El punto del horizonte hacia el que convergen las paralelas horizontales que se alejan en la misma dirección."),
   ("r2", "¿A qué corresponde la altura del horizonte?", "A la altura de los ojos de quien observa; su posición en una foto depende también de hacia dónde apunte la cámara.")],
  "Busca en tu celular una foto de una calle recta y marca con el dedo dónde convergen sus bordes.",
  [src("britannica-persp", "Encyclopaedia Britannica", "Linear perspective", "https://www.britannica.com/art/linear-perspective", "Párrafo inicial", ["Paralelas convergen en un único punto de fuga sobre el horizonte, en la perspectiva de un punto", "Ideado hacia 1415, atribuido a Brunelleschi", "Documentado por Alberti en 1435 (Della pittura)"], HOY),
   src("met-renacimiento", "The Metropolitan Museum of Art", "Architecture in Renaissance Italy (ensayo)", "https://www.metmuseum.org/essays/architecture-in-renaissance-italy", "Pasaje sobre Brunelleschi y el tratado de Alberti", ["La perspectiva lineal pudo haber sido desarrollada primero por Brunelleschi", "Della pittura de Alberti fue un manual fundamental que explica los principios de la perspectiva lineal"], HOY),
   src("getty-2p", "Getty Research Institute", "Art & Architecture Thesaurus, registro 300034309 (two-point perspective)", "http://vocab.getty.edu/page/aat/300034309", "Apartado Note. Verificado por ChatGPT N°9; Claude no pudo abrir el registro el 19-10-2026 (error de conexión)", ["Existe la perspectiva de dos puntos"], None),
   src("getty-3p", "Getty Research Institute", "Art & Architecture Thesaurus, registro 300067713 (three-point perspective system)", "http://vocab.getty.edu/page/aat/300067713", "Apartado Note, acepción geométrica: tres grupos de paralelas que retroceden hacia sus puntos de fuga. Verificado por ChatGPT N°9; Claude no pudo abrir el registro el 19-10-2026 (error de conexión)", ["En la perspectiva de tres puntos, tres grupos de paralelas retroceden hacia sus respectivos puntos de fuga"], None),
   src("britannica-aerea", "Encyclopaedia Britannica", "Aerial perspective", "https://www.britannica.com/art/aerial-perspective", "Definición y párrafo siguiente", ["Contrastes de luz y sombra menos extremos a gran distancia", "Los colores oscuros lejanos tienden al azul; montañas lejanas azuladas", "Bordes y contornos menos nítidos"], HOY)]))

# ------------------------------------------------------------------ bauhaus r2
L.append(lesson("bauhaus", "Diseño", "arte", ["diseño", "siglo XX", "retícula"],
  "La Bauhaus y la forma útil", 12,
  ["Ubicar la Bauhaus en el tiempo y sus sedes", "Reconocer el uso de retículas en interfaces actuales"],
  "Antes de leer: piensa en una silla que te parezca \"moderna\". ¿Qué tiene y qué no tiene?",
  [
    step("escuela", "De Weimar a Berlín", [
      "La Bauhaus fue una escuela alemana de diseño fundada en 1919 en Weimar por el arquitecto Walter Gropius. Funcionó en Weimar (1919–1925), en Dessau (1925–1932) y en Berlín (1932–1933).",
      "En Dessau, la mayoría nacionalsocialista del concejo municipal decidió su cierre en 1932. En Berlín, desde abril de 1933 los nacionalsocialistas sellaron el edificio; Ludwig Mies van der Rohe anunció la disolución en agosto de 1933.",
      "Comenzó con un enfoque artesanal que buscaba unir arte y oficio. En 1923 Gropius reorientó la escuela hacia el diseño para la producción en masa, con el lema \"Arte en la industria\"."],
      ["bauhaus-koop", "met-bauhaus"],
      fig(bau, "Un triángulo relleno, un cuadrado y un círculo dibujados con trazo grueso.", "Composición ilustrativa con formas básicas."),
      ("prediccion", "En el curso preliminar, los estudiantes trabajaban con materiales, color y forma antes de especializarse. ¿Qué crees que aprendían al combinar figuras simples como estas?", "A observar relaciones de tamaño, peso visual, color y equilibrio entre formas, antes de diseñar objetos concretos.")),
    step("reticula", "La retícula", [
      "Ordenar una página o una pantalla con una grilla invisible da coherencia: cada elemento se alinea con algo.",
      "Las retículas se utilizan en sistemas actuales de diseño. El IBM Design Language, por ejemplo, define márgenes y una división en columnas y filas iguales que da estructura a la composición."],
      ["ibm-grid"], None,
      ("explicacion", "Abre la app de tu banco o de correo. Señala dos márgenes o columnas que se repitan.", "Es frecuente encontrar márgenes laterales iguales, íconos del mismo tamaño y textos alineados a una misma línea.")),
    step("legado", "El legado", [
      "Del taller de muebles de Marcel Breuer salieron sillas livianas de tubo de acero. La escuela usaba tipografías sin serifa y fotografía en sus impresos, por ejemplo en el trabajo de Herbert Bayer. El edificio de Gropius en Dessau usó estructura de acero y un muro cortina de vidrio.",
      "Una pregunta útil al diseñar: para qué sirve cada elemento."],
      ["met-bauhaus"], None,
      ("explicacion", "Elige un objeto de tu escritorio y nombra un elemento que sobra y uno que no puede faltar.", "La respuesta es personal; lo importante es justificar cada elemento por su función.")),
  ],
  [
    q("q1", "¿En qué ciudad se fundó la Bauhaus?", [
      ("a", "Weimar", "Correcto: en 1919."),
      ("b", "Dessau", "Dessau fue su segunda sede, desde 1925."),
      ("c", "París", "La Bauhaus fue una escuela alemana.")], "a", ["bauhaus-koop"]),
    q("q2", "Diseñas una planilla de rendiciones para que se lea con claridad. ¿Qué haces?", [
      ("a", "Agregar adornos para que se vea profesional", "El adorno sin función suele dificultar la lectura."),
      ("b", "Alinear columnas en una retícula y quitar lo que no cumple función", "Correcto: la claridad funcional facilita la lectura."),
      ("c", "Usar muchos colores distintos", "El color sin función agrega ruido.")], "b", ["ibm-grid"]),
    q("q3", "¿Cómo terminó la Bauhaus en 1933?", [
      ("a", "Por falta de alumnos", "No fue esa la causa."),
      ("b", "Se disolvió en Berlín tras el cierre y la presión de los nacionalsocialistas", "Correcto: sellaron el edificio en abril y Mies anunció la disolución en agosto de 1933."),
      ("c", "Porque Gropius se jubiló", "Gropius había dejado la dirección en 1928; no fue la causa del fin.")], "b", ["bauhaus-koop"]),
  ],
  [("r1", "Nombra las tres sedes de la Bauhaus en orden.", "Weimar, Dessau y Berlín."),
   ("r2", "¿Qué es una retícula en diseño?", "Una grilla invisible de márgenes, columnas y filas que ordena y alinea los elementos.")],
  "Revisa un documento tuyo y alinea todo a dos márgenes comunes.",
  [src("bauhaus-koop", "Bauhaus Kooperation Berlin Dessau Weimar", "What exactly was the Bauhaus?", "https://bauhauskooperation.com/knowledge/the-bauhaus/bauhaus-at-a-glance", "Secciones sobre Weimar; Dessau (1925–1932), último párrafo; Berlín (1932–1933), circular del 10-08-1933", ["Fundada en Weimar en 1919 por Walter Gropius", "Dessau 1925–1932; Gropius dirigió hasta 1928", "La Bauhaus de Dessau cerró el 30-09-1932 por decisión de la mayoría nacionalsocialista del concejo municipal", "Berlín 1932–1933: en abril de 1933 se selló el edificio; Mies anunció la disolución el 10-08-1933"], HOY),
   src("met-bauhaus", "The Metropolitan Museum of Art", "The Bauhaus, 1919–1933 (ensayo)", "https://www.metmuseum.org/essays/the-bauhaus-1919-1933", "Párrafos sobre objetivos, curso preliminar, giro de 1923 y talleres", ["Inicio artesanal que buscaba unir arte y oficio", "Curso preliminar de materiales, color y forma", "En 1923, giro hacia el diseño para la producción en masa (\"Art into Industry\")", "Sillas de tubo de acero de Breuer; tipografía sin serifa y fotografía; edificio de Dessau con estructura de acero y muro cortina"], HOY),
   src("ibm-grid", "IBM Design Language", "2x Grid", "https://www.ibm.com/design/language/2x-grid/", "Apartados Margins y Columns and rows", ["Los márgenes separan el contenido del borde", "Columnas y filas dan estructura a la composición y deben ser iguales"], HOY)]))

# ------------------------------------------------------------------ arco-panteon r2
L.append(lesson("arco-panteon", "Arquitectura", "arte", ["Roma", "estructuras", "hormigón"],
  "El arco, la bóveda y el Panteón", 14,
  ["Explicar por qué un arco de piedra trabaja principalmente a compresión", "Describir cómo se redujo la masa de la cúpula del Panteón"],
  "Antes de leer: ¿por qué un puente de piedra antiguo puede seguir en pie después de 2.000 años?",
  [
    step("compresion", "El arco trabaja a compresión", [
      "Las piedras de un arco, llamadas dovelas, tienen forma de cuña y se apoyan unas en otras. Por el arco recorren principalmente fuerzas de compresión.",
      "La dovela central superior se llama clave. Un arco de fábrica como este tiende a abrirse en su base: produce un empuje horizontal que carga sobre los apoyos, y la estructura que lo rodea, como muros o contrafuertes, debe resistirlo."],
      ["britannica-arco", "engrome-domos"],
      fig(arch, "Nueve bloques en forma de cuña forman un semicírculo; el bloque central está destacado; dos flechas en la base apuntan hacia afuera.", "Modelo de arco de fábrica con apoyos que deben resistir sus empujes."),
      ("prediccion", "¿Qué puede pasar si los apoyos de un arco de fábrica ceden hacia afuera?", "El arco puede perder estabilidad, porque deja de tener dónde descargar sus empujes.")),
    step("cupula", "Del arco a la cúpula", [
      "Si giras la forma de un arco sobre su eje vertical obtienes la forma de una cúpula. Es una analogía geométrica: una cúpula no funciona exactamente como un arco.",
      "El Panteón de Roma fue reconstruido durante el reinado de Adriano (117–138 d. C.). Su cúpula de hormigón tiene una luz interior de unos 43 metros, y la altura interior es aproximadamente igual a esa luz: cabría una esfera."],
      ["uw-panteon"], None,
      ("calculo", "Si la luz interior es 43,2 m, como indica la fuente, ¿qué volumen tendría la esfera que cabe en el interior?", "V = (4/3) × π × r³ con r = 21,6 m: (4/3) × 3,1416 × 10.077,696 = 42.213,5 m³ (cálculo con π = 3,1416, redondeado a un decimal). El resultado es aproximado, igual que la medida.")),
    step("trucos", "Cómo se redujo la masa", [
      "En la cúpula se usaron áridos distintos: más densos abajo y más livianos, como la piedra pómez, hacia la parte alta. Así la densidad disminuye hacia arriba.",
      "Los casetones forman un patrón decorativo y retiran parte del material de la cúpula. En la cima, el óculo es la principal entrada de luz cenital."],
      ["uw-panteon", "engrome-domos"], None,
      ("explicacion", "Explica por qué conviene que la parte alta de una cúpula pese menos.", "Reducir la masa de la parte superior disminuye las cargas que debe soportar el resto de la estructura.")),
  ],
  [
    q("q1", "¿A qué esfuerzo trabaja principalmente un arco de piedra?", [
      ("a", "Compresión", "Correcto: las dovelas se apoyan unas en otras."),
      ("b", "Tracción", "La piedra resiste mal la tracción; la forma del arco busca evitarla."),
      ("c", "Torsión", "Un arco bien cargado no trabaja principalmente a torsión.")], "a", ["britannica-arco"]),
    q("q2", "Debes revisar un muro antiguo que sostiene un arco de piedra. ¿Qué empuje debe resistir?", [
      ("a", "Un empuje horizontal hacia afuera", "Correcto: el arco tiende a abrirse en su base y carga sus apoyos."),
      ("b", "Un empuje hacia arriba", "El peso del arco empuja hacia abajo y hacia los lados, no hacia arriba."),
      ("c", "Ninguno; el arco se sostiene solo", "Sin apoyos que resistan el empuje, el arco puede perder estabilidad.")], "a", ["engrome-domos"]),
    q("q3", "¿Qué material liviano se usó en la parte alta de la cúpula del Panteón?", [
      ("a", "Basalto", "Los materiales más densos se usaron abajo."),
      ("b", "Piedra pómez", "Correcto: es liviana y se usó hacia la parte alta."),
      ("c", "Acero", "La cúpula es de hormigón, sin acero.")], "b", ["uw-panteon", "engrome-domos"]),
  ],
  [("r1", "¿Qué es la clave de un arco?", "La dovela central superior del arco."),
   ("r2", "Nombra dos recursos con que se redujo la masa de la cúpula del Panteón.", "Áridos más livianos hacia arriba, como la piedra pómez, y los casetones, que retiran parte del material.")],
  "Busca un arco en un edificio de tu ciudad e identifica dónde está su clave.",
  [src("britannica-arco", "Encyclopaedia Britannica", "Arch (architecture)", "https://britannica.com/technology/arch-architecture", "Resumen y pies de los diagramas", ["La construcción del arco depende de la cuña", "Dovelas en forma de cuña forman la curva; la clave está arriba al centro", "Las fuerzas de compresión recorren la estructura"], HOY),
   src("uw-panteon", "University of Washington, Honors Program in Rome (trabajo educativo firmado en 2005)", "The Pantheon", "https://depts.washington.edu/hrome/Authors/zinnia/Pantheon/pub_zbarticle_view_printable.html", "Sección Description", ["Reconstruido bajo Adriano (117–138)", "Luz interior de 43,2 m; altura igual a la luz", "El óculo es la fuente de luz del interior", "Basalto en la base y piedra pómez arriba", "Íntegramente de hormigón, sin acero"], HOY),
   src("engrome-domos", "Engineering Rome (programa de estudios en Roma, University of Washington)", "Studying Domes: Engineering of the Roman Pantheon and Brunelleschi's Duomo", "https://engineeringrome.org/studying-domes-engineering-of-the-roman-pantheon-and-brunelleschis-duomo/", "Secciones Engineering of a Dome (párrafo que comienza \"The distributed load on the arch…\") y Domes as 3D Arches; párrafos sobre áridos y casetones", ["Un arco o cúpula tiende a abrirse en la base: el empuje horizontal carga los apoyos", "El empuje horizontal es resistido principalmente por la estructura circundante", "Áridos que reducen la densidad hacia la parte alta, con piedra pómez", "Los casetones probablemente buscaban también reducir peso"], HOY)]))
