 # 1) Count from 100 down to 0.
number = 100
while number >= 0:
	print(number)
	number -= 1

# 2) Ask for favorite colors until the user types "done".
color = input("Enter a favorite color (or type done to finish): ")
while color.lower() != "done":
	print("Favorite color:", color)
	color = input("Enter another favorite color (or type done to finish): ")

# 3) Ask for family members' ages until -1, then display the average.
total_age = 0
family_members = 0
age = int(input("Enter a family member's age (-1 when done): "))
while age != -1:
	total_age += age
	family_members += 1
	age = int(input("Enter another family member's age (-1 when done): "))

if family_members > 0:
	print("The average age is", total_age / family_members)
else:
	print("No ages were entered, so an average cannot be calculated.")

# 4) (University Only) Count how many times the number is divisible by 2.
number = int(input("Please enter your number: "))
divisions = 0
while number != 0 and number % 2 == 0:
	divisions += 1
	number //= 2

print("Your number is divisible by 2", divisions, "times.")