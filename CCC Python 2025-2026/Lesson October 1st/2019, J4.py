flips = input().strip()

grid = [[1, 2], [3, 4]]

h = flips.count('H') % 2
v = flips.count('V') % 2

if h:
    grid[0], grid[1] = grid[1], grid[0]
if v:
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

print(f"{grid[0][0]} {grid[0][1]}")
print(f"{grid[1][0]} {grid[1][1]}")
