tasks = []
def show_menu():
    print("""
        1.Add a task
        2.Show the task
        3.Delete a task
        4.Quit""")

def add_task():
    task = input("Add a task you want to do: ")
    tasks.append(task)
    print(f"{task} task added")

def delete_task():
    if not tasks:
        print("You do not have any tasks now!")
        return
    show_menu()
    try:
        index = int(input("Enter a number: "))
        if 1<= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"{removed} task removed")
        else:
            print("Invalid Task")
    except ValueError:
        print("Please enter a number")

def show_task():
    if not tasks:
        print("Add a task first!")
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    while True:
        show_menu()
        try:
            option = int(input("Enter a option: "))
            if option == 1:
                add_task()
            elif option == 2:
                show_task()
            elif option == 3:
                delete_task()
            elif option == 4:
                print("Goodbye!")
                break
            else:
                print("Enter a valid number 1-4")
        except ValueError:
            print("Enter a valid number!")
            continue
    
if __name__=="__main__":
    main()