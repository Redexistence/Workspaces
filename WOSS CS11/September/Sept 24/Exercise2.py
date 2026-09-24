first_description = input("Please enter a description of the first item bought.\n")
first_cost = float(input(f"How much was {first_description}?\n"))

second_description = input("Please enter a description of the second item bought.\n")
second_cost = float(input(f"How much was {second_description}?\n"))

subtotal = first_cost + second_cost
hst = subtotal * 0.13
total = subtotal + hst

print(f"Your purchases come to ${subtotal:.2f}.")
print(f"The HST on your purchases is ${hst:.2f}.")
print(f"The total amount you owe is ${total:.2f}.")

payment = float(input("How much money will you give to pay off the total?\n"))
change = payment - total
print(f"You receive ${change:.2f} in change.")