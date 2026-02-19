# Question 1:
print("Question 1: Average Test Score")
try:
    n = int(input("Number of test scores: "))
    if n <= 0:
            print("Error: Please enter a positive number of test scores.")
    
    scores = []
    for i in range(n):
          while True:
                try:
                      score = float(input(f"Enter test score {i+1}: "))
                      if score < 0:
                            print("Score negative, try again.")
                            continue
                      scores.append(score)
                      break
                except ValueError:
                      print("Invalid Input.")
    
    average = sum(scores) / n
    rounded_down_average = int(average)

    print(f"\nThe average test score is: {rounded_down_average}")
    
except ValueError:
    print("Error: Please enter a valid integer for the number of test scores.")