#!/usr/bin/python3
"""The Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class which inherits from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size property which
        is the same as the width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the size property"""
        self.width = self.height = value

    def __str__(self):
        """public str method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update square attributes
        """

        expectedArgs = (self.id, self.size, self.x, self.y)
        if args != ():
            self.id, self.size, self.x, self.y = \
                args + expectedArgs[len(args):len(expectedArgs)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """returns a dictionary representation of a rectangle"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
