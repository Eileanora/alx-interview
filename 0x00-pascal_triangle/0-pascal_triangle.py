'''Module defining pascal traingle function'''


def pascal_traingle(n):
    '''Function to create pascale traingle of size n'''
    if n <= 0:
        return []
    pascalTraingle = []
    for row in range(0, n):
        pascalTraingle.append([])
        for col in range(0, row + 1):
            if col == 0 or col == row:
                pascalTraingle[row].append(1)
            else:
                pascalTraingle[row].append(
                    pascalTraingle[row - 1][col]
                    + pascalTraingle[row - 1][col - 1])

    return pascalTraingle
