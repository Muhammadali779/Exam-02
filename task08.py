def calculate_stats(numbers: list) -> dict:
    _sum = sum(numbers)
    average = _sum / len(numbers)

    return {"sum": _sum, "average": round(average, 2)}  

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
