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

def f():
    def g():
        print("G")

    g()
    print("H")


f()


