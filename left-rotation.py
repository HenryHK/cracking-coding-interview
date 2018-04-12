#!/usr/bin/python3
# Idea: see the array as a round, cut it from a new point


def array_left_rotation(arr, n, d):
    former = arr[0:d]
    latter = arr[d:]
    new = latter + former
    return new


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
