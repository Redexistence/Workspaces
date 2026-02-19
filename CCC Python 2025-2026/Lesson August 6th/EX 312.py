numbers = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid number.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"\nAverage: {average:.2f}")

    below = [num for num in numbers if num < average] # Below average values
    average_num = [num for num in numbers if num == average] # Average values
    above = [num for num in numbers if num > average] # Above average values

    print("\nBelow average values:")
    print(below if below else "None")
    
    print("\nAverage values:")
    print(average_num if average_num else "None")

    print("\nAbove average values:")
    print(above if above else "None")
else:
    print("None entered.")