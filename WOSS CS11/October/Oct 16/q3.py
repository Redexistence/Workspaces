# Write a program that asks the user to input the month.  The program should then output the number of days in the month.  Assume a non leap year.
month = input("Enter the month: ")
if month.lower() in ["january", "march", "may", "july", "august", "october", "december"]:
    print("The month has 31 days.")
elif month.lower() in ["april", "june", "september", "november"]:
    print("The month has 30 days.")
elif month.lower() == "february":
    print("The month has 28 days.")
else:
    print("Invalid month entered.")