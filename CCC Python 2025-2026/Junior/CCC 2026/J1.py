B = int(input())
T = int(input())
P = int(input())

can = T - P

if B <= can:
    left = can - B
    print(f"Y {left}")
else:
    print("N")