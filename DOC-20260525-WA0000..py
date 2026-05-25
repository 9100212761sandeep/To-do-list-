tasks=[]

while True:

    print("1.Add task")
    print("2.view task")
    print("3.remove task")
    print("4.exit")

    choice=input("1/2/3/4: ")

    if choice=="1":

        task=input("give task name: ")
        tasks.append(task)

    elif choice=="2":
        
        if len(tasks)==0:
            print("no tasks available")
        
        else:

            for i in range(len(tasks)):
                print(f"\nyour tasks \n{i+1}.{tasks[i]}")

    elif choice=="3":
        if len(tasks)==0:
            print("no tasks")
        else:
            for i in range(len(tasks)):
                print(f"\nyour tasks \n{i+1}.{tasks[i]}") 
            remove=int(input("enter your task no: "))
                
                
            if remove>0 and remove<=len(tasks):

                    sk=tasks.pop(remove-1)
                    print(f"{sk}\nyour task is removed succesfully")
            else:
                    print("invalid operation")
    elif choice=="4":
        break

    else:
        print("invalid option")    






                             




    

