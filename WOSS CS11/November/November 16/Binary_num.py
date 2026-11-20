def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2
        
    return binary_str


def binary_to_decimal(binary_str):
    binary_str = str(binary_str)
    decimal_total = 0
    power = 0
    
    for digit in reversed(binary_str):
        decimal_total += int(digit) * (2 ** power)
        power += 1
        
    return decimal_total

dec_input = int(input("Enter a decimal number: "))
print("Binary:", decimal_to_binary(dec_input))

print()

bin_input = input("Enter a binary number: ")
print("Decimal:", binary_to_decimal(bin_input))
