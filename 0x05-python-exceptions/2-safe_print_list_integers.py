#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try : 
             print("{:d}".format(my_list[j]), end='')
             j += 1
        except Exception as error :
            pass
    print()
    return (j)
