# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y versionado según [Semantic Versioning](https://semver.org/lang/es/). Ver
el estándar completo en
[`docs/VERSIONADO.md`](https://github.com/elyini/Biblioteca_Documentacion/blob/main/docs/VERSIONADO.md)
de Biblioteca Documentación.

## [0.2.0] - 2026-08-30

### Changed
- Alcance ampliado: además de cómic EEUU/Canadá fuera de universos de
  grandes editoriales, se incluye el **cómic iberoamericano**
  (Latinoamérica/España). Motivo: al revisar el escaneo real de Mac
  (`elyini_informe_2026-08-29.json`), el volumen `/Volumes/AMERICA` no se
  divide en "YANKI vs. resto" sino en 3 carpetas — `YANKI` (grandes
  editoriales, 34.570 archivos, va a Biblioteca America Comics),
  `AMERICANO` (12.238 archivos, EEUU/Canadá independiente) e
  `IBEROAMERICANO` (1.902 archivos, sin biblioteca asignada). El usuario
  confirmó que `IBEROAMERICANO` entra también en mi catálogo.
- Alcance total ahora: 14.140 archivos (~1,04 TB) de `AMERICANO` +
  `IBEROAMERICANO`.

## [0.1.0] - 2026-08-30

### Changed
- Alcance confirmado por el usuario: cómics estadounidenses y canadienses
  que no pertenezcan a los universos compartidos de las grandes editoriales
  americanas (Marvel, DC, Image, etc.). Reemplaza el borrador anterior
  (literatura americana / otros medios no-cómic, ahora fuera de alcance).
- `CLAUDE.md`, `README.md`, `ROADMAP.md`: actualizados con el alcance
  definitivo y la frontera con Biblioteca America Comics.

## [0.0.1] - 2026-08-29

### Added
- `CLAUDE.md`: contexto inicial de coordinación con el proyecto Biblioteca
  (rol, alcance pendiente de confirmar, protocolo de comunicación).
- `README.md`, `VERSION`, `ROADMAP.md`, `CONSULTAS.md`: identificación y
  estructura base del repositorio.
