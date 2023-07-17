#!/usr/bin/python3
""" Module containing a class called Base"""
import json
import os
import csv


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
