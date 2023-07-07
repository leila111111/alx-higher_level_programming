#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    function returning the max of
    a list
    """
    if len(list) == 0:
        return None
    maximum = list[0]
    n = 1
    while n < len(list):
        if list[n] > maximum:
            maximum = list[n]
        n += 1
    return maximum
