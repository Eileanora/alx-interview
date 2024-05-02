#!/usr/bin/python3
''' Making Change '''


def makeChange(coins, total):
    ''' Min number of coins to make a given value '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    rem = total
    count = 0
    idx = 0
    while rem > 0 and idx < len(coins):
        if rem >= coins[idx]:
            rem -= coins[idx]
            count += 1
        else:
            idx += 1
    if rem == 0:
        return count

    return -1
