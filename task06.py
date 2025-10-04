def analyze_grades(students: dict) -> dict:
    
    total = sum(students.values())
    count = len(students)
    average = total / count

    result = {}
    for name, value in students.items():
        if value > average:
            result[name] = value 
    return result


print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
