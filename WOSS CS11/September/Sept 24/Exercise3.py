first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))

full_name = f"{first_name} {last_name}"
age_in_five_years = age + 5

print(f"\n{'Name:':<20}{full_name:<20}")
print(f"{'Current Age:':<20}{age:<20}")
print(f"{'Age in 5 years:':<20}{age_in_five_years:<20}")