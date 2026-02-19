M = int(input())
N = int(input())
K = int(input())
rows = [0] * M
cols = [0] * N

for i in range(K):
    stroke = input().split()
    direction = stroke[0]
    index = int(stroke[1])-1

    if direction == 'R':
        rows[index] += 1
    else:
        cols[index] += 1

count = 0
for i in range(M):
    for j in range(N):
        if (rows[i] + cols[j]) % 2 == 1:
            count += 1

print(count)