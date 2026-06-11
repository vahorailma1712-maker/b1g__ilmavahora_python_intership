original_list = [1,2,2,3,4,4,5,1,3]
print(f"original list: {original_list}\n")

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("---method 1 (loop)---")
print(f"clean list:{unique_list}\n")

clean_set_list = list(set(original_list))
print("---method 2 (set)---")
print(f"clean list: {clean_set_list}")

