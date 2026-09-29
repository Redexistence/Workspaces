COMMISSION_RATE = 0.025

sales = []
for ordinal in ("first", "second", "third"):
	agent = input(f"Please enter the {ordinal} agent: ")
	price = int(input(f"Please enter the sale price for agent {agent}: "))
	sales.append((agent, price))

print(f"{'Agent':<20}{'Price':>12}{'Commission':>16}")
for agent, price in sales:
	commission = price * COMMISSION_RATE
	print(f"{agent:<20}{price:>12}{commission:>16.2f}")