def base7_to_base10(num_base7):
    # Converti un numero dal sistema settenario (base 7) al sistema decimale (base 10)
    base10_num = 0
    for i in range(len(num_base7)):
        base10_num += int(num_base7[i]) * (7 ** (len(num_base7) - 1 - i))
    return base10_num

def base10_to_base7(num_base10):
    # Converti un numero dal sistema decimale (base 10) al sistema settenario (base 7)
    if num_base10 == 0:
        return "0"

    base7_num = ""
    while num_base10 > 0:
        remainder = num_base10 % 7
        base7_num = str(remainder) + base7_num
        num_base10 //= 7

    return base7_num

def multiply_in_base7(num1_base7, num2_base7):
    # Moltiplica due numeri nel sistema settenario (base 7)
    num1_base10 = base7_to_base10(num1_base7)
    num2_base10 = base7_to_base10(num2_base7)

    result_base10 = num1_base10 * num2_base10
    result_base7 = base10_to_base7(result_base10)
    return result_base7

# Numeri nel sistema settenario (base 7)
num1_base7 = "265"
num2_base7 = "24"

# Calcola il prodotto nel sistema settenario
product_base7 = multiply_in_base7(num1_base7, num2_base7)

print(f"Il prodotto di {num1_base7} e {num2_base7} nel sistema settenario è: {product_base7}")
