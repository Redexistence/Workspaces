def on_ride(position_in_line, number_of_cars, people_per_car):
    total_ppl = number_of_cars * people_per_car

    if position_in_line <= total_ppl:
        return "yes"
    else:
        return "no"

N = int(input("Enter your position in line: "))
C = int(input("Enter the number of cars: "))
P = int(input("Enter the number of people per car: "))

print(on_ride(N, C, P))