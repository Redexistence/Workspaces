# How to solve the problem
# When it comes to solving a problem, there are a few key steps:
# Read the question carefully and understand what is being asked. Key words like "Calculate," "format," "display," "round," etc., will help you identify the relevant information.
# Break down the problem into smaller, more manageable pieces. This can help you focus on one aspect of the problem at a time.
# Plan out the solution before you start coding. Write out the steps you will need to take to solve the problem and organize them in a logical order. This can help you identify any potiential roadblocks or challenges before you start coding.
# Write your code, using clear and concise syntax. Avoid using complex or unnecessary long code, as this can make the solution harder to understand and debug.
# Test your code to make sure it is working correctly. Use sample inputs and outputs to verify that your code is producing the expected results. If your code is not working as expected, go back and troubleshoot any errors or bugs.
# Once Your code is working correctly, review it to make sure it is efficient and well-written. Is there any way you could improve the performance or clarity of your solution? Are there any rebundant or unnecessary steps in your code?

# Solve the Problem in Practice
# Problem: Given your birthday and the current date, calculate your age in days. Assume that the birthday and current date are correct dates(and no time travel). Simply put, if you were born in 1 Jan 2010, and today's date is 2 Jan 2010, you are 1 day old.
# Step 1: Read the question and understand the problem. In this case, we need to calculate the difference in days between your birthday and the current date.
# Step 2: Break down the problem into smaller, more manageable pieces. In this case, we need to find the difference in years, months, and days between your birthday and the current date.
# Step 3: Plan out the solution. In this case, we will use the datetime module in Python to calculate the difference in days between your birthday and the current date.
# Answer:

import datetime

# Get today's date
today = datetime.date.today()

# Get your birthday date
birthday = datetime.date(2011,7,12)

# Calculate the difference in days between today and your birthday
difference = (today - birthday).days

print(difference)
