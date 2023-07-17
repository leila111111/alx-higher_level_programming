#!/usr/bin/python3
""" Square Class task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting size"""
        self.width = value
        self.height = value

    def __str__(self):
        """square representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update the square attribute"""
        if args:
            for num, val in enumerate(args):
                if num == 0:
                    self.id = val
                elif num == 1:
                    self.size = val
                elif num == 2:
                    self.x = val
                else:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of square instance"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
