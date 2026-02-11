import sys
input = sys.stdin.readline

def get_cell(i, j):
    return (i*c + j - 1) % m

r, c, m = int(input()), int(input()), int(input())
dp_prev = [float('inf')] + [i%m for i in range(c)] + [float('inf')]
dp_curr = [float('inf')] + [0]*c + [float('inf')]
for i in range(1, r):
    for j in range(1, c+1):
        dp_curr[j] = min(dp_prev[j-1], dp_prev[j], dp_prev[j+1]) + get_cell(i, j)
    dp_prev, dp_curr = dp_curr, dp_prev
print(min(dp_prev) + r)