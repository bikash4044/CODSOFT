''' 
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
'''
import os

def add(pos=-1):
    if(pos==-1):
        pos = len(l)
    tmp=[]
    tmp.append(input("Enter Name:"))
    tmp.append(input("Enter Phone number:"))
    tmp.append(input("Enter email:"))
    tmp.append(input("Enter address:"))
    l.insert(pos,tmp)

def search():
    src = input("Enter phone number or name to search for the contact:")
    for i in l:
        if(i[0]==src or i[1]==src):
            print(f"Name: {i[0]}")
            print(f"Phone Number: {i[1]}")
            print(f"Email: {i[2]}")
            print(f"Address: {i[3]}")
            return
    print("No match found.")

def view():
    if(len(l)==0):
        print("Empty List.")
    else:
        print("List of contacts:")
        for i in range(len(l)):
            print(f"{i+1}. {l[i][0]} : {l[i][1]}")

def update():
    view()
    if(len(l)>0):
        ind = int(input("Enter the serial number of the contact to be updated:"))
        delete(ind)
        add(ind)


def delete(i):
    view()
    if(i>len(l)):
        print("Invalid Input ! ! !")
    else:
        del l[i-1]
        print("Deleted successfully.")





if __name__ == "__main__":
    try:
        open("contact.txt",'x')
    except Exception as e:
        pass
    l=[]

    if(os.path.getsize("contact.txt")!=0):
        #use file handling to store the details
        with open("contact.txt",'r') as f:
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
        elif(inp==4):
            update()
        elif(inp==5):
            if(len(l)==0):
                print("Empty list.")
            else:
                view()
                i = int(input("Enter the serial number of contact to be deleted:"))
                delete(i)
        else:
            print("Invalid Input. Aborting ! ! !")
            exit()
        c = input("Press Y or y to continue:")
    with open("contact.txt",'w') as f:
        for i in l:
            for j in i:
                f.write(j)