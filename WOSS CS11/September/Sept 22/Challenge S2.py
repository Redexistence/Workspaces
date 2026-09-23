import sys


data = list(map(int, sys.stdin.read().split()))
n = data[0]
measurements = sorted(data[1:])

low = measurements[:(n + 1) // 2][::-1]
high = measurements[(n + 1) // 2:]

answer = []
for i in range(n):
	if i < len(low):
		answer.append(low[i])
	if i < len(high):
		answer.append(high[i])

print(*answer)