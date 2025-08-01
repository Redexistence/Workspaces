import random

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6)

def expected_probability(total):
    # Number of ways to get each total with 2 dice
    ways = {
        2: 1,  3: 2,  4: 3,  5: 4,  6: 5,  7: 6,
        8: 5,  9: 4, 10: 3, 11: 2, 12: 1
    }
    return ways.get(total, 0) / 36 * 100

simulations = 1000
counts = {total: 0 for total in range(2, 13)}

for _ in range(simulations):
    total = dice_roll()
    counts[total] += 1

print(f"{'Total':>5} {'Frequency':>10} {'Observed %':>12} {'Expected %':>12}")
for total in range(2, 13):
    frequency = counts[total]
    observed = frequency / simulations * 100
    expected = expected_probability(total)
    print(f"{total:>5} {frequency:>10} {observed:>12.2f} {expected:>12.2f}")