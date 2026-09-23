import math

# 1) Circle
radius = float(input("Enter the radius of the circle in cm: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"A circle with a radius {radius} cm has a circumference of {circumference} cm and an area of {area} cm^2.")

# 2) Average
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))
average = (first + second + third) / 3
print(f"The average of the numbers is {average:.2f}.")

# 3) Name age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")