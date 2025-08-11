def remaining_donuts(initial_donuts, events):
    # Start with the initial number of donuts
    donuts = initial_donuts
    
    # Process each event
    for event in events:
        symbol, quantity = event
        if symbol == '+':
            donuts += quantity
        elif symbol == '-':
            donuts -= quantity
    
    return donuts

# Sample input
D = int(input("Enter the initial number of donuts: "))
E = int(input("Enter the number of events: "))

events = []
for _ in range(E):
    symbol = input("Enter the event symbol (+ or -): ")
    Q = int(input("Enter the quantity: "))
    events.append((symbol, Q))

print(remaining_donuts(D, events))