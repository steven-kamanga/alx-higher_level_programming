#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Function to return the area of the square"""

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character using for loop"""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
            if self.__size == 0:
                print("")
