import json
import os 
FILE_NAME = "tasks.json"

# Loads Task from file 
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file,indent=4)

# Add a new task 
def add_task():
    tasks = load_tasks()
    title = input("Enter task description:")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully! ")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return 
    for i, task in enumerate(tasks):
        status = "C" if task["completed"] else "X"
        print(f"{i+1}. {task['title']} [{status}]")

# Mark as completed
def mark_done():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done:"))
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed['title']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main Menu
def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()