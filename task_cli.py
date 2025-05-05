import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'
# aqui para Carga las tareas desde el archivo JSON, Si el archivo no existe devuelve una lista vacía [].
#Si el archivo existe pero está vacío o mal escrito → también devuelve [] para evitar errores.
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Error: Task with ID {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted successfully.")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task['status'] == status_filter]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
         print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress.")
            return
    print(f"Error: tarea con ID {task_id} no encontrada.")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Error: Task with ID {task_id} not found.")
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [command] [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Task description is required.")
            return
        description = sys.argv[2]
        add_task(description)

    elif command == "list":
        if len(sys.argv) == 3:
            status_filter = sys.argv[2]
            if status_filter not in ['todo', 'in-progress', 'done']:
                print("Error: Invalid status filter. Use 'todo', 'in-progress', or 'done'.")
                return
            list_tasks(status_filter)
        else:
            list_tasks()
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Task ID and new description are required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        new_description = sys.argv[3]
        update_task(task_id, new_description)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Task ID is required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Task ID is required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        mark_in_progress(task_id)

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Task ID is required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        mark_done(task_id)    
    
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()