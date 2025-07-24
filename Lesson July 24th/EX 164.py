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
remain = pennies % 5

if remain < 2.5:
    adjusted = pennies - remain
else:
    adjusted = pennies + (5 - remain)

cash_total = adjusted / 100
print(f"Amount due (cash): ${cash_total:.2f}")