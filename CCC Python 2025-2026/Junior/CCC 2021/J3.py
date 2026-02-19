direction = ''
while True:
    code = input()

    if code == "99999":
        break

    sum_of_first_two_digit = int(code[0]) + int(code[1])
    if sum_of_first_two_digit %2 == 1:
        direction = "left"
    elif sum_of_first_two_digit == 0:
        pass
    else:
        direction = "right"

    step = code[2:]
    print(direction +" " + step)