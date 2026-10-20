import sys
input = sys.stdin.readline

n = int(input())

ans = 0

for i in range(n//5+1):
    if (n-i*5) % 4 == 0:
        ans += 1

print(ans)