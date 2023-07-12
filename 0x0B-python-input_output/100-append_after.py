#!/usr/bin/python3
"""function that inserts a line of
text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of
    text to a file, after each line
    containing a specific"""
    with open(filename, "r") as fr:
        for line in fr:
            fr.write(line)
            if search_string in line:
                file.write(new_string)
