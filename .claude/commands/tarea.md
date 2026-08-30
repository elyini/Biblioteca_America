---
description: Registra una tarea del usuario para que la recoja otra biblioteca
---

El usuario va a describir (o acaba de describir) una tarea para una o
varias bibliotecas del proyecto Biblioteca. Tu trabajo:

1. Identifica a qué biblioteca(s) va dirigida la tarea. Si no está claro
   por el mensaje del usuario, pregúntaselo antes de registrar nada.
2. Si la tarea es para **ti mismo** (el usuario te habló directamente a
   ti, en tu propio chat) y quieres ejecutarla ya: hazlo directamente, no
   hace falta pasar por `tareas/`. Este comando es para tareas dirigidas
   a **otra** biblioteca distinta de la sesión actual.
3. Añade `elyini/Biblioteca_Documentacion` con `access: "push"`
   (`add_repo(owner="elyini", repo="Biblioteca_Documentacion", access="push")`
   si no eres tú misma) y añade una entrada fechada al final de
   `tareas/<biblioteca-destino>.md`, con el texto de la tarea tal y como
   la dio el usuario (no la reinterpretes ni la resumas de más — copia lo
   esencial). Formato en `tareas/README.md`.
4. Haz commit y push.
5. Responde al usuario confirmando en qué archivo quedó registrada la
   tarea, y recuérdale que la biblioteca destinataria la recogerá la
   próxima vez que reanude sesión (`/reanudar-sesion`) — no se ejecuta
   sola ni en vivo.
6. No ejecutes tú la tarea en nombre de la otra biblioteca, salvo que el
   usuario te lo pida explícitamente a ti.
