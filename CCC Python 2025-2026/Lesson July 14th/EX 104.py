# Question 2:
print("\nQuestion 2: Unique Values")
numbers = input("Enter a list of numbers separated by spaces: ").split()
unique_numbers = list(set(numbers))
print("Unique values:", " ".join(unique_numbers))