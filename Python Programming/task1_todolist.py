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
    open("todo.txt",'x')
    f = open("todo.txt",'r+')
    f.close()
    