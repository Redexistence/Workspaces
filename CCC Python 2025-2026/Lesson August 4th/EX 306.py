def remove_outliers(data, n):
    if len(data) < 2 * n:
        raise ValueError("List must contain at least {} elements.".format(2 * n))
    sorted_data = sorted(data)
    return sorted_data[n:-n]

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in user_input.split()]
if len(numbers) < 4:
    print("Error: You must enter at least 4 numbers.")
    exit()
filtered = remove_outliers(numbers, 2)
print("List with outliers removed:", filtered)
print("Original list:", numbers)