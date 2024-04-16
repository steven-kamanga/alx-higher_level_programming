#!/usr/bin/python3

"""Module defines a rectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """SSquare representation"""

    def __init__(self, size):
        """Initializing a Square object

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
