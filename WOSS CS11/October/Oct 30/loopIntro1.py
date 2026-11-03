for k in range(1,10,2):
    print(k)

for k in range(10,-10, -2):
    print(k)

string = "Halloween"

for i in range(2, len(string), 3):
    print(string[i])

howMany = 0

for letter in string:
    if letter.lower() == "l":
        howMany += 1
    print(letter, end="")

for i in range(10):
    print("\U0001F383","\U0001F478")