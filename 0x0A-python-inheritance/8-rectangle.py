#!/usr/bin/python3

"""Module defines a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initializing a Rectangle object
        Args:
            width: width of rectangle
            height: height of rectangle
        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
