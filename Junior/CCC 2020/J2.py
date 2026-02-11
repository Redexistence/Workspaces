P = int(input())
N = int(input())
R = int(input())
day_count = 0
current_infected = N
while (current_infected <= P):
    current_infected += N*R
    N *= R
    day_count += 1
print(day_count)