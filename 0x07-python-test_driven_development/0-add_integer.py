#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a (int or float): The first operand.
        b (int or float, optional): The second operand. Defaults to 98.

    Returns:
        int: The integer addition of a and b.

    Raises:
        TypeError: If either of a or b is not an int or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
