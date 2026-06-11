students = [
    {"Name": "ilma", "Marks": 85},
    {"Name": "saniya", "Marks": 92},
    {"Name": "fatima", "Marks": 78}
]

# Loop through the list
for students in students:
    name = students["Name"]
    marks = students["Marks"]
    print(f"Students: {name}, Marks: {marks}")