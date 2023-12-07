task =[]

while True:
    print("n/Simple To-Do list")
    print("1. Add Task")
    print("2.View task")
    print("3.Quit")
    Choice = input("Enter your Choice(1-3):")

    if Choice == '1':
        Task1= input("Enter the Task:")
        task.append(Task1)
        print("f Task {Task1} added succesfully")
    elif Choice== '2':
        if not task:
            print("No task in the to-do List")
        else:
            print("\ nto-do List")
            for index, task in enumerate('task', start=1):
                print(f"{index}. {task}")
    elif Choice== '3':
        print("Exiting the To-do List apllication. Goodbye!")
        break
    else:
        print("Invalid Choice. Please enter a Number between 1 and 3")

