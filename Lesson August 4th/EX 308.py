negative = []
zeros = []
positive = []

while True:
    user_input = input("Enter integer (or press Enter to finish): ")
    if user_input == "":
        break
    number = int(user_input)
    if number < 0:
        negative.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positive.append(number)

print("Negatives:", negative)
print("Zeros:", zeros)
print("Positives:", positive)
