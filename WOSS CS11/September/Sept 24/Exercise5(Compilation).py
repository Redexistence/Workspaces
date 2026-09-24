import math


# 1) Hourly pay
hours = float(input("How many hours did you work? "))
pay = hours * 10.25
print(f"A student works for {hours:g} hours at $10.25/hour. Their pay is ${pay:.2f}.")


# 2) Distance between two points
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between the two points is {distance:.2f}.")


# 3) Test marks and percentages
marks = []
print("\nMark\tPercent")
for _ in range(5):
	mark = float(input("Enter a test mark out of 60: "))
	marks.append(mark)
	print(f"{mark:g}\t{mark / 60 * 100:>7.1f}")

average = sum(marks) / len(marks) / 60 * 100
print(f"The average for the test is: {average:.1f}%")


# 4) Cash register
products = []
subtotal = 0
for _ in range(3):
	name = input("Enter the product name: ")
	cost = float(input("Enter the product cost: "))
	products.append((name, cost))
	subtotal += cost

tax = subtotal * 0.13
total = subtotal + tax

print("\nWOSS Gift Shop Receipt")
print("-------------------------------")
for name, cost in products:
	print(f"{name:<10}{cost:>20.2f}")
print("-------------------------------")
print(f"{'HST (13%)':<10}{tax:>20.2f}")
print("-------------------------------")
print(f"{'TOTAL':<10}{total:>20.2f}")
