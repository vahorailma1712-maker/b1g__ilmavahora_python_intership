a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(f"Before Swapping: a = {a}, b = {b}")

# Pythonic Swapping (No third variable)
a, b = b, a

# Alternative Math Swapping:
# a = a + b
# b = a - b
# a = a - b

print(f"After Swapping: a = {a}, b = {b}")
