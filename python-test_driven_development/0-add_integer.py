#!/usr/bin/python3
"""
This module provides a function to safely add two integers.
The inputs must be integers or floats, otherwise an error is raised.
"""


def add_integer(a, b=98):
    """
    Adds two integers (or floats casted to int) and returns the result.
    a and b must be integers or floats, otherwise raise a TypeError.

    >>> add_integer(1, 2)
    3
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return result
