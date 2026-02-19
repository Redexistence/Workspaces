M = int(input())
x, y = 0, 0
slimy = {(0, 0)}
ct = 0

dirs = {'N': (0, 1),'S': (0, -1),'E': (1, 0),'W': (-1, 0)}

for _ in range(M):
    move = input().strip()
    dir = move[0]
    dis = int(move[1:])
    
    dir_x, dir_y = dirs[dir]
    
    for _ in range(dis):
        x += dir_x
        y += dir_y

        if (x, y) in slimy:
            ct += 1
        
        slimy.add((x, y))

print(ct)