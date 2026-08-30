# Biblioteca America

**Versión:** v0.3.0 (ver [`CHANGELOG.md`](./CHANGELOG.md) y
[`ROADMAP.md`](./ROADMAP.md))

Catálogo de cómic americano (EEUU/Canadá e iberoamericano) que **no**
pertenezca a los universos compartidos de las grandes editoriales
estadounidenses (Marvel, DC, Image, etc.), dentro del proyecto
"Biblioteca" de elyini. Detalle del alcance en [`CLAUDE.md`](./CLAUDE.md).

## Contenido

- [`data/catalogo.csv`](./data/catalogo.csv) — catálogo de trabajo real:
  14.140 archivos (`AMERICANO` + `IBEROAMERICANO` del volumen AMERICA del
  usuario), esquema propio provisional (ver `ROADMAP.md`).
- [`data/escaneos/america_2026-08-29.json`](./data/escaneos/america_2026-08-29.json)
  — copia filtrada del informe real de Biblioteca Mac
  (`elyini_informe_2026-08-29.json`) con solo mis archivos.
- [`scripts/extraer_catalogo.py`](./scripts/extraer_catalogo.py) — script
  que genera ambos a partir de un informe de `elyini_scanner.py`.

Coordinación central del proyecto: `elyini/Biblioteca_Documentacion`
(rol, versionado, gobernanza y protocolo de comunicación entre
bibliotecas — no lo dupliques aquí, enlázalo).
