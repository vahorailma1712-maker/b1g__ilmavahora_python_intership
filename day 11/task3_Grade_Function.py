def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"
    
print(f"marks 95 -> grade: {get_grade(95)}") 
print(f"marks 82 -> grade: {get_grade(82)}")
print(f"marks 65 -> grade: {get_grade(65)}")
