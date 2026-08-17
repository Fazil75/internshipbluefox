def todo_list(choice,tasks):
    if choice == 1:
        task = input("enter the task:")
        tasks.append(task)
    elif choice == 2:
        task =input("enter the task to delete:")
        if task in tasks:
            tasks.remove(task)
        else:
            print("task not found")
    elif choice == 3:
        if len(tasks) == 0:
            print("no tasks")
        else:
            print(tasks)
    else :
        print("invalid choice")

def main():
    tasks = []
    while True:
        print("1.Add")
        print("2.Remove")
        print("3.View")
        print("4.Exit")
        choice=int(input("enter the choice:"))
        if choice == 4:
           print("exiting..")
           break
        todo_list(choice,tasks)   
main()
    


