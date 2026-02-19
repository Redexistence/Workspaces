import time
import os
# Python Collections
# Lists
# Pros and Cons
# Pros:
# 1. Lists are ordered and the order of a list can hold important information in addition ot the data stored in it. Like a queue
# Cons:
# Lists are not computationally efficient. It takes much more time to access and change data in a list than in more efficient kinds of collections.
# Lists are not memory efficient. They take up more space in computer memory than other kinds of collection, as a Python must reserve some space to add more elemtents as necessary.
# Lists are created using square brackets [] and data stored in them are separated by commas. Other collections can be converted to lists using the list() function.
# For example
word_list = ['this', 'is', 'a', 'list', 'of', 'strings']
random_list = [12, 'frog', ['this', 'is', 'a', 'nested', 'list'], True, 3.14]
print(word_list)
print(random_list)
print(random_list[2])
# You can add items to a list usein the append() method or insert() method.
word_list.append('longer')
print(word_list)
word_list.insert(2, 'inserted')
print(word_list)
# You can remove items from a list using the remove() method or the del keyword.
word_list.remove('a')
print(word_list)
del word_list[1]
print(word_list)
# To concatenate two lists, you can use the + operator or the extend() method.
concatenated_list = word_list + random_list
print(concatenated_list)
time.sleep(8)
os.system('cls')

# Tuples
# Tuples are another kind of collection you will run into in Python.
# Tuples are
# - Ordered
# - Immutable
# - Unchangeable
# - Can contain different data types

# Pros and Cons:
# Pros:
# 1. Tuples are faster to access and change data in a tuple than in more efficient kinds of collections.
# 2. Tuples are more memory efficient than lists, as a Python does not need to reserve space to add more elements as necessary.
# Cons:
# 1. Tuples are not changeable. Once a tuple is created, you cannot change its elements.
# 2. Tuples are still computational efficient for accessing data than some other data types.

# Tuples are created using parentheses () and data stored in them are separated by commas. Other collections can be converted to tuples using the tuple() function.
# Since tuples are ordered, they can be accessed like lists, with indicing.
# For example
integer_tuple = (1, 2, 3, 4, 5)
random_tuple = (1, 'horse', integer_tuple, word_list, False)
print(integer_tuple)
print(random_tuple)
print(tuple(word_list))
print(random_tuple[1])
print(type(word_list)) # Check the type of the word_list variable
time.sleep(8)
os.system('cls')
# Remember, you cannot add, remove, or change items in a tuple! However, you can combine two tuples using the + operator or the extend() method.
tuple_1 = (1,2)
tuple_2 = (3,4)
combined_tuple = tuple_1 + tuple_2
print(tuple_1)
print(tuple_2)
print(combined_tuple)

# Characteristics of Dictionaries
# Dictionaries are another kind of collection in Python.
# Dictionaries are
# - Unordered
# - Mutable
# Restriction of keys:
# - Keys must be unique.
# - Keys must be immutable (like numbers, strings, or tuples).
# - Values can be of any data type.
# Pros and Cons:
# Pros:
# Dictionaries are fast. They are very computationally efficient for accessing and changing data.
# Cons:
# Dictionaries
# Examples:
boolean_dict = {'George': True, 'Ahmad': False, 'Juanita': True}
print(boolean_dict)
