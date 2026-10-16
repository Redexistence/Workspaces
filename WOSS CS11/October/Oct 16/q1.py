# Write a program that asks the user to input a number.  Your program should then determine if that number is even or odd.
# Hint:  All even numbers when divided by 2 give a remainder of 0.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")