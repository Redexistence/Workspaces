# Python Error and Exception
# A small typing mistake can lead to an erorr in any programming language becuse we must follow the syntax rules while coding in any programming language.
# Same is the case with Python, in this lesson we will learn about syntax errors and exceptions in python.
# Syntax Errors are the most common type of errors in Python. They occur when the Python interpreter encounters a statement that it doesn't understand.
class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0:
            raise ValueError("Age must be non-negative.")
        
        self._name = name
        self._age = age

try:
    p = Person("Sally", 45)
except ValueError as err:
    print(err)
try:
    p = Person(["Sally"], 45)
    print(p._name)
except ValueError as err:
    print(err)
try:
    p = Person("Sally", -1)
    print(p._name)
except ValueError as err:
    print(err)