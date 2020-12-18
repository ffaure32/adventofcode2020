import numpy as np

from utils import file_utils


def prepare_data(file_name):
    cells = file_utils.get_lines(file_name)
    max_y = len(cells)
    max_x = len(cells[0])
    matrix = np.zeros((1, 1, max_y, max_x)).astype(int)
    for y in range(max_y):
        for x in range(max_x):
            if cells[y][x] == '#':
                matrix[0][0][y][x] = 1
    return matrix


def solution(file_name):
    matrix = prepare_data(file_name)
    for i in range(6):
        matrix = cycle(matrix)
    return matrix.sum()


def cycle(matrix):
    matrix = extend_matrix(matrix)
    matrix_copy = matrix.copy()
    µ, z, y, x = matrix_copy.shape
    for i in range(1, µ - 1):
        for j in range(1, z - 1):
            for k in range(1, y - 1):
                for l in range(1, x - 1):
                    nb = nb_neighbours(matrix, i, j, k, l)
                    if matrix[i][j][k][l] == 1 and nb in (2, 3):
                        matrix_copy[i][j][k][l] = 1
                    else:
                        matrix_copy[i][j][k][l] = 0
                    if matrix[i][j][k][l] == 0 and nb == 3:
                        matrix_copy[i][j][k][l] = 1
    return matrix_copy


def extend_matrix(matrix):
    µ, z, y, x = matrix.shape
    extended_matrix = np.zeros((µ + 4, z + 4, y + 4, x + 4)).astype(int)
    for i in range(µ):
        for j in range(z):
            for k in range(y):
                for l in range(x):
                    extended_matrix[i + 2][j + 2][k + 2][l + 2] = matrix[i][j][k][l]
    return extended_matrix


def nb_neighbours(matrix, i, j, k, l):
    neighbours = 0
    for µ in (i - 1, i, i + 1):
        for z in (j - 1, j, j + 1):
            for y in (k - 1, k, k + 1):
                for x in (l - 1, l, l + 1):
                    if matrix[µ][z][y][x] == 1 and (µ, z, y, x) != (i, j, k, l):
                        neighbours += 1
    return neighbours
