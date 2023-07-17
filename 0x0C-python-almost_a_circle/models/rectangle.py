#!/usr/bin/python3
"""  class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """ class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y gettre"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ public method that returns the area value
        of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """ method that prints in stdout the Rectangle
        instance with the character #"""
        disp = "\n" * self.y
        for i in range(self.height):
            disp += (" " * self.x) + ("#" * self.width) + "\n"

        print(disp, end='')

    def __str__(self):
        """method so that it returns [Rectangle] (<id>) <x>/<y> -
        <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigning  argument to each attribute and updating """
        if args:
            for num, val in enumerate(args):
                if num == 0:
                    self.id = val
                elif num == 1:
                    self.width = val
                elif num == 2:
                    self.height = val
                elif num == 3:
                    self.x = val
                else:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.size = kwargs["width"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "height" in kwargs:
                self.height = kwargs["height"]

    def to_dictionary(self):
        """dictionary representation of rectangle instance"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
