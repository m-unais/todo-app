def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())

    except FileNotFoundError:
        print("No file yet, starting with an empty list")
    return tasks

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks added to list")

    else:
        print("Here's the list")
        for task in tasks:
            print(task)

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks("tasks.txt")
choice = ""

while choice != "4":
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task= ").strip()
        if task != "":
            tasks.append(task)
            print(f"{task} Added to list")
            save_tasks("tasks.txt", tasks)

        else:
            print("Task can't be empty")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        task = input("Task to remove: ").strip()

        if task in tasks:
            tasks.remove(task)
            save_tasks("tasks.txt", tasks)
            print("Task removed from list")

        else:
            print(f"We don't have {task}")

    elif choice  == "4":
        print("Bye!")

    else:
        print("Please choose 1, 2, 3 or 4")