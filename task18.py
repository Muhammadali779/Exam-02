def square_values(numbers: list) -> list:
    result = []
    

    for item in numbers:

        new_item = item.copy()
        new_item['value'] = new_item['value'] ** 2

        result.append(new_item)
    
    return result


print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))

