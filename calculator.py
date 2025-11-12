#https://github.com/Sandwich-Monsieur/lab11-DH-JS.git
#Partner 1: Dominic Hung
#Partner 2: Jose Serrano

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except:
        raise ValueError

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError as error:
        return None

def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if b <= 0:
        raise ValueError
    return log(b, a)# use math library + raise ValueError

def exp(a, b): return a**b

"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""


