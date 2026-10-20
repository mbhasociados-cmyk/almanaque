# Almanaque del Saber — Especificación v2.0 (20-10-2026)

Reemplaza la v1.0.1 por decisión de Max (20-10-2026): la app pasa a ser una app de aprendizaje visual en tarjetas, al estilo de Imprint o Kinnu, siempre en línea y con una colección de resúmenes de lo aprendido. Lo que no se menciona aquí se mantiene como en la v1.0.1: inicio de sesión, sincronización, seguridad y flujo editorial.

## 1. Producto
- Cada día, una idea nueva de cualquier tema, fácil de entender, en unos 5 minutos.
- La lección es una secuencia de tarjetas a pantalla completa, con barras de avance arriba. Se avanza con un botón o deslizando.
- Tipos de tarjeta:
  - `portada`: título e invitación, con ilustración;
  - `idea`: una idea breve con su ilustración;
  - `pregunta`: "¿Qué crees?", con respuesta inmediata y sin nota; hay que responder para seguir;
  - `revelar`: "toca para descubrir";
  - `dato`: dato curioso.
- Al final, una tarjeta de resumen ("Lo que aprendiste", 2 o 3 puntos) que se guarda en la sección **Aprendido**.
- Secciones (barra inferior): Hoy · Explorar (temas en mosaico, con filtro) · Aprendido (colección de resúmenes) · Cuenta.
- Se eliminan los repasos espaciados, el puntaje, la biblioteca manual y el modo sin conexión.

## 2. Arquitectura
- PWA en GitHub Pages, **en línea**. El service worker pide siempre a la red y usa la copia guardada de la interfaz solo ante un corte momentáneo. No intercepta `data/` ni Supabase. Una versión nueva toma el control sola, sin aviso de actualización.
- El catálogo, el calendario, las aprobaciones y las lecciones se descargan con `cache: "no-store"` al abrir la app y al volver a ella.
- Antes de mostrar una lección se verifica su SHA-256 contra el catálogo.
- IndexedDB conserva los eventos pendientes de enviar y una copia de las lecciones ya vistas, para que la colección Aprendido muestre sus resúmenes.
- Supabase sin cambios de esquema: los tipos de evento y las validaciones SQL de la v1.0.1 bastan.

## 3. Esquema de lección 2.0
```json
{ "schemaVersion": "2.0", "id": "…", "revision": 1, "idioma": "es-CL",
  "disciplina": "Ciencia cotidiana", "familia": "fisica", "titulo": "…", "subtitulo": "…", "minutosEstimados": 5,
  "tarjetas": [ { "id": "c1", "tipo": "portada|idea|pregunta|revelar|dato", "titulo": "…", "texto": "…",
                  "visual": "<svg …>", "revelado": "…", "pregunta": "…",
                  "opciones": [ { "id": "a", "texto": "…", "retro": "…" } ], "correctaId": "a", "fuenteIds": ["…"] } ],
  "resumen": { "titulo": "…", "puntos": ["…", "…", "…"] },
  "fuentes": [ /* igual que en el esquema 1.0, con consultadaEl */ ] }
```
- Familias de color: fisica/astronomia, biologia/salud, quimica/cocina, historia, arte, matematica/tecnologia, geografia, economia/sociedad, literatura.
- Ilustraciones SVG sanitizadas. A la lista permitida se agregan las clases de color `as-svg__fill`, `as-svg__soft`, `as-svg__warm`, `as-svg__cool`, `as-svg__sun`, `as-svg__warmline` y `as-svg__coolline`. Siguen prohibidos los colores literales, los scripts y las referencias externas.
- La interfaz v3 muestra solo lecciones 2.0. Las lecciones 1.x quedan archivadas en el repositorio.

## 4. Eventos (correspondencia con la v1)
| Acción | Evento |
|---|---|
| Abrir una lección | `lesson_opened` + `attempt_started` |
| Llegar a una tarjeta | `step_reached` (`step_id` = id de la tarjeta) |
| Responder una pregunta | `quiz_answered` |
| Llegar al resumen | `lesson_completed` |

"Aprendido" = lecciones con `lesson_completed`, derivado de los eventos y sincronizado entre equipos.

## 5. Guía editorial (v1.1 de ChatGPT N°12, adaptada a tarjetas)
- Una pregunta cotidiana y una idea central. Entre 6 y 9 tarjetas.
- Cada tarjeta, 1 a 3 frases. Sin fórmulas ni tecnicismos.
- Al menos 1 tarjeta de pregunta y una ilustración en la mayoría de las tarjetas.
- El dato curioso refuerza la idea; si introduce otro tema, se omite.
- Verificación de ChatGPT: exactitud por afirmación, fidelidad de la simplificación y comprensión.
- Prueba de comprensión con Max antes del V°B°. Aprobación por SHA-256 en `data/aprobaciones.v1.json`.
- Vista previa explícita: `?vista=id@rev`.
