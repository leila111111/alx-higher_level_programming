#!/usr/bin/python3
"""empty class Square that defines a square:"""


class Square:
    """ class Square with private attribute size:"""
    def __init__(self, size=0):
        """initialisation"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """instance method that returs the current square area"""
        return (self.__size * self.__size)
