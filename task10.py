def sort_numbers(numbers: list, reverse: bool = False) -> list:
    result1 = sorted(numbers, reverse=True)
    result2 = sorted(numbers, reverse=False)

    return f"Kamayish tartibi: {result1}, \nO`sish Tartibi: {result2}"

print(sort_numbers([3, 7, 10, -5, -8, 15, 22, 0]))