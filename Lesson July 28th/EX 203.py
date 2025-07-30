import random
import string

def random_password():
    length = random.randint(7, 10)
    chars = string.printable.strip()
    return ''.join(random.choice(chars) for _ in range(length))

def is_good_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) >= 8 and has_lower and has_upper and has_digit

def generate_good_password():
    attempts = 0
    while True:
        attempts += 1
        pswrd = random_password()
        if is_good_password(pswrd):
            return pswrd, attempts


password, attempts = generate_good_password()
print("Random password:", password)
print("It took", attempts, "attempts")