
number = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in number if digit.isdigit())

print("The sum of the digits is:", digit_sum)
