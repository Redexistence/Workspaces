# Question 3:
print("\nQuestion 3: Highest Score")

students = []
    
for _ in range(3):
    entry = input("Enter name and score separated by space: ").split()
    name = entry[0]
    score = int(entry[1])
    students.append((name, score))

highest = max(students, key=lambda x: x[1])
print(highest[0])