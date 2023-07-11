#!/usr/bin/python3
"""function that appends a string at
the end of a text file (UTF8) and
returns the number of characters added:"""


def append_write(filename="", text=""):
    """function that appends a string at
    the end of a text file (UTF8)"""
    with open(filename, 'a') as fr:
        return fr.write(text)
