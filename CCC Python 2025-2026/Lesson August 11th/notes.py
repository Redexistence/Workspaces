import time
import os
# Debugging:
# We make 2 lists, and one list of costomer names and another list of how many purchases they made.
# We put those lists into another list which is now our database of purchases. Then first element of the first list matches with the first elemtns of the second list. Customers matched with their number of purchases.
list_of_customers = ['Bradley','Miranda','Tarik','Hayden']
customer_purchases = [3,5,1]
# Reading the Error
# This is tedious if we want to look up a spectific customer's number of purchases. Let's convert this into a dictionary for easy lookup.
customer_lookup = {}
for i in range(len(list_of_customers)):
    name = list_of_customers[i]
    # customer_purchases = customer_purchases[i] #(This line causes an error because we're trying to access an index that doesn't exist in the list.)
    # customer_lookup[name] = customer_purchases[i] This line also causes an error because we're trying to access an index that doesn't exist in the list.

# We've run into an error in trying to create our disctionary. At the bottom of the error message it says: IndexError: list index out of range.
# A search of Stack Overflow shows us that this error means that Python tried to use an index number with a list that did not exist.
# We can also see in the printout that Python is indicating line 10 as where the error occured.
# customer_lookup = {}
# for i in range(len(list_of_customers)):
    # print(f"Value of i: {i}")
    # name = list_of_customers[i]
    # customer_lookup[name] = customer_purchases[i]
    # print(f"Successfully added item: {i}")
# The code fails on the 4th iteration, index 3. Let's check the lengths of each list to see if one of the them is less than 4 elements long.
print(f"Length of list_of_customers: {len(list_of_customers)}")
print(f"Length of customer_purchases: {len(customer_purchases)}")
# Putting the Clues Together:
# We know that our error says we are searching past the end of one of our lists.
customer_purchases.append(2)
customer_lookup = {}
for i in range(len(list_of_customers)):
    print(f"Value of i: {i}")
    name = list_of_customers[i]
    customer_lookup[name] = customer_purchases[i]
    print(f"Successfully added item: {i}")

# Finally, we remove the print statements as there is no need to see them.
customer_lookup = {}
for i in range(len(list_of_customers)):
    name = list_of_customers[i]
    customer_lookup[name] = customer_purchases[i]

time.sleep(8)
os.system('cls')

print("Debug Challenge:")
contractor_hours = {}
contractor_hours['James'] = 10
contractor_hours['Purvi'] = 4
contractor_hours['Sherlin'] = 20

#
contractor_hours['total_hours'] = sum(contractor_hours.values())
print("contractor_hours:", contractor_hours)
time.sleep(8)
os.system('cls')