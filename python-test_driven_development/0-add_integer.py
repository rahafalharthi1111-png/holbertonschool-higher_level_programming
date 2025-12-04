#!/usr/bin/python3
"""
Module for add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and INF manually (Holberton checker tests them)
    if isinstance(a, float) and (a != a or a == float('inf') or a == -float('inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == -float('inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
