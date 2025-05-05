- Task Tracker CLI

Este es un pequeño proyecto de línea de comandos (CLI) que desarrollé para gestionar tareas pendientes, tareas en progreso y tareas completadas. Es una herramienta simple pero útil para practicar programación con Python, manejo de archivos JSON y argumentos en consola.

##  ¿Qué hace esta aplicación?

Permite:

- Agregar tareas
- Actualizar la descripción de una tarea
- Eliminar tareas
- Marcar tareas como "en progreso" o "completadas"
- Ver todas las tareas
- Filtrar tareas por estado (`todo`, `in-progress`, `done`)

Toda la información se guarda en un archivo `tasks.json` dentro del mismo directorio del script.
## Cómo usarlo

Primero, asegúrate de tener **Python instalado** (versión 3.6 o superior). Luego abre una terminal y navega al directorio donde tengas `task_cli.py`.

### Agregar una tarea
```bash
python task_cli.py add "Hacer ejercicio"
### actualizar/modificar una tarea por numero de ID
```bash
python task_cli.py update 2 "cambio de tarea"
 ### Eliminar una tarea por numero de ID
```bash
python task_cli.py delete 2
  ### Listar tareas por id con nombre y fecha de creacion
```bash
python task_cli.py list 

las tareas al añadirse automaticamente entrara con el estado "todo"
para listar todos los que tengan el mismo estado de todo
  ### Listar tareas por id con nombre y fecha de creacion con el estado Todo
```bash
python task_cli.py list todo

### Cambiar los estados por numero de id 
```bash
python task_cli.py mark-in-progress 2
python task_cli.py mark-done 2

### Listar por estados epecificos 
python task_cli.py list in-progress
python task_cli.py list done# task-cli
