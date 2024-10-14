# Functions
# Python Functions is a block of statements that return the specific task.

from loguru import logger


def is_even(num):
    """
    the is even is function for finding num to be even or odd
    """

    # x = i % 2 == 0
    #
    # return x

    if num % 2 == 0:
        return "even"

    else:
        return "odd"


output = is_even(5)
logger.info(output)


# 2 types of functions = parameters vs arguments

# types of arguments
# default , positional , keyword

# default arguments
#  are values that are provided while defining functions.

def add(a=1, b=4, c=8):
    """
    default parameter example ...
    """
    return a + b + c


x = add(2, 3)  # we have to give the values

logger.info(x)


# print(add.__doc__)

# positional arguments
# During a function call, values passed through arguments should be in the order
# of parameters in the function definition. This is called positional arguments

def sumofnumbers(a, b, c):
    return a + b + c


logger.info(sumofnumbers(2, 3, 4))


# args
# allows us to pass variable number of non-keyword args to func

def multiply(*args):
    prd = 1

    for i in args:
        prd *= i

    return prd


logger.info(multiply(1, 2, 3, 6, 5, 6))


# kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.


def display(**num):
    for (key, value) in num.items():
        logger.info(f"{key} -> {value}")


print(display(india='delhi', srilanka='colombo', nepal='kathmandu', pakistan='islamabad'))


# without return statement it gives a none statement first and then print the
# output as the python have default types to give a return statement as a "none"

def is_even(num):
    """
    the is even is function for finding num to be even or odd
    """

    # x = i % 2 == 0
    #
    # return x

    if num % 2 == 0:
        print("even")

    else:
        print("odd")


is_even(5)


def h(y):
    num = 6
    num += 1
    print(num)


x = 10
h(5)
print(x)


#  Nested Function

# Example 01

def f():
    def g():
        print("G")

    g()
    print("H")


f()


# Example 02

def g(nums):
    def func():
        n = 'abc'

    nums = nums + 1
    print('in g(x): x =', nums)
    func()
    return nums


n = 3
z = g(x)


# Example 03

def g(x):
    def h(x):
        x = x + 1
        print("in h(x): x = ", x)

    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x


x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)


# Functions are 1st class citizens
# Example 01
def square(num):
    return num ** 2


logger.info(type(square))
# Here it has shown a 1st class function.
# function is a datatype in python it can do all a datatype can do
# squareofnumber = square(5)
# logger.info(squareofnumber)
# you can also delete a func by using
del (square)


# Example 02
def f():
    def x(a, b):
        return a + b

    return x


val = f()(3, 4)
print(val)


# Here the f() func is returning a func as value is this only possible in python


def func_a():
    print('inside func_a')


def func_b(z):
    print('inside func_c')
    return z()


logger.info(func_b(func_a))

# Lambda Functions


# Benefits of using a Function

# - Code Modularity
# - Code Readability
# - Code Reusability

### Lambda Function

# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.


# example 01

squareofnumber = lambda x: x ** 2
logger.info(squareofnumber(6))
"""
Here is a example of lambda func as it is soo easy to use and important 
best feature of python 
"""

sumofnumbers = lambda x, y: x + y
logger.info(sumofnumbers(2, 9))

# Diff between lambda vs Normal Function

# - No name
# - lambda has no return value(in fact,returns a function)
# - lambda is written in 1 line
# - not reusable
#
# Then why use lambda functions?<br>
# **They are used with HOF**

evenoddnumber = lambda x: "even" if x % 2 == 0 else "odd"
logger.info(evenoddnumber(6))

#  Higher order func

# map

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

L = [1, 3, 4, 6, 7, 8]
print(list(map(lambda x:'even' if x % 2 == 0 else 'odd', L)))


# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

ns = list(map(lambda users:users['age'], users))
print(ns)