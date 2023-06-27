#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            print(i, end=' ')
            j += 1
            if i == x:
                break
    except TypeError:
        print("Error: Invalid list element.")
    print("")
    return (i)
