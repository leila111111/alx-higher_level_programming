#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 0:
        print("{} arguments.".format(number))
    elif number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))
    i = 1
    while i <= number:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
