N = int(input())

days = ["", "", "", "", ""]

for i in range(N):
    availability = str(input())
    
    for c in range(5):
        if availability[c] == "Y":
            days[c] += "Y"

largest = [[0, 0]]
for s in range(len(days)):
    stri = days[s]
    lenStr = len(stri)
    
    if lenStr == largest[0][0]:
        largest.append([lenStr, s])
    
    if lenStr > largest[0][0]:
        largest = [[lenStr, s]]


T = [str(l[1] + 1) for l in largest]
print(", ".join(T))