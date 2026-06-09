P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in years (T): "))

# Simple Interest Formula
SI = (P * R * T) / 100

# Display simple interest
print("Simple Interest =", int(SI)) # Print as integer to match expected output or float
