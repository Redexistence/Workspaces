import random

def create_card():
    bingo = {}
    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }
    
    for letter, number_range in ranges.items():
        bingo[letter] = random.sample(number_range, 5)
    
    return bingo

def display_card(bingo):
    print(" B   I   N   G   O")
    for i in range(5):
        for letter in "BINGO":
            print(f"{bingo[letter][i]:2}", end="  ")
        print()


card = create_card()
display_card(card)