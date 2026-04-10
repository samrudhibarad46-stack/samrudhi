tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        break