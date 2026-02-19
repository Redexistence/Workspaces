s = []
for i in range(5):
    s.append(int(input()))

D = int(input())

s.remove(max(s))
s.remove(min(s))

T = sum(s) * D

print(T)