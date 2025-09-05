N = int(input())
days = [0] * 5

for _ in range(N):
    availab = input().strip()
    for i in range(5):
        if availab[i] == 'Y':
            days[i] += 1

max_attend = max(days)
result = [str(i+1) for i, count in enumerate(days) if count == max_attend]
print(','.join(result))