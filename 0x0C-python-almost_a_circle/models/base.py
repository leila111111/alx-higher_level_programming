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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        file_name = cls.__name__ + '.json'
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as readeb:
            the_list = readeb.read()
        this_list = []
        seco_list = cls.from_json_string(the_list)
        for i in range(len(seco_list)):
            this_list.append(cls.create(**seco_list[i]))
        return this_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialization CSV method"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as writefile:
            csvwriter = csv.writer(writefile)
            if list_objs is None or list_objs == []:
                writefile.write("[]")
            else:
                for i in list_objs:
                    if cls.__name__ == "Rectangle":
                        list_file = [i.id, i.width, i.height, i.x, i.y]
                    else:
                        list_file = [i.id, i.size, i.x, i.y]
                    csvwriter.writerow(list_file)

    @classmethod
    def load_from_file_csv(cls):
        """ deserialization csv method"""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as readfile:
            reade = csv.reader(readfile)
            csv_list = list(reade)
        if cls.__name__ == "Rectangle":
            list_list = ['id', 'width', 'height', 'x', 'y']
        else:
            list_list = ['id', 'size', 'x', 'y']
        fin_list = []
        for i in csv_list:
            fin_csv = {}
            for ju in enumerate(csv_elem):
                fin_csv[list_list[ju[0]]] = int(ju[1])
            fin_list.append(fin_csv)
        list_for = []
        for i in range(len(fin_list)):
            list_for.append(cls.create(**fin_list[i]))
        return list_for

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares:"""
        for rectangles in list_rectangles:
            up()
            goto(rectangles.x, rectangles.y)
            down()
            color("#b5e3d8")
            for i in range(2):
                forward(rectangles.width)
                left(90)
                forward(rectangles.height)
                left(90)
        for squares in list_squares:
            up()
            goto(squares.x, squares.y)
            down()
            color("#00246B")
            for i in range(2):
                forward(squares.width)
                left(90)
                forward(squares.height)
                left(90)
        done()
