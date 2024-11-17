# A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
# command-line or GUI-based application using Python, allowing
# users to create, update, and track their to-do lists

class ToDo:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.task} - Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task description: ")
        self.tasks.append(ToDo(task))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def mark_completed(self):
        self.view_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if task_number <= len(self.tasks) and task_number > 0:
                self.tasks[task_number - 1].completed = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_number = int(input("Enter the task number to delete: "))
            if task_number <= len(self.tasks) and task_number > 0:
                del self.tasks[task_number - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def update_task(self):
        self.view_tasks()
        try:
            task_number = int(input("Enter the task number to update: "))
            if task_number <= len(self.tasks) and task_number > 0:
                new_task = input("Enter the updated task description: ")
                self.tasks[task_number - 1].task = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def menu(self):
        while True:
            print("\n----- To-Do List -----")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Update Task")
            print("5. Delete Task")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                self.update_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()
