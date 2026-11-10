import math

area = int(input("Please enter the area."))
root = math.sqrt(area)

for length in range(1, int(root) + 1):
	if area % length == 0:
		width = area // length
		perimeter = 2 * length + 2 * width
		print("%i x %i has perimeter %i." % (length, width, perimeter))