

tasks = []

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour Tasks (sorted by priority):")
        for i, task in enumerate(sorted(tasks, key=lambda x: x['priority'])):
            print(f"{i+1}. {task['title']} (Priority: {task['priority']})")

def add_task():
    title = input("Enter task: ")
    try:
        priority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low): "))
        if priority not in [1, 2, 3]:
            print("Invalid priority! Default set to 3 (Low).")
            priority = 3
        tasks.append({"title": title, "priority": priority})
        print("Task added successfully!\n")
    except ValueError:
        print("Priority must be a number (1, 2, or 3)!\n")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")

1
