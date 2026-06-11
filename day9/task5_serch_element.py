numbers = [12,45,78,23,56,89]
print(f"available numbers: {numbers}")

target = int(input("enter number to serch:"))

print("\n---method 1 (in opretars)---")
if target in numbers:

    position = numbers.index (target)
    print(f"found at index {position}!")
else:
     print("not found")

print("\n---method 2 (manual loop)---")
found = False 
found_index =-1

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        found_index = i
        break  # Exit loop immediately since we found it

if found:
    print(f"Found at index {found_index}!")
else:
    print("Not Found")

