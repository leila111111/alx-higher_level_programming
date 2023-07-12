#!/usr/bin/python3
"""function that inserts a line of
text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of
    text to a file, after each line
    containing a specific"""
    with open(filename, "r") as fr:
        strings = fr.readlines()
    with open(filename, "w") as w:
        for line in strings:
            w.write(line)
            if search_string in line:
                w.write(new_string)
