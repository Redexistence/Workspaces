import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()
n = data[0]
lengths = data[1:1+n]

MAX_L = 2000
freq = [0] * (MAX_L + 1)
for L in lengths:
    freq[L] += 1

max_boards = 0
num_heights = 0

for s in range(2, 2 * MAX_L + 1):
    boards = 0
    # iterate l from 1 to s//2 to avoid double counting
    upper = min(MAX_L, s - 1)
    for l in range(1, min(s // 2, upper) + 1): 
        r = s - l
        if r > MAX_L or r < 1:
            continue
        if l == r:
            boards += freq[l] // 2
        else:
            boards += min(freq[l], freq[r])

    if boards > max_boards:
        max_boards = boards
        num_heights = 1
    elif boards == max_boards and boards > 0:
        num_heights += 1

print(max_boards, num_heights)