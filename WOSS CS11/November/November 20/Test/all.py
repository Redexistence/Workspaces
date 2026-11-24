# Level 2:

print("Level 2:")
number = input("Please enter a number: ")

for digit in number:
	print(digit)


# Level 3:

print("")
print("Level 3:")
number = input("Please enter a number: ")

for digit in number:
	print(digit)
digit_sum = sum(int(digit) for digit in number)
print(f"The sum is {digit_sum}")


# Level 4:

print("")
print("Level 4:")
number = input("Please enter a number: ")
digit_sum = sum(int(digit) for digit in number)
while digit_sum >= 10:
	print(digit_sum)
	digit_sum = sum(int(digit) for digit in str(digit_sum))
print(digit_sum)


# Level 4+:

print("")
print("Level 4+:")
print("Numbers with 3 repetitions:")
for num in range(900, 1001):
	digit_sum = sum(int(digit) for digit in str(num))
	repetitions = 1
	while digit_sum >= 10:
		digit_sum = sum(int(digit) for digit in str(digit_sum))
		repetitions += 1
	if repetitions == 3:
		print(num)