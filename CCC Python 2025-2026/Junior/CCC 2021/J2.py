N = int(input())
max_bid = -1

for i in range(N):
    name = input()
    current_bid = int(input())
    if max_bid < current_bid:
        winner = name
        max_bid = current_bid

print(winner)