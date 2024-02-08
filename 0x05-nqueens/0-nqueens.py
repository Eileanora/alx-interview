#!/usr/bin/python3
'''Module for N queens problem.'''
from sys import argv


def is_safe(board, row, col, N):
    '''Checks if a position is safe for a queen.'''
    for i in range(col):
        if board[row][i]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i, j = i - 1, j - 1
    i, j = row, col
    while j >= 0 and i < N:
        if board[i][j]:
            return False
        i, j = i + 1, j - 1
    return True


def solve(board, col, N):
    '''Solves the N queens problem.'''
    # if safe just print the position
    if col == N:
        positions = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    positions.append([i, j])
        print(positions)
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve(board, col + 1, N)
            board[i][col] = 0


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    solve([[0 for i in range(N)] for j in range(N)], 0, N)
