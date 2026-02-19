n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split(','))
    xs.append(x)
    ys.append(y)

min_x = min(xs) - 1
max_x = max(xs) + 1
min_y = min(ys) - 1
max_y = max(ys) + 1

print(f"{min_x},{min_y}")
print(f"{max_x},{max_y}")