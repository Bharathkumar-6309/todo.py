# Simple To-Do List Manager in Python

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Empty task cannot be added.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()
