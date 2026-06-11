numbers = [10,20,30,40,50]
print(f"list: {numbers}\n")

built_in_sum = sum(numbers)
print("---method 1 (built_in)---")
print(f"total = {built_in_sum}\n")

total = 0
for num in numbers:
    total += num

print("---method 2 (manual loop)---") 
print(f"total = {total}")
   