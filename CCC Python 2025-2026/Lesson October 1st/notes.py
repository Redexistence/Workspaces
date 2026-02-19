def rotate_90(grid):
    N = len(grid)
    return [[grid[N - j - 1][i] for j in range(N)] for i in range(N)]

def is_original(grid):
    N = len(grid)
    for row in grid:
        if any(row[i] > row[i+1] for i in range(N-1)):
            return False
    for col in range(N):
        if any(grid[i][col] > grid[i+1][col] for i in range(N-1)):
            return False
    return True

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    if is_original(grid):
        break
    grid = rotate_90(grid)

for row in grid:
    print(' '.join(map(str, row)))

# Explanation of what the question is asking:
# The problem involves a square grid of integers that has been rotated
# by 0, 90, 180, or 270 degrees. The task is to determine the original
# orientation of the grid, where each row and each column is sorted in
# non-decreasing order. The solution involves checking the grid in its
# current orientation and rotating it until the original sorted state
# is found. The code reads the grid, performs rotations, checks for
# the sorted condition, and prints the correctly oriented grid.
"""
Input:
2
1 3
2 9
Output:
1 3
2 9
"""
# Is this code using Brute Force, Greedy, or Dynamic Programming?
# This code is using a Brute Force approach by checking all four possible
# orientations of the grid until it finds the one that meets the criteria.
# What is the time complexity of this code?
# The time complexity is O(N^2) for each of the four rotations, resulting
# in an overall time complexity of O(4 * N^2) = O(N^2)