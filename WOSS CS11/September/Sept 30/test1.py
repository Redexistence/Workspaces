"""
Level 2:
Write a program that asks the user for a single digit with one prompt followed by the user's full name (first and last name) using a second prompt.
Display how many characters are in the user's full name (including the space)
Display the name as many times as the digit.

Sample input:
Enter a single digit: 3
Enter your full name: Billy Smith
Sample output:
The full name has 11 characters
Billy SmithBilly SmithBilly Smith
"""

digit = int(input("Enter a single digit: "))
full_name = input("Enter your full name: ")

print(f"The full name has {len(full_name)} characters")
print(full_name * digit)

"""
Level 3:
Using the implementation from Level 2, modify it to use only one prompt to get the digit and the full name. We can assume that a space will separate the digit from the name.
Still display how many characters are in the user's full name but this time DO NOT count the space.
Display the name as many times as the digit, without spaces.

Sample input:
Please enter a single digit and your full name: 3 Billy Smith

Sample output:
The full name has 10 characters
BillySmithBillySmithBillySmith
"""

user_input = input("Please enter a single digit and your full name: ")
digit_text, full_name = user_input.split(" ", 1)
digit = int(digit_text)

name_without_spaces = full_name.replace(" ", "")
print(f"The full name has {len(name_without_spaces)} characters")
print(name_without_spaces * digit)

"""
Level 4:
Continue from level 3.
Swap the case (uppercase becomes lower case and the opposite too).
Display the new string as many times as the digit, without spaces.

Sample input:
Please enter a digit and your full name: 3 Billy Smith
Sample output:
The full name has 10 characters
BillySmithBillySmithBillySmith
bILLYsMITHbILLYsMITHbILLYsMITH
"""

user_input = input("Enter a single digit and your full name: ")
digit_text, full_name = user_input.split(" ", 1)
digit = int(digit_text)

name_without_spaces = full_name.replace(" ", "")
print(f"The full name has {len(name_without_spaces)} characters")
print(name_without_spaces.swapcase() * digit)

"""
Level 4+:
Continue from level 4.
Create a new string made of the initial of the last name combined with the initial of the first name.
Display the new string as many times as the length of the full name without space.
Sample input:
Please enter a single digit and your full name: 3 Billy Smith

Sample output:
The full name has 10 characters
BillySmithBillySmithBillySmith
bILLYsMITHbILLYsMITHbILLYsMITH
SBSBSBSBSBSBSBSBSBSB
"""

user_input = input("Enter a single digit and your full name: ")
digit_text, full_name = user_input.split(" ", 1)
digit = int(digit_text)

name_without_spaces = full_name.replace(" ", "")
print(f"The full name has {len(name_without_spaces)} characters")
print(name_without_spaces * digit)
print(name_without_spaces.swapcase() * digit)

first_initial = full_name.split()[0][0]
last_initial = full_name.split()[-1][0]
initial_pair = last_initial + first_initial
print(initial_pair * len(name_without_spaces))