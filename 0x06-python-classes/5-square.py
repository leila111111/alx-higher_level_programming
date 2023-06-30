#!/usr/bin/python3
"""empty class Square that defines a square:"""


class Square:
    """ class Square with private attribute size:"""
    def __init__(self, size=0):
        """initialisation"""
        self.__size = size

    @property
    def size(self):
        """return the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """instance method that returs the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
