#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''Given a number n, returns the fewest number of operations needed to \
    result in exactly n H characters in the file.'''
    def helper(n):
        if n == 1:
            return 0

        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return helper(n // i) + i
        return n
    return helper(n)
