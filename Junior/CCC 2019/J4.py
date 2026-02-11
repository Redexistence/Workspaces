line = input()

grid = [[1,2],[3,4]]

def horizontalFlip(grid):
    grid[0],grid[1] = grid[1],grid[0]
    pass

def verticalFlip(grid):
    temp = [grid[0][1], grid[0][0]]
    temp1 = [grid[1][1] , grid[1][0]]
    grid[1] = temp1
    grid[0] = temp
    pass


for i in range(len(line)):
    if line[i] == "H":
        horizontalFlip(grid)
    else:
        verticalFlip(grid)

for i in grid:
    for k in i:
        print(k, end=" ")
    print(" ")