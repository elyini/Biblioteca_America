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
- [x] Enriquecer `autor(es)` y `formato` a partir de ruta/nombre de
      archivo (`scripts/enriquecer_catalogo.py`) — ver `CHANGELOG.md`.
- [ ] `editorial/sello` y `año`: sin señal fiable en ruta/nombre para
      este dominio; pendiente de metadatos externos (ComicVine/GCD o
      similar) o de que el usuario decida una fuente.
- [ ] Separar `guionista` de `dibujante` dentro de `autores`: no hay
      convención fiable de orden en el nombre de archivo; requeriría la
      misma fuente externa que editorial/año.
- [ ] Revisar la calidad de `tipo_detectado`/`idioma` heredados de
      `elyini_scanner.py` (13.763 de 14.140 archivos sin tipo detectado
      con confianza) — posible mejora en el propio script de Mac.
- [ ] Revisar y filtrar los duplicados detectados por Biblioteca Mac que
      caen en mi ámbito (`AMERICANO`/`IBEROAMERICANO`, dentro de los 200
      grupos de AMERICA de `resultados/buscar_duplicados/` en su repo).

## Próximas versiones

Por definir junto con el usuario y Biblioteca Documentación. Cada hito
relevante debe reportarse a Biblioteca Documentación (ver protocolo de
comunicación en su repo).
