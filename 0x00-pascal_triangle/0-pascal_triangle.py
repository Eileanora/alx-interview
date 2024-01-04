#!/usr/bin/python3
'''Module defining pascal traingle function'''


def pascal_triangle(n):
    '''Function to create pascale traingle of size n'''
    if n <= 0:
        return []
    triangle = []
    for row in range(0, n):
        triangle.append([])
        for col in range(0, row + 1):
            if col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(
                    triangle[row - 1][col]
                    + triangle[row - 1][col - 1])

    return triangle
