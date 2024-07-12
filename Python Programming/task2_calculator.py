'''
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
'''

if __name__ == "__main__":
    print("Calculator:")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Avaialable calculations:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (x)\n4. Division (/)")
    c = int(input("Enter your choice: "))
    if(c==4 and b==0):
        print("Error: Division by zero not possible. Aborting ! ! !")
        exit()
    if(c==1):
        print("The answer is ",a+b)
    elif(c==2):
        print("The answer is ",a-b)
    elif(c==3):
        print("The answer is ",a*b)
    elif(c==4):
        print("The answer is ",a/b)
        if((int(a)-a)==0 and (int(b)-b)==0):
            print("Integer Division possible: Quotient= ",int(a)//int(b)," Remainder= ",int(a)%int(b))