'''
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''
import random

l = int(input("Enter the length of password:"))
if(l<4):
    print("Length must be 4 at least. Aborting ! ! !")
    exit()
pswd=[]
for i in range(l-2):
    pswd.append(chr(random.randint(97,122)))
for i in range(2):
    x = random.randint(0,l-2-1)
    pswd[x]= pswd[x].upper()
for i in range(2):
    loc = random.randint(0,l+i-1)
    pswd.insert(loc,chr(random.randint(33,64)))
pswd=''.join(pswd)
print(f"Password: {pswd}")