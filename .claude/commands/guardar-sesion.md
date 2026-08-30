---
description: Deja el repo limpio, versionado y reportado antes de cerrar la sesión
---

El usuario quiere cerrar esta sesión de forma ordenada. Sigue el checklist
de cierre de tarea de
[`docs/VERSIONADO.md`](https://github.com/elyini/Biblioteca_Documentacion/blob/main/docs/VERSIONADO.md)
(añade `elyini/Biblioteca_Documentacion` con `access: "read"` si no lo
tienes ya) antes de dar la sesión por guardada:

1. Revisa `git status`. Si hay cambios sin commitear que deban
   conservarse, díselo al usuario si no está claro qué hacer con ellos —
   nunca los descartes sin confirmar.
2. Si hubo trabajo relevante desde la última versión reportada:
   - Actualiza `VERSION` y añade la entrada correspondiente en
     `CHANGELOG.md`.
   - Actualiza `README.md`/`ROADMAP.md` para que reflejen el estado real.
   - Si creaste o modificaste scripts, confirma que siguen la convención
     de resultados (`resultados/<script>/`, ver `VERSIONADO.md`) y que no
     dejan archivos temporales o de prueba sin limpiar en el repo.
3. Haz commit y push de todo a tu rama de desarrollo.
4. **Si NO eres Biblioteca Documentación:** añade una entrada de cierre en
   tu buzón `comunicaciones/<tu-biblioteca>.md` (en
   `elyini/Biblioteca_Documentacion`, `access: "push"`): resumen de lo
   hecho en la sesión, versión actual, y qué queda pendiente para la
   próxima. Si tenías tareas en `tareas/<tu-biblioteca>.md`, actualiza su
   estado ahí también (`pendiente`/`en curso`/`hecha`).
   **Si eres Biblioteca Documentación:** confirma que las fichas
   individuales (`docs/<biblioteca>.md`) y `docs/FUNCIONES.md` reflejan
   los últimos avisos recibidos en `comunicaciones/`.
5. Confirma al usuario, en una frase, que todo está guardado y qué queda
   pendiente para la próxima sesión.
