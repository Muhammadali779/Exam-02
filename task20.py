def find_shortest_name_student(students: list) -> str:
    
    shortest_student = min(students, key=lambda s: len(s['name']))
    return {"name": shortest_student['name'], "age": shortest_student['age']}

students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]

print(find_shortest_name_student(students))  
