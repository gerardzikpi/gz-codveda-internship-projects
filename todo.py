class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        new_task = input("Add a new task: ")
        self.tasks.append(new_task)

    def view_tasks(self):
        print(self.tasks)

    def remove_task(self):
        clear_task = input("Remove a task: ")
        self.tasks.remove(clear_task)

todo_app = Todo()

# dashboard = print("""Welcome to the Todo app:
# 1. Add task
# 2. View task
# 3. Remove task""")

while True:
    user_input = input("""Welcome to the Todo app:
     1. Add task
     2. View task
     3. Remove task
     Please select a task from the list above: """).lower

    if user_input == "add task":
        todo_app.add_task()
        add_another_task = input("Add another task (Yes/No): ").lower()
        if add_another_task == "yes" or add_another_task == "y":
            todo_app.add_task()
        elif add_another_task == "no" or add_another_task == "n":
            break
        else:
            print("please select an option from above")

    elif user_input == "2" or user_input =="view tasks":
        todo_app.view_tasks()

    elif user_input == "3" or user_input == "remove task":
        todo_app.remove_task()
        remove_another_task = input("Add another task (Yes/No): ").lower()
        if remove_another_task == "yes" or remove_another_task == "y":
            todo_app.remove_task()
        elif remove_another_task == "no" or remove_another_task == "n":
            break
        else:
            print("please select an option from above.")

    else:
        print("Sorry, invalid task! Please select a valid task")