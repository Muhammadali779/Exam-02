# - 0 - 5,000,000: 0%
# - 5,000,001 - 10,000,000: 12%
# - 10,000,001 - 20,000,000: 18%
# - 20,000,001+: 25%

result = {"gross": int, "tax": int, "net": int, "rate": str}
def calculate_tax(salary: int) -> dict:
    if 0 <= salary and salary <= 5_000_000:
        tax = (salary / 100 )* 0
        result['gross'] = salary
        result["tax"] = tax
        result['net'] = salary - tax
        result["rate"] = "0%"
    
    elif 5_000_000 < salary and salary <= 10_000_000:
        tax = (salary / 100 )* 12
        result['gross'] = salary
        result["tax"] = tax
        result['net'] = salary - tax
        result["rate"] = "12%"

    elif 10_000_000 < salary and salary <= 20_000_000:
        tax = (salary / 100 )* 18
        result['gross'] = salary
        result["tax"] = tax
        result['net'] = salary - tax
        result["rate"] = "18%"

    elif salary > 20_000_000:
        tax = (salary / 100 )* 25
        result['gross'] = salary
        result["tax"] = tax
        result['net'] = salary - tax
        result["rate"] = "25%"

    else:
        return "Maosh 0 dan kichik bo`lishi mumkin emas! "
    
    return result

print(calculate_tax(8_000_000))
