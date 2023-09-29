#!/usr/bin/python3
"""find_peak function script"""


def find_peak(list_of_integers):
    """function that finds a peak
    in a list of unsorted integers."""

    lenght = len(list_of_integers)
    if lenght == 0:
        return None
    if lenght == 2:
        return max(list_of_integers)
    if lenght == 1:
        return list_of_integers[0]
    i = int(lenght / 2)
    if i > 0 and list_of_integers[i] < list_of_integers[i + 1]:
        return find_peak(list_of_integers[i:])
    if list_of_integers[i] >= list_of_integers[i - 1] and\
            list_of_integers[i] >= list_of_integers[i + 1]:
        return list_of_integers[i]
    if i > 0 and list_of_integers[i] < list_of_integers[i - 1]:
        return find_peak(list_of_integers[:i])
