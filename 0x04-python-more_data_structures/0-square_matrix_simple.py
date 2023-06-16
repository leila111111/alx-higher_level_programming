def square_matrix_simple(matrix=[]):
    square = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            square[i][j] = matrix[i][j] ** 2

    return square

