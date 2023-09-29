#!/usr/bin/python3
"""find_peak function script"""


def find_peak(list_of_integers):
    """function that finds a peak
    in a list of unsorted integers."""

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    i = int(len(list_of_integers) / 2)
    if i > 0 and list_of_integers[i] < list_of_integers[i + 1]:
        return find_peak(list_of_integers[i:])
    if list_of_integers[i] >= list_of_integers[i - 1] and\
            list_of_integers[i] >= list_of_integers[i + 1]:
        return list_of_integers[i]
    if i > 0 and list_of_integers[i] < list_of_integers[i - 1]:
        return find_peak(list_of_integers[:i])
