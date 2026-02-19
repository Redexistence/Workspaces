# Question 4:
print("\nQuestion 4: Swap Tuple Elements")
tuples = []
for _ in range(4):
    a, b = map(int, input().split())
    tuples.append((a, b))

swapped = [(b, a) for (a, b) in tuples]
for t in swapped:
    print(t)