def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.values())
    
    top_students = []
    for name, grade in grades.items():
        if grade == max_grade:
            top_students.append(name)
    
    return {"max_grade": max_grade, "students": top_students}


print(find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}))

