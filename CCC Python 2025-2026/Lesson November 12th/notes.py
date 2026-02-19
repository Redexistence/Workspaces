# Read input
M = int(input().strip())
received_times = {}  # friend_id -> queue of receive times
wait_times = {}      # friend_id -> total wait time
current_time = 0

for _ in range(M):
    parts = input().strip().split()
    entry_type, X = parts[0], int(parts[1])
    
    if entry_type == 'W':
        current_time += X
    elif entry_type == 'R':
        if X not in received_times:
            received_times[X] = []
        received_times[X].append(current_time)
    elif entry_type == 'S':
        if X in received_times and received_times[X]:
            wait_time = current_time - received_times[X].pop(0)
            wait_times[X] = wait_times.get(X, 0) + wait_time
        else:
            wait_times[X] = -1
    
    if entry_type != 'W':
        current_time += 1

# Check for friends with unreplied messages
for friend_id, times_list in received_times.items():
    if times_list:
        wait_times[friend_id] = -1

# Output results
for friend_id in sorted(wait_times.keys()):
    print(friend_id, wait_times[friend_id])