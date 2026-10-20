# Lecciones en guía editorial v1.1 (acordada en MENSAJE DE CLAUDE N°11 y RESPUESTA DE CHATGPT N°12).
# Se ejecuta dentro de gen_lessons.py y comparte sus helpers.
HOY11 = "2026-10-20"

def lesson11(id, disciplina, familia, etiquetas, titulo, minutos, objetivos, pregunta, contexto, pasos, quiz, repaso, cierre, dato, fuentes):
    les = lesson(id, disciplina, familia, etiquetas, titulo, minutos, objetivos, pregunta, pasos, quiz, repaso, cierre, fuentes)
    les["schemaVersion"] = "1.1"
    if contexto: les["entrada"]["contexto"] = contexto
    if dato: les["datoCurioso"] = {"texto": dato[0], "fuenteIds": dato[1]}
    return les

# ------------------------------------------------------------------ piloto: cielo-azul r1
cielo_fig = svg("0 0 320 180",
    arrow_def("cielo-azul-f1-ah") +
    '<rect width="320" height="180" class="as-svg__surface"/>'
    '<circle cx="40" cy="40" r="20" class="as-svg__ink as-svg__accent" stroke-width="2.5"/>'
    '<text x="40" y="80" text-anchor="middle" class="as-svg__label" font-size="11">sol</text>'
    '<line x1="62" y1="48" x2="250" y2="130" class="as-svg__ink" stroke-width="2" marker-end="url(#cielo-azul-f1-ah)"/>'
    '<text x="72" y="28" class="as-svg__label as-svg__muted" font-size="10">luz con todos los colores</text>'
    '<circle cx="150" cy="86" r="4" class="as-svg__ink"/>'
    '<line x1="150" y1="86" x2="150" y2="46" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#cielo-azul-f1-ah)"/>'
    '<line x1="150" y1="86" x2="186" y2="52" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#cielo-azul-f1-ah)"/>'
    '<line x1="150" y1="86" x2="110" y2="120" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#cielo-azul-f1-ah)"/>'
    '<line x1="150" y1="86" x2="196" y2="110" class="as-svg__ink as-svg__accent" stroke-width="2" marker-end="url(#cielo-azul-f1-ah)"/>'
    '<text x="160" y="172" text-anchor="middle" class="as-svg__label" font-size="9">el aire desvía el azul en todas direcciones</text>'
    '<circle cx="270" cy="140" r="8" class="as-svg__ink"/>'
    '<text x="290" y="144" text-anchor="middle" class="as-svg__label" font-size="11">tú</text>',
    "La luz del sol cruza el aire y el azul se desvía en muchas direcciones")

L.append(lesson11("cielo-azul", "Ciencia cotidiana", "fisica", ["luz", "colores", "cielo"],
  "¿Por qué el cielo es azul?", 6,
  ["Explicar por qué el cielo es azul", "Explicar por qué el atardecer se ve naranjo"],
  "¿Por qué el cielo es azul y el atardecer, naranjo?",
  "Es el mismo sol al mediodía y al atardecer. ¿Qué cambió?",
  [
    step("colores", "La luz del sol trae todos los colores", [
      "La luz del sol parece blanca, pero en realidad trae mezclados todos los colores del arcoíris.",
      "La luz viaja como ondas, parecidas a las olas del mar. Cada color tiene ondas de distinto largo: las del azul son más cortas que las del rojo."],
      ["nasa-cielo"], None, None),
    step("desvio", "El aire desvía el azul", [
      "Cuando la luz entra al aire, las moléculas diminutas que lo forman desvían el azul en todas direcciones. Al rojo y al amarillo los desvían mucho menos.",
      "Ese azul desviado te llega desde todas partes del cielo. Por eso, la mayor parte del tiempo, vemos el cielo azul."],
      ["nasa-cielo", "britannica-rayleigh"],
      fig(cielo_fig, "El sol a la izquierda envía una flecha de luz hacia una persona a la derecha. En el camino, desde un punto salen cuatro flechas cortas en distintas direcciones: es la luz azul desviada por el aire.", "Esquema simple, sin escala."),
      ("prediccion", "Imagina un aire que desviara más el rojo que el azul. ¿De qué color se vería el cielo?", "Se vería rojizo, porque el color que llega desde todas partes del cielo es el que el aire desvía más. Es solo un ejercicio para pensar: en la Tierra, el aire desvía más el azul.")),
    step("atardecer", "Al atardecer, la luz hace un camino más largo", [
      "Cuando el sol está bajo, su luz tiene que cruzar mucho más aire para llegar hasta ti.",
      "En ese camino largo, gran parte del azul se desvía antes de llegar directo a tus ojos. Lo que sigue derecho es, sobre todo, el amarillo, el naranjo y el rojo.",
      "El polvo y otras partículas del aire también desvían el azul, y pueden hacer que el atardecer se vea todavía más rojo."],
      ["nasa-cielo"], None, None),
  ],
  [
    q("q1", "¿Por qué vemos el cielo azul?", [
      ("a", "Porque el aire desvía la luz azul en todas direcciones", "Así es: ese azul desviado nos llega desde todo el cielo."),
      ("b", "Porque el cielo refleja el color del mar", "Es una idea muy repetida, pero no es la explicación: el azul viene de cómo el aire desvía la luz del sol."),
      ("c", "Porque la luz del sol es azul", "La luz del sol trae todos los colores mezclados; el aire desvía sobre todo el azul.")], "a", ["nasa-cielo"]),
    q("q2", "Vas por la carretera al atardecer y el sol, ya bajo, se ve naranjo. ¿Qué le pasó a su luz?", [
      ("a", "Cruzó mucho aire y gran parte del azul se desvió en el camino", "Así es: llegan directo sobre todo el amarillo, el naranjo y el rojo."),
      ("b", "El sol cambia de color al final del día", "El sol es el mismo; lo que cambia es el largo del camino que recorre su luz por el aire."),
      ("c", "El aire se tiñe de naranjo en la tarde", "El aire no se tiñe: desvía el azul y deja pasar más el naranjo y el rojo.")], "a", ["nasa-cielo"]),
  ],
  [("r1", "¿Por qué el cielo es azul?", "Porque el aire desvía la luz azul en todas direcciones, y ese azul nos llega desde todo el cielo."),
   ("r2", "¿Por qué el atardecer se ve naranjo?", "Porque la luz cruza mucho más aire y gran parte del azul se desvía en el camino; llegan sobre todo el amarillo, el naranjo y el rojo.")],
  "La próxima tarde despejada, compara el color del cielo justo encima de ti con el color cerca del horizonte, donde se pone el sol.",
  ("En Marte, al atardecer, el cielo cerca del Sol puede verse azulado. Allí interviene el polvo fino de su atmósfera, que deja pasar mejor la luz azul. El robot Curiosity de la NASA lo fotografió en abril de 2015.", ["jpl-marte"]),
  [src("nasa-cielo", "NASA Space Place", "Why Is the Sky Blue?", "https://spaceplace.nasa.gov/blue-sky/en/", "Secciones de la luz blanca y las ondas; por qué el cielo es azul; por qué el atardecer es rojo", ["La luz del sol se ve blanca, pero está formada por todos los colores del arcoíris", "La luz viaja en ondas; las ondas de la luz azul son más cortas que las de la roja", "Las moléculas diminutas del aire dispersan la luz azul en todas direcciones; por eso vemos el cielo azul la mayor parte del tiempo", "Con el sol bajo, la luz cruza más atmósfera; se dispersa aún más el azul y el rojo y el amarillo pasan derecho", "El polvo, la contaminación y otros aerosoles también dispersan la luz azul"], HOY11),
   src("britannica-rayleigh", "Encyclopaedia Britannica", "Rayleigh scattering", "https://www.britannica.com/science/Rayleigh-scattering", "Párrafo inicial", ["La dispersión de Rayleigh produce el color azul del cielo iluminado por el sol", "Las longitudes de onda más cortas se dispersan mucho más"], HOY11),
   src("jpl-marte", "NASA Jet Propulsion Laboratory", "Sunset in Mars' Gale Crater (PIA19400)", "https://www.jpl.nasa.gov/images/sunset-in-mars-gale-crater", "Descripción de la imagen", ["Imagen tomada al cierre del sol 956 de la misión, el 15 de abril de 2015", "El polvo tiene partículas finas que permiten que la luz azul atraviese la atmósfera con más eficiencia", "Los colores azules se mantienen más cerca de la zona del cielo donde está el sol"], HOY11)]))
