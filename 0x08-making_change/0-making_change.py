#!/usr/bin/python3
"""
determining the fewest number of coins 
"""
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
