#!/usr/bin/python3
"""This module contains a function that prints a square with the character #."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
