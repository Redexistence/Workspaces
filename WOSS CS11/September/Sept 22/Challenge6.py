daytime = int(input("Number of daytime minutes?\n"))
evening = int(input("Number of evening minutes?\n"))
weekend = int(input("Number of weekend minutes?\n"))

plan_a = max(0, daytime - 100) * 25 + evening * 15 + weekend * 20
plan_b = max(0, daytime - 250) * 45 + evening * 35 + weekend * 25

print(f"Plan A costs ${plan_a / 100:.2f}")
print(f"Plan B costs ${plan_b / 100:.2f}")

if plan_a < plan_b:
	print("Plan A is cheapest.")
elif plan_b < plan_a:
	print("Plan B is cheapest.")
else:
	print("Plan A and B are the same price.")
