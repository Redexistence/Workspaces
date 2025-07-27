points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0
}

grades = []
while True:
    letter = input("Enter a letter grade (blank to finish): ")
    if letter == "":
        break
    grades.append(points[letter])

if grades:
    avg = sum(grades) / len(grades)
    print(f"Your GPA (Average) is {avg:.2f}")
else:
    print("None entered.")