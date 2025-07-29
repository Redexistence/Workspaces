# Function Invocation and Arguments:
# The execution of a function is done by calling it:
import math

def distance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(distance((1, 2), (3, 4)))

# You can pass arguments by name, with default values, and use collectors for extra arguments.
# By default, arguements are matched by position.
# Python allows for default values for arguments, which allows you to specify a value when defining the argument name. You are not required to specify values fpr default arguments when calling the function.

def func(a, b=1, c='spam'):
    print(a, b, c)

func(33)
func(33, 23, 'hello')

# Argument Matching:
# You must place default agruments after non-default arguments.
# Argument Matching: Calling
# The caller can provide arguments by position or by keyword.
# Positional aruments: matched from left to right.
# Keywords: matched by argument name (name=value).

def func(a, b=1, c='spam'):
    print(a, b, c)

func(4, 4, 4)
func(4)
# You may not use func() because the first argument is required.

func('Bob', 'Sally', 'Joe')
func(b='Sally', c='Joe', a='Bob')  # Keyword arguments can be used in any order.
func(c='Joe', a='Bob')  # You can skip the second argument if you want.

# Collecting Keyword Arguments:
def reduce_add(*args):
    s = 0
    for x in args:
        s += x
    return s

print(reduce_add(1, 2, 3, 4, 5))

# Unpacking Arguments:
# Callers can also use:
# *iterables to pass all objects in the iterable object as individual arguments.
# **dict to pass all key-value pairs as individual keyword arguments.
