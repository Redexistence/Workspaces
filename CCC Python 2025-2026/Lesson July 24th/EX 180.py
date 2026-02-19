import random

def flip_coin():
    if random.randint(0, 1) == 0:
        return 'H'
    else:
        return 'T'

def simulate():
    flips = []
    count = 0
    while True:
        outcome = flip_coin()
        flips.append(outcome)
        count += 1
        if len(flips) >= 3 and flips[-1] == flips[-2] == flips[-3]:
            break
    print(''.join(flips))
    return count


total_flips = 0
simulations = 10
for _ in range(simulations):
    flips_needed = simulate()
    print(f"Number of flips: {flips_needed}\n")
    total_flips += flips_needed
average_flips = total_flips / simulations
print(f"Average number of flips needed: {average_flips:.2f}")
