#Ism Sharif, Familiya shaklida chiqarish kerak
def format_name(full_name: str) -> str:
    # familya ism Sharif shaklida input buladi
    name = full_name.split()
    result = f"{name[1]} {name[2]}, {name[0]}"


    return result

print(format_name("Aliyev Vali G'aniyevich"))
