def arithmetic_sequence(digits):
    if len(digits) < 2:
        return True
    diff = digits[1] - digits[0]
    for i in range(2, len(digits)):
        if digits[i] - digits[i-1] != diff:
            return False
    return True

arithmetic_times = set()
for hour in range(1, 13):
    for min in range(0, 60):
        time_str = f"{hour}{min:02d}"
        digits = [int(ch) for ch in time_str]
        if arithmetic_sequence(digits):
            arithmetic_times.add((hour, min))

per_cyc = len(arithmetic_times)

D = int(input())

cyc_mins = 12 * 60

full_cycs = D // cyc_mins
remaining_mins = D % cyc_mins

total = full_cycs * per_cyc

hour = 12
min = 0
for _ in range(remaining_mins + 1):
    if (hour, min) in arithmetic_times:
        total += 1
    min += 1
    if min == 60:
        min = 0
        hour += 1
        if hour == 13:
            hour = 1

print(total)