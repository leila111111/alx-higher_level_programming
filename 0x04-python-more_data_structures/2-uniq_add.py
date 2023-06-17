#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    res = 0
    for i in my_list:
        if i not in unique:
            res += i
            unique.append(i)
    return(res)
