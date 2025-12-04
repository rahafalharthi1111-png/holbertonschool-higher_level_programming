#!/usr/bin/python3
"""
Module for add_integer function.
Adds two integers with type checking.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not int or float,
                   or if they cannot be converted to int (NaN/inf/overflow)
    """

    # Type validation first
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Try converting to int and catch conversion errors (NaN / inf / overflow)
    try:
        ia = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        ib = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return ia + ib
