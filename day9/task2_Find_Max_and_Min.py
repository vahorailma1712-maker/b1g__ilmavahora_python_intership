numbers =[45,10,89,3,56,90,12]
print(f"List: {numbers}\n")

built_in_max = max(numbers)
built_in_min = min(numbers)
print("---method 1 (built-in)---")
print(f"max = {built_in_max}")
print(f"min = {built_in_min}")

largest = numbers[0]
smalest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smalest:
        smalest = num

print("---method 2 (manual loop)---")
print(f"max = {largest}")
print(f"min = {smalest}")

