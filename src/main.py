
import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "tasks.json"


def load_tasks():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    DATA_DIR.mkdir(exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": task_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task completed successfully.")
            return

    print("Task not found.")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
