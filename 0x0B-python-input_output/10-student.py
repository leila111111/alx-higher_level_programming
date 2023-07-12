#!/usr/bin/python3
""""a class Student that defines
a student by:"""


class Student:
    """Public instance attributes"""

    def __init__(self, first_name, last_name, age):
        """instantation with arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        dictio = {}
        for attr in attrs:
            if hasattr(self, attr):
                new = getattr(self, attr)
                dictio[attr] = new
        return dictio     
