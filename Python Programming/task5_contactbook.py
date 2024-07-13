''' 
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
'''

def add():
    pass

def search():
    pass

def view():
    for i in range(len(l)):
        print(f"{i+1}. {l[i][0]} : {l[i][1]}")

def update():
    pass

def delete():
    view()
    i = int(input("Enter the serial number of contact to be deleted:"))
    if(i>len(l)):
        print("Invalid Input ! ! !")
    else:
        del l[i-1]
    print("Deleted successfully.")





if __name__ == "__main__":
    try:
        open("todo.txt",'x')
    except Exception as e:
        pass
    l=[]

    #use file handling to store the details
    with open("todo.txt",'r') as f:
        tmp=[]
        for i in range(4):
            tmp.append(f.readlines())
        l.insert(len(l),tmp)

    c='y'
    while(c[0]=='y' or c[0]=='Y'):
        print("1. Add new contact")
        print("2. View contact list")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        inp = int(input("Enter the operation you want to perform:"))
        if(inp==1):
            add()
        elif(inp==2):
            view()
        elif(inp==3):
            search()
        elif(4):
            update()
        elif(5):
            if(len(l)==0):
                print("Empty list.")
            else:
                delete()
        else:
            print("Invalid Input. Aborting ! ! !")
            exit()
        c = input("Press Y or y to continue:")
    with open("todo.txt",'w') as f:
        for i in l:
            f.write(i)