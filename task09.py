def find_min_max(numbers: list) -> dict:
    mn = min(numbers)
    mx = max(numbers)

    return {"max": mx, "min": mn}

print(find_min_max([3, 7, 10, -5, -8, 15, 22]))