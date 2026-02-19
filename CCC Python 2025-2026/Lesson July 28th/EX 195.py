import random
import string

def license_plate():
    if random.choice([True, False]):
        # Old
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
    else:
        # New
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        return numbers + letters

plate = license_plate()
print("plate number:", plate)