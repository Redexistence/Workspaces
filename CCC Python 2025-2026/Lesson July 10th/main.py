#Test question 1: Create a program that reads the length and width of a farmer's field from the user in feet. Display the are of the field in acres.
#Hint: There are 43,560 square feet in an acre.

import time

square_feet_per_acre = 43560
print("Field Area Calculation (in acres)")
time.sleep(1)
print("-------------------------------")


try:
    length = float(input("Enter the length of the field in feet: "))
    width = float(input("Enter the width of the field in feet: "))

    #This calculates the area in square feet
    area_sqft = length * width

    #This converts it to acres
    area_acres = area_sqft / square_feet_per_acre

    #This displays the result
    print(f"\nThe area of the field is {area_acres:.2f} acres rounded to 2 decimal places.")

except ValueError:
    print("Error: Please enter valid numerical values for length and width.")

#Test question 2: Create a program that you create fr this excercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the taac and top for the meal. Use your local tax rate (13%) when computing the ampunt of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format te output so that all the values are displayed using 2 decimal places.

tax_rate = 0.13
tip_percentage = 0.18

print("Meal Cost Calculation")
print("-------------------")

meal_cost = float(input("Enter the cost of the meal: $"))

#Calculates the tax and tips
tax_amount = meal_cost * tax_rate
tip_amount = meal_cost * tip_percentage

#Calculate the total
grand_total = meal_cost + tax_amount + tip_amount

#Results
print("\nReceipt:")
print(f"Meal: ${meal_cost:.2f}")
print(f"Tax (13%): ${tax_amount:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print("-------------------")
print(f"Grand Total: ${grand_total:.2f}")