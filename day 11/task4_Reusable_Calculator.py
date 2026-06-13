def add(a,b):
    return a +b

def subtract(a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide(a,b):
    return a/b

num1 = float(input("enter firs number:"))
num2 = float(input("enter secound number:"))

print(f"Addition: {add(num1,num2)}")
print(f"substraction: {subtract(num1,num2)}")
print(f"multiplication: {multiply(num1,num2)}")
print(f"division: {divide(num1,num2)}")