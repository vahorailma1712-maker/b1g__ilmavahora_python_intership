students = [
    {"Name": "ilma", "Marks": 85},
    {"Name": "saniya", "Marks": 92},
    {"Name": "ilza", "Marks": 78}
]

search_name = input("Enter students name to search: ")
found = False

for students in students:
    # We use .lower() to make the search case-insensitive
    if students["Name"].lower() == search_name.lower():
        print("Students Found")
        print(f"Marks: {students['Marks']}")
        found = True
        break # Exit loop once found

if not found:
    print("Students Not Found")