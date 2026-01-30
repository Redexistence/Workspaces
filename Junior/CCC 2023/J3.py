n = int(input())
day_counts = [0] * 5

for _ in range(n):
    person = input()
    for d in range(5):
        if person[d] == 'Y':
            day_count += 1
mx = max(day_counts)
best = [str(1+1) for i in range(5) if day_counts[i] == mx]
print(",".join(best))