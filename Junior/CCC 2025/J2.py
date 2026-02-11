D=int(input())
E=int(input())

for _ in range(E):
    e = input()
    Q = int(input())

    if e == "+":
        D += Q
    elif e == '-':
        D -= Q

print(D)