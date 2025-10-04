def sort_names(students: list) -> list:
    name = sorted(students, reverse=False)

    return name

print(sort_names(["Zara", "Bobur", "Anvar"]))