C = int(input())

    
row1 = str(input())
row2 = str(input())

row1 = row1.replace(" ", "")
row2 = row2.replace(" ", "")

tiles = [row1, row2] 
M = 0

for i in range(len(tiles)):
    for j in range(len(tiles[i])):
        if tiles[i][j] == "1":
            M += 3
            
            if j > 0 and tiles[i][j-1] == "1":
                M -= 2
                
            if i == 0 and tiles[i+1][j] == "1" and j % 2 == 0:
                M -= 2

print(M)