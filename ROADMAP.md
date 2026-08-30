# Roadmap — Biblioteca America

Estado: alcance confirmado y ampliado. Cómic americano (EEUU/Canadá +
iberoamericano) fuera de los universos compartidos de las grandes
editoriales estadounidenses. Carpetas reales: `AMERICANO` +
`IBEROAMERICANO` de `/Volumes/AMERICA` (14.140 archivos, ~1,04 TB).

## v0.0.x — Fundación

- [x] Contexto de coordinación con el proyecto (`CLAUDE.md`).
- [x] Confirmar con el usuario el alcance exacto (qué entra aquí vs.
      Biblioteca America Comics).

## v0.1.x — Alcance confirmado

- [x] Documentar el alcance definitivo en `CLAUDE.md`/`README.md` y
      reportarlo a Biblioteca Documentación.

## v0.2.x — Alcance ampliado y catálogo real

- [x] Detectar (vía escaneo real de Mac) que el volumen AMERICA tiene una
      tercera carpeta (`IBEROAMERICANO`) sin biblioteca asignada, y
      confirmar con el usuario que entra en mi alcance.
- [x] Construir el catálogo real a partir del escaneo entregado por
      Biblioteca Mac (`elyini_informe_2026-08-29.json`, carpetas
      `AMERICANO` + `IBEROAMERICANO`) → `data/catalogo.csv` (14.140 filas),
      sin esperar a un escaneo nuevo.
- [ ] Adoptar el esquema de datos común en cuanto lo publique Biblioteca
      elyini y migrar `data/catalogo.csv` a ese esquema.
- [ ] Definir/enriquecer campos de catálogo propios (editorial/sello
      independiente, autor(es), guionista, dibujante, año, formato:
      serie/one-shot/recopilatorio, país/región: EEUU, Canadá o
      Iberoamérica) — el catálogo actual solo trae lo que ya extraía
      `elyini_scanner.py` (serie/volumen/número por patrón de nombre,
      13.763 de 14.140 archivos aún sin tipo/idioma detectado con
      confianza).
- [ ] Revisar y filtrar los duplicados detectados por Biblioteca Mac que
      caen en mi ámbito (`AMERICANO`/`IBEROAMERICANO`, dentro de los 200
      grupos de AMERICA de `resultados/buscar_duplicados/` en su repo).

## Próximas versiones

Por definir junto con el usuario y Biblioteca Documentación. Cada hito
relevante debe reportarse a Biblioteca Documentación (ver protocolo de
comunicación en su repo).
