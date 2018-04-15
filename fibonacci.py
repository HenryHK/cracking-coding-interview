#!/usr/bin/python3


def fibonacci(n):
    mem = [-1 for i in range(n)]
    mem[0] = 1
    mem[1] = 1
    for i in range(2, n):
        mem[i] = mem[i-1]+mem[i-2]
    return mem[n-1]


print(fibonacci(6))
