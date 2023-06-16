#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []

    for i in range(len(matrix)):
        res = []
        for j in range(len(matrix[0])):
            res.append(matrix[i][j] ** 2)
        square.append(res)
    return (square)
