# Write a program that asks the user to input the weight of a letter in grams, determine the cost of the postage given the following information:
# Up to 30 g:	$0.48
# Up to 50 g:	$0.70
# Up to 100 g:	$0.90
# $0.18 more for each 50 g or less after that.
weight = float(input("Enter the weight of the letter in grams: "))
if weight <= 30:
    cost = 0.48
elif weight <= 50:
    cost = 0.70
elif weight <= 100:
    cost = 0.90
else:
    additional_weight = weight - 100
    additional_cost = (additional_weight // 50 + (1 if additional_weight % 50 > 0 else 0)) * 0.18
    cost = 0.90 + additional_cost
print(f"The cost of the postage is ${cost:.2f}.")