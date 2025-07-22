input_date = input("Enter date: ")
year, month, day = map(int, input_date.split('-'))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_yr(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if month == 2 and leap_yr(year):
    max_day = 29
else:
    max_day = days_in_month[month - 1]

if day < max_day:
    day += 1

else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(f"{year:04d}-{month:02d}-{day:02d}")