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
