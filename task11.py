def analyze_list(items: list) -> dict:
    counter = {}
    
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    
    total = len(items)
    
    unique = len(counter)
    

    duplicates = []
    for key, value in counter.items():
        if value > 1:
            duplicates.append(key)
    
    most_common = None
    max_count = 0
    
    for key, value in counter.items():
        if value > max_count:
            max_count = value
            most_common = key
    
    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common
    }


print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))
