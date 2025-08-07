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

    below_average = [num for num in numbers if num < average]
    average_values = [num for num in numbers if num == average]
    above_average = [num for num in numbers if num > average]

    print("\nBelow average values:")
    print(below_average if below_average else "None")
    
    print("\nAverage values:")
    print(average_values if average_values else "None")

    print("\nAbove average values:")
    print(above_average if above_average else "None")
else:
    print("None entered.")