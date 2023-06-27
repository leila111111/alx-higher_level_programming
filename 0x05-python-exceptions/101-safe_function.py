#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        point = fct(*args)
        return point
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
