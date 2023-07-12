#!/usr/bin/python3
"""function that returns a list of
lists of integers representing the
Pascal’s triangle of n"""


def pascal_triangle(n):
    """function that returns a list of
    lists of integers"""
    if n <= 0:
        return []
    triangle_list = [[1]]
    for i in range(1, n):
        triangle = [1]
        for j in range(1, i):
            triangle.append(triangle_list[i-1][j-1] + triangle_list[i-1][j])
        triangle.append(1)
        triangle_list.append(triangle)
    return triangle_list
