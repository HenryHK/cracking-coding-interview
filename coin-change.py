#!/usr/bin/python3


def make_change(n, coins):
    result = [0 for i in range(n+1)]
    result[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            result[i] += result[i-coin]
    return result[n]
