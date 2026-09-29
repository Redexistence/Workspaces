import sys
input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
valTrack = [arrB[0]]
rangeTrack = []

l = 0
r = 0
val = arrB[0]

for i in range(1, n):
    if arrB[i] == val:
        r += 1
    else:
        rangeTrack.append((l, r))
        l = i
        r = i
        val = arrB[i]
        valTrack.append(val)
rangeTrack.append((l, r))

cur = 0
swipeL = []
swipeR = []
for i in range(n):
    if cur == len(valTrack): break
    if arrA[i] == valTrack[cur]:
        if rangeTrack[cur][0] < i:
            swipeL.append((rangeTrack[cur][0], i))
        if rangeTrack[cur][1] > i:
            swipeR.append((i, rangeTrack[cur][1]))
        cur += 1

if cur == len(valTrack):
    print("YES")
    print(len(swipeL) + len(swipeR))
    for left in swipeL:
        print("L", left[0], left[1])
    for i in range(len(swipeR)-1, -1, -1):
        print("R", swipeR[i][0], swipeR[i][1])

else:
    print("NO")