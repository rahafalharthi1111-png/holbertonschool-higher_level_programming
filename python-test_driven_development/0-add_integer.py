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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
