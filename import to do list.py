import os

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, status = line.strip().split(" | ")
                tasks.append({"title": title, "status": status})
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']} | {task['status']}\n")

# Function to display the task list
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {'Completed' if task['status'] == 'done' else 'Pending'}")

# Function to add a new task
def add_task(tasks):
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "status": "pending"})
    print(f"Task '{title}' added!")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks) and tasks[task_index]['status'] == 'pending':
            tasks[task_index]['status'] = 'done'
            print(f"Task '{tasks[task_index]['title']}' marked as completed!")
        else:
            print("Invalid task number or task already completed.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main function to run the To-Do list app
def todo_list_app():
    tasks = load_tasks()  # Load existing tasks from file at the start
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Exit")
        choice = input("\nChoose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            save_tasks(tasks)  # Save tasks to file when exiting
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_app()
