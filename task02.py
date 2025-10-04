def atm_operation(balance: int, action: str, amount: int) -> dict:
    if action.lower() == "deposit":
        if amount > 0 :
            balance += amount

            return f"Deposit amalga oshirildi! \nNatija: {balance}"

        else:
            return "Amount 0 yoki manfiy bo`lishi mumkin emas! "
    
    elif action.lower() == "withdraw":
        if amount < balance and amount > 0:
            balance -= amount

            return f"withdraw amalga oshirildi! \nNatija: {balance}"
        
        else:
            return "Amount balansdan kichik bo`lishi va manfiy bo`lmasligi kerak!"
        
    return None

print(atm_operation(100000, "Withdraw", 500000))

