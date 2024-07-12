'''
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''

# x mode: if not exists
# r mode: read
# w mode: write

if __name__ == "__main__":
    try:
        open("todo.txt",'x')
    except Exception as e:
        pass
    l=[]
    with open("todo.txt",'r') as f:
        l=f.readlines()
    
    #CRUD
    c='y'
    while(c[0]=='y' or c[0]=='Y'):
        print("1. Display the list of tasks")
        print("2. Add a new task")
        print("3. Delete a completed task from list")
        inp = int(input("Enter the operation you want to perform:"))
        if(inp==1):
            print("List of tasks:")
            if(len(l)>0):
                for i in range(len(l)):
                    print(i+1,": ",l[i])
            else:
                print("Empty List of task.")
        elif(inp==2):
            l.append(input("Enter the new task:"))
            print("Added successfully.")
        elif(inp==3):
            if(len(l)==0):
                print("Empty list.")
            else:
                print("List of tasks:")
                for i in range(len(l)):
                    print(i+1,": ",l[i])
                d = int(input("Enter the serial no. of the task you want to remove"))
                if(d<0 or d>len(l)):
                    print("Invalid Input. Abroting ! ! !")
                else:
                    del l[d-1]
                    print("Removed successfully.")
        else:
            print("Invalid Input. Aborting ! ! !")
            exit()
        c = input("Press Y or y to continue:")
    with open("todo.txt",'w') as f:
        for i in l:
            f.write(i)
        

        

    



 
    