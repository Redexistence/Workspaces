#Question 1
import random

def lottery_numbers():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    ticket = lottery_numbers()
    print("lottery numbers:", ticket)