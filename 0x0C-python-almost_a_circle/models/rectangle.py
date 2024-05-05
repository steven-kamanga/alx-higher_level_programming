#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the height attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the height attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a triangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle instance with character '#' """
        print("\n" * self.y, end="")
        for num in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str rectangle function"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    # def update(self, *args):
    #     """assigns an argument to each attribute"""
    #     arg_length = len(args)
    #     if arg_length > 0:
    #        self.id = args[0]
    #     if arg_length > 1:
    #         self.__width = args[1]
    #     if arg_length > 2:
    #         self.__height = args[2]
    #     if arg_length > 3:
    #         self.__x = args[3]
    #     if arg_length > 4:
    #         self.__y = args[4]

    # try:
        #     self.id = args[0]
        #     self.__width = args[1]
        #     self.__height = args[2]
        #     self.__x = args[3]
        #     self.__y = args[4]
        # except IndexError:
        #     pass

    def update(self, *args, **kwargs):
        """update rectangle attributes
        """
        expectedArgs = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expectedArgs[len(args):len(expectedArgs)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """returns a dictionary representation of a rectangle"""
        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x, "y": self.y
            }
