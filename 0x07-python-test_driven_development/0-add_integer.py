#!/usr/bin/python3
"""
Module add-integer
sums two integers

"""


def add_integer(a, b=98):
    """Returns the sum of a and b,
    or raises an exception if a and b are neither floats or ints
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
