total = 0.0

while True:
    price = input("Enter price: ")
    if price == "":
        break
    try:
        total += float(price)
    except ValueError:
        print("Invalid input.")

print(f"Total: ${total:.2f}")

pennies = round(total * 100)
remained = pennies % 5

if remained < 2.5:
    adjusted = pennies - remained
else:
    adjusted = pennies + (5 - remained)

cash_total = adjusted / 100
print(f"Cash: ${cash_total:.2f}")