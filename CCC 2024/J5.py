from collections import deque

r = int(input())
c = int(input())

SCORES = {"S": 1, "M": 5, "L": 10}

def valid(node):
    x, y = node
    return 0 <= x < r and 0 <= y < c and not vis[x][y] and patch[x][y] != "*"

def neighbours(node):
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

patch = []
vis = []

for i in range(r):
    patch.append(list(input()))
    vis.append([False] * c)

a = int(input())
b = int(input())

queue = deque([(a, b)])
score = SCORES.get(patch[a][b], 0)
vis[a][b] = True

while queue:
    node = queue.popleft()
    
    for n in neighbours(node):
        if valid(n):
            x, y = n
            vis[x][y] = True
            score += SCORES.get(patch[x][y], 0)
            queue.append(n)

print(score)