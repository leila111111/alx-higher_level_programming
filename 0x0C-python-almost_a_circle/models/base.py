#!/usr/bin/python3
""" Module containing a class called Base"""
import json
import os
import csv
import turtle


class Base:
    """ class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialisation """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"class method that writes the JSON string representation
        of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dictio_list = []
                for i in list_objs:
                    dictio_list.append(i.to_dictionary())
                jsonfile.write(Base.to_json_string(dictio_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            up = cls(2, 2)
        else:
            up = cls(2)
        up.update(**dictionary)
        return up
