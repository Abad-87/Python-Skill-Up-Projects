def tasks():
    task = []
    print("--- Welcome to the To-Do List App ---")
    Total_tasks = int(input("Enter the total number of task you want to add :"))
    for i in range(1, Total_tasks + 1):
        task_name = input(f"Enter task {i} :")
        task.append(task_name)
    print(f"Today tasks are\n{task}")

    while True:
        operations = int(input("Enter \n1-Add Task\n2-Delete Task\n3-Update Task\n4-View Task\n5-Exit/Stop"))
        if operations == 1:
            add = input("Enter the task you want to add :")
            task.append(add)
            print(f"Task {add} added successfully")
        
        elif operations == 2:
            delete = input("Enter the task name you want to delete :")
            if delete in task:
                index = task.index(delete)
                del task[index]
                print(f"Deleted task {delete} has been successfully deleted. ")

        elif operations == 3:
            updated = input("Enter the task name you want to update :")
            if updated in task:
                up = input("Enter new task name :")
                index = task.index(updated)
                task[index] = up
                print(f"Updated task {up}")

        elif operations == 4:
            print(f"Total tasks = {task}")

        elif operations == 5:
            print("Program is ending...")
            break

        else:
            print("Invalid input, please try again...")
tasks()
