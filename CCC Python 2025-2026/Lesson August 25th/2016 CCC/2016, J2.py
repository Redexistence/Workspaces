square = [list(map(int, input().split())) for _ in range(4)]
target = sum(square[0])

for row in square:
    if sum(row) != target:
        print("not magic")
        exit()

for col in range(4):
    if sum(square[row][col] for row in range(4)) != target:
        print("not magic")
        exit()

print("magic")