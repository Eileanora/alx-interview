#!/usr/bin/python3
''' Making Change '''


def memo(coins, m, v, dp):
    ''' dp memoization '''

    if v == 0:
        return 0

    if dp[v] != -1:
        return dp[v]

    ans = float('inf')

    for i in range(m):
        if coins[i] <= v:
            sub = memo(coins, m, v - coins[i], dp)
            if sub != float('inf') and sub + 1 < ans:
                ans = sub + 1
    dp[v] = ans

    return ans


def makeChange(coins, total):
    ''' Min number of coins to make a given value '''
    dp = [-1 for _ in range(total + 1)]

    ans = memo(coins, len(coins), total, dp) if total > 0 else 0
    return ans if ans != float('inf') else -1
