#!/usr/bin/python3

cache = {0: 1}


def ways(n):
    '''
    use cache to store knowledge
    sth like DP
    '''
    if n < 0:
        return 0
    if n in cache:
        return cache[n]
    result = ways(n-1) + ways(n-2) + ways(n-3)
    cache[n] = result
    return result


print(ways(7))
