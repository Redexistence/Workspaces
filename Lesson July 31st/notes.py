import os
import time
# DICTIONARIES AND SETS:
# A ditionary allows you to store a collection of Python objects indexed with only hashable types.
# DICTIONARY LITERALS:
# Placing elements inside curly braces {} seperating them with commas creates a dictionary literal.
# Dictionaries can consist of integers, strings, Boolean, and list. These types of dictionaries are know as mixed dictionaries.
# Python provides the built-in function dict() to create a dictionary. The empty curcle braces {} are used to create an empty dictionary.
# DICTIONARY OPERATIONS:
# Accessubg a value D[Key] and modifying a value D[Key] = new_value.
# Retrieving the length (len), key membership checking (in), and creating lists(list)
# If you try to access a key that does not exist, Python will raise a KeyError.
# You can use the get() method instead, which returns None if the key isn't in the dictionary.
# You can even give it a default value to return instead in that case.
# For example:
test_average = {'Test 1': 90, 'Test 2': 85, 'Test 3': 88}
print(test_average['Test 1'])  
print(test_average.get('Test 4'))
print(test_average.get('Test 5', 'DEFAULT!'))  # Returns 'DEFAULT!' if 'Test 5' is not found
test_average['Test 3'] = 96 # Modifying an existing value
print(test_average)
print('Test 1' in test_average)
print('Bob' in test_average)  
print(len(test_average)) 

time.sleep(8)
os.system('cls')
# Create a list of keys, use the .keys() method to retrieve all the keys in the dictionary.
keys = list(test_average.keys())
print(keys)  
print("---")

# Create a list of values, use the .values() method to retrieve all the keys in the dictionary.
vales = list(test_average.values())
print(vales)

time.sleep(8)
os.system('cls')

# Dictionaries are mutable, so you can change, expand, and shrink without making new dictionaries.
# Example:
D = {'eggs': 3, 'spam': 2, 'ham': 1}
# Change an entry we already was this above
D['ham'] = ['grill', 'bake', 'fry']
print(D)
# Delete an entry in the dictionary
# Syntax: del dictionary_name[key]
del D['eggs']
print(D)
# Add a new entry is just the same syntax as updating an entry.
# We are going to add 'brunch' as a key and the value of 'Bacon'
D['brunch'] = 'Bacon'
print(D)

time.sleep(8)
os.system('cls')

### For loop idioms with dictionaries:
test_averages = {'Test 1': 84, 'Test 2': 76, 'Test 3': 94}

# For loop 'in' idiom returns all the keys in the dictionary.
for key in test_averages:
    print(test_averages[key])  # Accessing values using keys

# Use the .items() method to return the key-value pair entries
for key, value in test_averages.items():
    fmt_str = f"Key = {key}, Value = {value}"
    print(fmt_str)  # Formatted string output for key-value pairs

print(test_averages.items())  # Display all items in the dictionary

time.sleep(8)
os.system('cls')
# Dictionary methods
# Documentation: https://docs.python.org/library/stdtypes.html#mapping-types-dict

# Dictionary View Objects:
# The objects returned by dict.keys(), dict.values(), and dict.items() are view objects.
# Provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
# Advantage to these views is that they require a small and fixed amount of memory and processor time.

# SETS:
# A set is collection of uncorded, unique, immutable objects.

# Defining a set using '{. . .}' syntax
colors = {'red', 'black', 'white', 'blue', 'blue'}
print(colors)  # Output: {'red', 'black', 'white', 'blue'} (duplicates removed)
# Defining a set using using the 'set(iterable)' syntax
colors2 = set(['red', 'blue', 'black', 'blue', 'blue'])
# Notice that there are not duplicates{'black', 'blue', 'red'}
print(colors2)  # Output: {'black', 'blue', 'red'} (duplicates removed)

time.sleep(3)
os.system('cls')

# Note: You can't use a literal to create an empty set because Python thinks it's a dictionary.
new_variable = {}
print(type(new_variable))  # Output: <class 'dict'> (not a set)
# Here is a hack to get around that
new_variable = {1}
new_variable.remove(1)  # Remove the element to make it an empty set
print(type(new_variable))  # Output: <class 'set'> (now it's a set)

time.sleep(3)
os.system('cls')

# You can even convert a set from a string, though I confess I'm not clear why you should do this.
# The following creates a set of single strings, 'a', 'b', 'c', 'd', 'e'.
# and another set of single strings, 'b', 'd', 'x', 'y', 'z'
A = set('abcde')
B = set('bdyxz')

print(A)  # Output: {'a', 'b', 'c', 'd', 'e'}
print("---")
print(B)  # Output: {'b', 'd', 'x', 'y', 'z'}

# Union Operation
new_set = A | B
print(new_set)
print("---")
new_set = A.union(B) # Same operation as above but using method
print(new_set)

time.sleep(5)
os.system('cls')
# Difference (difference()) or -):  A set that consists of elements tat are in one set but not the other
# Fun language fact: In Ruby, you can subtract Arrays: arr = [1, 2, 3] - [1, 3] will give you a, arr of [a] in Ruby.
# Python *does not* support this: you have to convert the lists to sets in order to do this, so the same operation in python should be
# arr1 = [1, 2, 3]
# arr2 = [1, 3]
# result = list(set(arr1) - set(arr2))
# print(result)  # Output: [2]
# Intersection (intersection or &)
# Immutable Contraints on Sets:
# Sets can only contain immutable (aka. "hashable") object types.
# Lists and dictionary connot be embedded in sets, but tuples can if you ned to store compound values.
S = {1, 23}
# You cannot do this because it makes an error S.add([1, 2, 3])
# Also not this one S.add({'a': 1})

def fun(name):
    print(f"Hello {name}, welcome to Algorithmics!")

cheer = fun
print(f"The id of fun(): {id(fun)}")
print(f"The id of cheer(): {id(cheer)}")

print(fun('Berny'))
print(cheer('Jack'))

time.sleep(5)
os.system('cls')

# Lambda/Anonymus
greet = lambda : print("Hello World!")
print(greet())

time.sleep(2)
os.system('cls')

# --------------------

def myfunc(n):
    return lambda a : a*n

mydoubler = myfunc(2)
mytripler = myfunc(3)
myNtimes = myfunc(6)

print(mydoubler(11))
print(mytripler(11))
print(myNtimes(5))

time.sleep(3)
os.system('cls')
time.sleep(1)
exit_command = input("That's all for today, the excersices are down below. To clear terminal, press 'x'. ")
if exit_command == 'x':
    print("Clearing Terminal.")
    time.sleep(0.5)
    os.system('cls')
    print("Clearing Terminal..")
    time.sleep(0.5)
    os.system('cls')
    print('Clearing Terminal...')
    time.sleep(0.5)
    os.system('cls')
    print("Clearing Terminal.")
    time.sleep(0.5)
    os.system('cls')
    print("Clearing Terminal..")
    time.sleep(0.5)
    os.system('cls')
    print('Clearing Terminal...')
    time.sleep(0.5)
    os.system('cls')
    print("Clearing Terminal.")
    time.sleep(0.5)
    os.system('cls')
    print("Clearing Terminal..")
    time.sleep(0.5)
    os.system('cls')
    print('Clearing Terminal...')
    time.sleep(0.5)
    os.system('cls')
    print("Terminal Cleared!")
    time.sleep(2)
    os.system('cls')