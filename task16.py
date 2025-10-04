def count_by_grade(grades: dict, target_grade: int) -> dict:
    students_list = []
    
    for student, grade in grades.items():
        if grade == target_grade:
            students_list.append(student)
    
    result = {
        "count": len(students_list),
        "students": students_list
    }
    
    return result

print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
