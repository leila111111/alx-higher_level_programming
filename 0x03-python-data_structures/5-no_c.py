#!/usr/bin/python3
def no_c(my_string):
    string_deleted = ""
    for i in my_string:
        if  i != 'C' and i != 'c':
            string_deleted += i
    return (string_deleted)
