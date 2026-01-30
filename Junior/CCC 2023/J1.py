P = int(input())
C = int(input())
F = P * 50 - C * 10 + (500 if P > C else 0)
print(F)