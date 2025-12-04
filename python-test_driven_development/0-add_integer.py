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
                   or if they are NaN or infinity
    """

    # Reject NaN or INF explicitly (Holberton checker requirement)
    for value, name in [(a, "a"), (b, "b")]:
        if isinstance(value, float):
            if value != value or value in (float('inf'), -float('inf')):
                raise TypeError(f"{name} must be an integer")

    # Type validation
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
