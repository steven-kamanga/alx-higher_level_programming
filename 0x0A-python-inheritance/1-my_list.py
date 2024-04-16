#!/usr/bin/python3

"""Module defines a MyList class"""


class MyList(list):
    """A class that inherits from list"""

    def __init__(self):
        """Initialize a MyList object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
