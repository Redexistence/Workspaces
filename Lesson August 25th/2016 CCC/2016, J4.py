def is_rush_hour(hour, minute):
    # Morning rush: 07:00 to 09:59
    if (hour == 7 and minute >= 0) or (8 <= hour <= 9):
        return True
    # Evening rush: 15:00 to 18:59
    if (hour == 15 and minute >= 0) or (16 <= hour <= 18):
        return True
    return False

def add_minute(hour, minute):
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
    return hour, minute

time_str = input().strip()
hour, minute = map(int, time_str.split(':'))
distance = 0.0

while distance < 2.0:
    if is_rush_hour(hour, minute):
        distance += 0.5 / 60  # Rush speed
    else:
        distance += 1.0 / 60  # Normal speed
    hour, minute = add_minute(hour, minute)

minute -= 1
print(f"{hour:02d}:{minute:02d}")