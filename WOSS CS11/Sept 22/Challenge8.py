angles = [int(input()) for _ in range(3)]

if angles == [60, 60, 60]:
	print("Equilateral")
elif sum(angles) != 180:
	print("Error")
elif len(set(angles)) == 2:
	print("Isosceles")
else:
	print("Scalene")
