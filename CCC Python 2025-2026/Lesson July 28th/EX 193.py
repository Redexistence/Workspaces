def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    next_one = n + 1
    while True:
        if is_prime(next_one):
            return next_one
        next_one += 1


n = int(input("Enter integer: "))
print("Next prime number:", next_prime(n))