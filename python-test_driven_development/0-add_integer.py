#!/usr/bin/python3
"""
Module for add_integer function.
Adds two integers with strict type checking.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats (after converting to int).

    Args:
        a (int or float)
        b (int or float)

    Returns:
        int: Sum of a and b

    Raises:
        TypeError: if a or b is not int or float,
                   or cannot be converted (NaN/inf/overflow)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # handle nan or inf values
    if a != a or b != b or a in (float('inf'), -float('inf')) or b in (float('inf'), -float('inf')):
        raise TypeError("a must be an integer") if a != a or a in (float('inf'), -float('inf')) else None
        raise TypeError("b must be an integer")

    return int(a) + int(b)
