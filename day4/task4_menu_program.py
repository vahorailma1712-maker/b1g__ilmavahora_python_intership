print("simpale calculation menu")
print("1.Add")
print("2.subtract")

choice = int(input("enter choice (1 or 2):"))

num1 = float(input("enter first number:"))
num2 = float(input("enter secound number:"))

if choice == 1:
    result = num1 + num2
    print(f"Result: {int(result)}")

elif choice == 2:
    result = num1 - num2
    print(f"Result: {int(result)}")
 
else:
   print("Invalid choice")
