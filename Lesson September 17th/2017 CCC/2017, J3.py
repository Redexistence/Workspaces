a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

dist = abs(a - c) + abs(b - d)

if dist <= t and (t - dist) % 2 == 0:
    print("Y")
else:
    print("N")