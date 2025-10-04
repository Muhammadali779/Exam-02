def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Nolga bo`lib bo`lmaydi"
    else:
        return "Operator hato kiritildi! "
    
    return round(result, 2)
    
print(calculate(3, 8, "*"))

