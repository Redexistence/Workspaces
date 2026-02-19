T = int(input())
C = int(input())

chore_times = []
for _ in range(C):
    chore_times.append(int(input()))

chore_times.sort()

completed_chores = 0
time_spent = 0

for time in chore_times:
    if time_spent + time <= T:
        time_spent += time
        completed_chores += 1
    else:
        break

print(completed_chores)