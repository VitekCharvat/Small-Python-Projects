

tasks = []

def view_tasks():
    if not tasks:
        print("No tasks to view")
        return
    for task in tasks:
        print(f"- {task}")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    return task

def remove_task():
    if not tasks:
        print("No tasks to remove")
    try:
        number = int(input("Enter a number of task:"))
        tasks.pop(number - 1)
    except ValueError as e:
        print(f"enter number, {e}")
    return

def main():
    while True:
        print("\n TODO list")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()

        elif choice == "2":
            remove_task()

        elif choice == "3":
            view_tasks()

        elif choice == "4":
            break

if __name__ == "__main__":
    main()