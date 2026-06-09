# 1. Take input as string (default input() is string)
str_num1 = input("Enter first number as string: ")
str_num2 = input("Enter second number as string: ")

# 2. Type convert to integers
int_num1 = int(str_num1)
int_num2 = int(str_num2)

# 3. Add and print the result
result = int_num1 + int_num2
print("Sum after conversion:", result)
