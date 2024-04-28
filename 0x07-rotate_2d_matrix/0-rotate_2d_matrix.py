#!/usr/bin/python3
''' Module for the rotate_2d_matrix method '''


def rotate_2d_matrix(matrix):
    ''' Rotates a 2D matrix 90 degrees clockwise '''
    if type(matrix) is not list or matrix == []:
        return None

    if not all(isinstance(row, list) for row in matrix):
        return None

    n = len(matrix)
    for x in range(n // 2):
        offset = 0
        for y in range(x, n - x - 1):
            top = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = top
            offset += 1
