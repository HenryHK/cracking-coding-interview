#!/usr/bin/python3
import math


def isPrime(n):
    if n == 1:
        return False
    result = True
    for i in range(2, int(math.sqrt(n))+1):
        result = result and (n/i) % 1 > 0
    return result
