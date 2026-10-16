# Write a program that asks the user to input the lengths of the three sides of a triangle.  Your program should then determine if the triangle can be classified as any of the following:
# Equilateral, isosceles, scalene, right
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
elif (side1**2 + side2**2 == side3**2) or (side1**2 + side3**2 == side2**2) or (side2**2 + side3**2 == side1**2):
    print("The triangle is right.")
else:
    print("The triangle is scalene.")