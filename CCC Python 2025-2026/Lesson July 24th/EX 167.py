total = 0.0

while True:
    input_age = input("Enter guest age (blank to finish): ")
    if input_age == "":
        break
    age = int(input_age)
    if age <= 2:
        cost = 0.0
    elif 3 <= age <= 12:
        cost = 14.0
    elif age >= 65:
        cost = 18.0
    else:
        cost = 23.0
    total += cost

print(f"The total admission cost for the group is ${total:.2f}")