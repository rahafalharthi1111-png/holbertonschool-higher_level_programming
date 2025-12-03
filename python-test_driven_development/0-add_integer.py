#!/usr/bin/python3
"""
Module for add_integer function.
Provides a function that adds two integers with type checking.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats after casting to int.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not int or float
    """
import math

    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer") if isinstance(a, float) and math.isnan(a):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and math.isnan(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    # Check if a is valid
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")

    # Check if b is valid
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
