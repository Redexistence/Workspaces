T = input().strip()
S = input().strip()

cyclic_shifts = S + S

found = False
for i in range(len(S)):
    shift = cyclic_shifts[i:i+len(S)]
    if shift in T:
        found = True
        break

print("yes" if found else "no")