#!/usr/bin/python3
'''Module defining pascal traingle function'''


def pascal_traingle(n):
    '''Function to create pascale traingle of size n'''
    if n <= 0:
        return []
    traingle = []
    for row in range(0, n):
        traingle.append([])
        for col in range(0, row + 1):
            if col == 0 or col == row:
                traingle[row].append(1)
            else:
                traingle[row].append(
                    traingle[row - 1][col]
                    + traingle[row - 1][col - 1])

    return traingle
