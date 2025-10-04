def filter_long_names(students: list, min_length: int = 5) -> list:
    result = []
    for name in students:         
        if len(name) > min_length: 
            result.append(name)  

    return result

print(filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]))
