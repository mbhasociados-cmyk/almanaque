# Guía de producción autónoma — opción A

Decisión de Max (20-10-2026, "dale opcion A"): Claude produce, verifica contra fuentes abiertas y publica las lecciones. No hay revisión previa de ChatGPT ni V°B° por lección. Max puede revocar esta delegación cuando quiera.

## Cada semana
1. Revisa el calendario (`data/calendar.v1.json`) y toma las 7 fechas siguientes a la última programada. Mantén siempre al menos 7 días programados por delante. Cuenta solo los días cuya lección está en tarjetas (esquema 2.0 en el catálogo): la app no muestra las lecciones del formato antiguo (1.x). Si una fecha futura apunta a una lección 1.x, prográmale una versión en tarjetas (ver lote 2, 22-10-2026).
2. Elige los 7 primeros temas pendientes de `TEMAS.md`, intentando no repetir la familia en días seguidos.
3. Por cada tema, **abre las fuentes** con WebFetch: NASA, NOAA, USGS, Britannica, Banco Central, INE, Memoria Chilena, universidades u organismos oficiales. Anota solo lo que la fuente dice; si una afirmación no está en una fuente abierta, no la escribas.
4. Escribe el lote en `tools/lotes/loteN.py` usando `tools/almanaque_lib.py`; el ejemplo es `tools/lote1_r2.py`. Guía editorial:
   - una pregunta cotidiana y una idea central; 8 tarjetas: portada, ideas, 2 preguntas sin nota, un revelar y un dato curioso;
   - de 1 a 3 frases por tarjeta, sin fórmulas ni tecnicismos;
   - toda tarjeta, incluida la portada, cita su fuente, y cada fuente indica en `respalda` qué tarjetas respalda;
   - resumen de 3 puntos que se entienda solo;
   - cuida estas lecciones aprendidas de las revisiones de ChatGPT:
     - no inventar relaciones de causa;
     - decir "en promedio" cuando un valor varía;
     - distinguir "mínimo" de "basta";
     - mencionar el desfase cuando un índice usa datos del mes anterior;
     - no dar frecuencias de uso sin una fuente;
     - no mezclar movimiento relativo con movimiento vertical.
5. Ejecuta `python3 tools/lotes/loteN.py`. Escribe los borradores en `borradores/loteN/` y rechaza cualquier falla.
6. Prueba en un navegador local (python3 -m http.server + Playwright) que cada lección se abra con `?vista=id@rev` y se recorra completa hasta Aprendido, sin errores.
7. Publica: `python3 tools/publicar_lote.py loteN id1:AAAA-MM-DD id2:AAAA-MM-DD …`. Si el control falla, no publica y restaura todo.
8. Marca los temas en `TEMAS.md`, haz commit y push a `main`. GitHub Pages publica solo.
9. Comprueba en línea, con fetch, que la huella de cada lección publicada coincide con la del catálogo.
10. Deja un resumen breve para Max: las 7 lecciones de la semana con fecha y título, y cualquier problema encontrado.

## Nunca
- Modificar una lección ya publicada: las correcciones van en una revisión nueva, con un registro nuevo.
- Publicar una lección que no pasó los controles o cuya fuente no se pudo abrir.
- Tocar `js/config.js` ni las credenciales de Supabase.
