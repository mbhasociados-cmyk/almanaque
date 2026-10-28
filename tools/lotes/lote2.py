# Lote 2 (opción A, 22-10-2026): versiones en tarjetas (esquema 2.0) de las lecciones del 23 al 26 de octubre,
# que estaban en el formato antiguo (1.0) y la interfaz v3 no muestra. Aprobado por Max el 22-10-2026.
# Son revisiones nuevas: las revisiones anteriores quedan intactas. Fuentes abiertas y comprobadas el 22-10-2026.
# Salida: borradores/lote2/
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from almanaque_lib import card, src, lesson, write

HOY = "2026-10-22"
LOTE = []

# ------------------------------------------------------------------ 23-10 perspectiva lineal (r4)
LOTE.append(lesson("perspectiva-lineal", "Arte", "arte",
  "¿Cómo se pinta la profundidad?", "Un invento del Renacimiento que todavía usamos.",
  [card("c1", "portada", titulo="¿Cómo se pinta la profundidad?", texto="Una pintura es plana, pero puede parecer una calle que se aleja. ¿Cómo se logra esa ilusión?", fuentes=["brit-lineal"]),
   card("c2", "pregunta", pregunta="En un dibujo con perspectiva, ¿qué hacen las líneas paralelas, como los bordes de una calle?", correctaId="a", opciones=[
     ("a", "Se juntan en un punto sobre el horizonte", "¡Así es! Ese punto se llama punto de fuga."),
     ("b", "Siguen separadas a la misma distancia", "En la realidad sí, pero en el dibujo con perspectiva se van juntando hasta un punto del horizonte."),
     ("c", "Se curvan hacia arriba", "No se curvan: siguen rectas y se juntan en un punto del horizonte.")], fuentes=["brit-lineal"]),
   card("c3", "idea", titulo="El punto de fuga", texto="La perspectiva lineal es un sistema para crear la ilusión de profundidad en una superficie plana. En ella, las líneas paralelas se juntan en un punto de la línea del horizonte.", fuentes=["brit-lineal"]),
   card("c4", "idea", titulo="Florencia, hacia 1415", texto="Se cree que el arquitecto italiano Filippo Brunelleschi desarrolló este sistema hacia el año 1415.", fuentes=["brit-lineal", "met-renacimiento"]),
   card("c5", "revelar", titulo="Las reglas por escrito", texto="Unos veinte años después, alguien explicó las reglas de la perspectiva para que cualquier pintor pudiera usarlas. ¿Quién fue?",
        revelado="Leon Battista Alberti, en su tratado Sobre la pintura (Della pittura), de 1435. Fue un manual fundamental para los artistas.", fuentes=["brit-lineal", "met-renacimiento"]),
   card("c6", "idea", titulo="El aire también pinta", texto="Los pintores usan además la perspectiva aérea: a gran distancia, las luces y sombras contrastan menos, los bordes se ven menos nítidos y los objetos oscuros tienden al azul.", fuentes=["brit-aerea"]),
   card("c7", "pregunta", pregunta="En un paisaje pintado con perspectiva aérea, ¿cómo se ven las montañas lejanas?", correctaId="b", opciones=[
     ("a", "Más oscuras y nítidas que las cercanas", "Al revés: a lo lejos el contraste baja y los bordes se suavizan."),
     ("b", "Azuladas y con bordes suaves", "¡Correcto! Por eso las montañas lejanas se ven azuladas."),
     ("c", "Del mismo color que las cercanas", "No: con la distancia los objetos oscuros tienden al azul.")], fuentes=["brit-aerea"]),
   card("c8", "dato", texto="Leonardo da Vinci le dio el nombre de perspectiva aérea en su Tratado de la pintura, pero la técnica ya aparecía en pinturas murales de la antigua Grecia y Roma.", fuentes=["brit-aerea"])],
  ("La perspectiva", ["En la perspectiva lineal, las líneas paralelas se juntan en un punto del horizonte y eso crea la ilusión de profundidad.",
                      "Se atribuye a Brunelleschi, hacia 1415, y Alberti explicó sus reglas por escrito en 1435.",
                      "En la perspectiva aérea, lo lejano se ve con menos contraste, bordes suaves y tonos azulados."]),
  [src("brit-lineal", "Encyclopaedia Britannica", "Linear perspective", "https://www.britannica.com/art/linear-perspective", "Texto principal",
       ["Sistema para crear la ilusión de profundidad en una superficie plana", "Las líneas paralelas se juntan en un punto de la línea del horizonte", "Se cree que Brunelleschi lo desarrolló hacia 1415", "Alberti lo registró en Della pittura en 1435"],
       ["c1", "c2", "c3", "c4", "c5"], HOY),
   src("met-renacimiento", "The Metropolitan Museum of Art", "Architecture in Renaissance Italy (ensayo)", "https://www.metmuseum.org/essays/architecture-in-renaissance-italy", "Párrafos sobre Brunelleschi y Alberti",
       ["La perspectiva lineal pudo haber sido desarrollada primero por Brunelleschi", "Della pittura de Alberti fue un manual fundamental para artistas que explicaba los principios de la perspectiva lineal"],
       ["c4", "c5"], HOY),
   src("brit-aerea", "Encyclopaedia Britannica", "Aerial perspective", "https://www.britannica.com/art/aerial-perspective", "Texto principal",
       ["A gran distancia los contrastes de luz y sombra son menos extremos", "Los objetos oscuros lejanos tienden al azul; las montañas lejanas se ven azuladas", "Los bordes lejanos se ven menos nítidos", "Leonardo da Vinci le dio el nombre en su Tratado de la pintura", "La técnica aparece en pinturas murales grecorromanas"],
       ["c6", "c7", "c8"], HOY)],
  revision=4))

# ------------------------------------------------------------------ 24-10 corriente de Humboldt (r3)
LOTE.append(lesson("corriente-humboldt", "Geografía", "geografia",
  "¿Por qué el mar de Chile es tan frío?", "Una corriente que corre hacia el norte.",
  [card("c1", "portada", titulo="¿Por qué el mar de Chile es tan frío?", texto="Quien se mete al mar en Chile lo nota: el agua es fría. Detrás de eso hay una corriente con nombre propio.", fuentes=["brit-humboldt"]),
   card("c2", "idea", titulo="Un río frío dentro del mar", texto="La corriente de Humboldt, también llamada corriente del Perú, es una corriente de agua fría del Pacífico. Avanza hacia el norte por la costa de Sudamérica: desde Chile, pasando por Perú, hacia Ecuador.", fuentes=["brit-humboldt"]),
   card("c3", "pregunta", pregunta="¿Hacia dónde avanza la corriente de Humboldt?", correctaId="a", opciones=[
     ("a", "Hacia el norte, a lo largo de la costa", "¡Exacto! Va desde Chile hacia Perú y Ecuador."),
     ("b", "Hacia el sur, hacia la Antártica", "Al revés: avanza hacia el norte."),
     ("c", "Hacia el continente, entrando en él", "No: corre a lo largo de la costa, hacia el norte.")], fuentes=["brit-humboldt"]),
   card("c4", "idea", titulo="Agua que sube desde abajo", texto="El viento empuja el agua de la superficie mar adentro, y desde lo profundo sube agua más fría a reemplazarla. Eso se llama surgencia, y hace aún más fría la corriente.", fuentes=["noaa-surgencia", "brit-humboldt"]),
   card("c5", "idea", titulo="Un mar lleno de vida", texto="El agua que sube trae muchos nutrientes, que alimentan al plancton. Por eso el mar frente a Chile, Perú y Ecuador está entre las mejores zonas de pesca del mundo, por ejemplo de anchoveta.", fuentes=["noaa-surgencia", "brit-humboldt"]),
   card("c6", "revelar", titulo="¿Por qué se llama Humboldt?", texto="El nombre de la corriente recuerda a un científico. ¿Qué hizo?",
        revelado="Alexander von Humboldt midió en 1802 lo fría que era esta corriente comparada con el aire y el mar que la rodean.", fuentes=["brit-humboldt"]),
   card("c7", "pregunta", pregunta="Durante el fenómeno de El Niño, la surgencia se debilita o se detiene. ¿Qué pasa entonces?", correctaId="b", opciones=[
     ("a", "Hay más peces que nunca", "Al revés: sin surgencia llegan menos nutrientes y eso afecta a los peces."),
     ("b", "Llegan menos nutrientes, hay menos plancton y eso afecta a los peces", "¡Así es! El efecto sigue por toda la cadena de alimentación."),
     ("c", "El agua se vuelve más fría", "No: la surgencia es la que trae el agua fría, y durante El Niño se debilita.")], fuentes=["noaa-nino"]),
   card("c8", "dato", texto="Esa misma agua fría lleva niebla a la costa y ayuda a que esa franja sea una de las zonas más áridas del mundo.", fuentes=["brit-humboldt"])],
  ("La corriente de Humboldt", ["Es una corriente fría que avanza hacia el norte por la costa de Chile, Perú y Ecuador.",
                                "La surgencia sube agua fría y llena de nutrientes, por eso es una de las mejores zonas de pesca del mundo.",
                                "Durante El Niño la surgencia se debilita, llegan menos nutrientes y eso afecta a los peces."]),
  [src("brit-humboldt", "Encyclopaedia Britannica", "Peru Current", "https://www.britannica.com/place/Peru-Current", "Texto principal",
       ["Corriente de agua fría del Pacífico suroriental, también llamada corriente de Humboldt", "Fluye hacia el norte por la costa occidental de Sudamérica, desde Chile, por Perú, hacia Ecuador", "La surgencia intensifica su flujo frío y lleva nutrientes que favorecen el plancton", "Las aguas de Perú, Chile y Ecuador están entre las mayores zonas de pesca del mundo, de anchoveta y peces mayores", "Humboldt midió en 1802 su frialdad respecto del aire y el mar que la rodean", "Lleva niebla a la costa y contribuye a que sea una de las zonas más áridas del mundo"],
       ["c1", "c2", "c3", "c4", "c5", "c6", "c8"], HOY),
   src("noaa-surgencia", "NOAA National Ocean Service", "What is upwelling?", "https://oceanservice.noaa.gov/facts/upwelling.html", "Texto principal",
       ["El viento empuja el agua de superficie y sube agua más fría desde abajo para reemplazarla", "El agua que sube es rica en nutrientes", "Las zonas de surgencia suelen ser buenas zonas de pesca"],
       ["c4", "c5"], HOY),
   src("noaa-nino", "NOAA National Ocean Service", "What are El Niño and La Niña?", "https://oceanservice.noaa.gov/facts/ninonina.html", "Sección sobre El Niño",
       ["Durante El Niño la surgencia se debilita o se detiene", "Sin nutrientes de lo profundo hay menos fitoplancton frente a la costa", "Eso afecta a los peces que comen fitoplancton y a lo que se alimenta de peces"],
       ["c7"], HOY)],
  revision=3))

# ------------------------------------------------------------------ 25-10 Bauhaus (r4)
LOTE.append(lesson("bauhaus", "Diseño", "arte",
  "¿Qué fue la Bauhaus?", "La escuela que quiso diseñar mejor los objetos de todos los días.",
  [card("c1", "portada", titulo="¿Qué fue la Bauhaus?", texto="Una escuela alemana fundada en 1919 unió arte y oficio, y terminó diseñando objetos de todos los días para la industria.", fuentes=["bauhaus-koop"]),
   card("c2", "idea", titulo="Arte y oficio, juntos", texto="La Bauhaus fue fundada en 1919 en Weimar por el arquitecto Walter Gropius. Quería unir el arte, la arquitectura y el trabajo artesanal.", fuentes=["bauhaus-koop", "met-bauhaus"]),
   card("c3", "pregunta", pregunta="¿Qué buscaba la Bauhaus al comenzar?", correctaId="b", opciones=[
     ("a", "Copiar estilos antiguos", "No: buscaba algo nuevo, uniendo arte y oficio."),
     ("b", "Unir el arte con el oficio", "¡Así es! Arte, arquitectura y trabajo artesanal en una sola escuela."),
     ("c", "Enseñar solo pintura", "No: también había arquitectura y talleres de oficios.")], fuentes=["bauhaus-koop", "met-bauhaus"]),
   card("c4", "idea", titulo="Del taller a la fábrica", texto="En 1923, Gropius orientó la escuela hacia el diseño para la producción en masa, con el lema \"Arte en la industria\".", fuentes=["met-bauhaus"]),
   card("c5", "revelar", titulo="Una silla con algo de bicicleta", texto="Marcel Breuer, que dirigía el taller de muebles, se inspiró en un objeto inesperado. ¿Cuál?",
        revelado="Los tubos de acero de su bicicleta. Con esa idea creó sillas metálicas livianas que se podían fabricar en serie.", fuentes=["met-bauhaus"]),
   card("c6", "idea", titulo="Letras simples y vidrio", texto="Sus impresos usaban letras sin adornos, llamadas sin serifa, junto con fotografías. El edificio que Gropius diseñó en Dessau tenía estructura de acero y una gran fachada de vidrio, rasgos que después marcaron la arquitectura moderna.", fuentes=["met-bauhaus"]),
   card("c7", "pregunta", pregunta="¿Qué cambio hizo Gropius en 1923?", correctaId="a", opciones=[
     ("a", "Orientó la escuela a diseñar para la producción en masa", "¡Correcto! Su lema fue \"Arte en la industria\"."),
     ("b", "Cerró los talleres", "No: los talleres siguieron; cambió hacia qué apuntaban."),
     ("c", "La dedicó solo a la pintura", "No: el cambio fue hacia la industria y la producción en masa.")], fuentes=["met-bauhaus"]),
   card("c8", "dato", texto="La Bauhaus existió casi catorce años y pasó por tres ciudades: Weimar, Dessau y Berlín. En 1933, bajo la presión de los nacionalsocialistas, se anunció su disolución.", fuentes=["bauhaus-koop"])],
  ("La Bauhaus", ["Fue una escuela alemana fundada en 1919 por Walter Gropius para unir arte, arquitectura y oficio.",
                  "Desde 1923 se orientó a diseñar objetos para la producción en masa.",
                  "Dejó sillas de tubo de acero, letras sin serifa y un edificio de acero y vidrio que marcaron el diseño moderno."]),
  [src("bauhaus-koop", "Bauhaus Kooperation Berlin Dessau Weimar", "What exactly was the Bauhaus?", "https://bauhauskooperation.com/knowledge/the-bauhaus/bauhaus-at-a-glance", "Texto principal",
       ["Fundada en Weimar en 1919 por Walter Gropius, unió arte, arquitectura y oficio", "Existió casi catorce años", "Weimar 1919–1925, Dessau 1925–1932 (productos cotidianos bien diseñados) y Berlín 1932–1933", "En Dessau cerró el 30-09-1932 por la mayoría nacionalsocialista del concejo; en Berlín se selló el edificio en 1933 y se anunció la disolución el 10-08-1933"],
       ["c1", "c2", "c3", "c8"], HOY),
   src("met-bauhaus", "The Metropolitan Museum of Art", "The Bauhaus, 1919–1933 (ensayo)", "https://www.metmuseum.org/essays/the-bauhaus-1919-1933", "Texto principal",
       ["Al inicio buscó unir las artes por medio del oficio", "En 1923 Gropius giró hacia el diseño para la producción en masa con el lema \"Art into Industry\"", "Breuer dirigió el taller de muebles y se inspiró en los tubos de su bicicleta para crear sillas livianas fabricables en serie", "Impresos con tipografía sin serifa y fotografía", "El edificio de Dessau usó estructura de acero y muro cortina de vidrio, rasgos que luego marcaron la arquitectura moderna"],
       ["c2", "c3", "c4", "c5", "c6", "c7"], HOY)],
  revision=4))

# ------------------------------------------------------------------ 26-10 arco y Panteón (r4)
LOTE.append(lesson("arco-panteon", "Arquitectura e ingeniería", "tecnologia",
  "¿Cómo se sostiene un arco de piedra?", "Y cómo los romanos levantaron una cúpula enorme.",
  [card("c1", "portada", titulo="¿Cómo se sostiene un arco de piedra?", texto="Un arco de piedra puede cubrir una puerta y aguantar el peso de lo que tiene encima. ¿Cómo lo logra?", fuentes=["brit-arco"]),
   card("c2", "idea", titulo="Piedras con forma de cuña", texto="Un arco se arma con piedras en forma de cuña, llamadas dovelas. La del centro, en lo más alto, se llama clave.", fuentes=["brit-arco"]),
   card("c3", "idea", titulo="Las piedras se aprietan", texto="El peso que carga el arco viaja a lo largo de su curva y aprieta unas piedras contra otras. A ese apretón se le llama compresión.", fuentes=["brit-arco"]),
   card("c4", "pregunta", pregunta="¿Cómo se llama la piedra del centro, en lo más alto de un arco?", correctaId="c", opciones=[
     ("a", "La base", "No: la base está abajo, donde el arco se apoya."),
     ("b", "La columna", "No: la columna es otra pieza; la del centro del arco es la clave."),
     ("c", "La clave", "¡Exacto! Es la dovela central, arriba.")], fuentes=["brit-arco"]),
   card("c5", "idea", titulo="Empuja hacia los lados", texto="Un arco o una cúpula tiende a abrirse en su base: empuja hacia afuera. Ese empuje lo resiste sobre todo el edificio que lo rodea.", fuentes=["eng-roma"]),
   card("c6", "revelar", titulo="El Panteón de Roma", texto="Su cúpula de hormigón fue reconstruida en tiempos del emperador Adriano, entre los años 117 y 138. ¿Qué tiene de especial su tamaño?",
        revelado="Mide 43,2 metros de ancho por dentro, y su altura es la misma. Adentro cabría una esfera perfecta.", fuentes=["uw-panteon"]),
   card("c7", "pregunta", pregunta="¿Cómo hicieron los romanos para que la cúpula pesara menos en lo alto?", correctaId="b", opciones=[
     ("a", "La reforzaron con barras de acero", "No: el Panteón es completamente de hormigón, sin acero."),
     ("b", "Usaron materiales más livianos hacia arriba, como la piedra pómez", "¡Así es! Abajo pusieron materiales pesados y arriba otros más livianos."),
     ("c", "La hicieron más gruesa arriba", "Al revés: buscaban que la parte alta pesara menos.")], fuentes=["uw-panteon", "eng-roma"]),
   card("c8", "dato", texto="En la cima de la cúpula hay un gran agujero, el óculo. Es la única entrada de luz a la cúpula.", fuentes=["uw-panteon"])],
  ("El arco y el Panteón", ["Un arco se arma con piedras en cuña, las dovelas, y la del centro arriba es la clave.",
                            "El peso viaja por la curva apretando las piedras, y el arco empuja hacia afuera en su base.",
                            "La cúpula del Panteón mide 43,2 metros por dentro y usa materiales más livianos hacia arriba."]),
  [src("brit-arco", "Encyclopaedia Britannica", "Arch (architecture)", "https://britannica.com/technology/arch-architecture", "Texto principal y leyendas de las ilustraciones",
       ["El arco cubre una abertura y soporta cargas desde arriba", "La construcción del arco depende de la cuña: dovelas en forma de cuña y la clave arriba al centro", "El arco lleva las cargas verticales principalmente por compresión a lo largo de su curva"],
       ["c1", "c2", "c3", "c4"], HOY),
   src("eng-roma", "Engineering Rome (programa de estudios en Roma, University of Washington)", "Studying Domes: Engineering of the Roman Pantheon and Brunelleschi's Duomo", "https://engineeringrome.org/studying-domes-engineering-of-the-roman-pantheon-and-brunelleschis-duomo/", "Secciones sobre el empuje y los materiales del Panteón",
       ["Arcos y cúpulas empujan hacia afuera en su base (empuje horizontal)", "Ese empuje lo resiste principalmente el edificio que los rodea", "El hormigón del Panteón es más liviano hacia arriba, con piedra pómez y toba liviana"],
       ["c5", "c7"], HOY),
   src("uw-panteon", "University of Washington, Honors Program in Rome", "The Pantheon", "https://depts.washington.edu/hrome/Authors/zinnia/Pantheon/pub_zbarticle_view_printable.html", "Texto principal",
       ["Reconstruido por completo durante el reinado de Adriano (117–138)", "Luz interior de 43,2 m y altura equivalente: encerraría una esfera perfecta", "Basalto en la base y áridos livianos como la piedra pómez arriba", "Íntegramente de hormigón, sin acero", "El óculo es la única fuente de luz de la cúpula"],
       ["c6", "c7", "c8"], HOY)],
  revision=4))

if __name__ == "__main__":
    for lid, rev, sha in write("lote2", LOTE):
        print(f"{lid} r{rev}  {sha[:12]}")
