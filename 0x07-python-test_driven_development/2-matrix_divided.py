#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that return a matrix
    where all the elements are
    devided by an element
    """
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element, (int, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    rows = len(matrix)
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise TypeError("Each row of the matrix must have the same size")
    new = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new.append(new_row)
    return new
