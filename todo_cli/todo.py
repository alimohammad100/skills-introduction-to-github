FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: add / done / show / quit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            task = input("Task to add: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added.")
        elif command == "done":
            show_tasks(tasks)
            index = int(input("Task number done: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
                print("✅ Task removed.")
            else:
                print("❌ Invalid number.")
        elif command == "show":
            show_tasks(tasks)
        elif command == "quit":
            break
        else:
            print("❓ Unknown command")

main()
