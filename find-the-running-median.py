#!/bin/python3
# Idea: keep two heap, lower is max heap, higher is min heap.
import sys

from heapq import heappush as push, heappushpop as pushpop


class Spliter:
    def __init__(self):
        self.upper = []
        self.lower = []

    def median(self):
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (self.upper[0] - self.lower[0]) / 2.

    def add(self, value):
        value = pushpop(self.upper, value)
        value = -pushpop(self.lower, -value)
        if len(self.upper) <= len(self.lower):
            push(self.upper, value)
        else:
            push(self.lower, -value)


n = int(input().strip())
a = []
a_i = 0
s = Spliter()
for a_i in range(n):
    a_t = int(input().strip())
    s.add(a_t)
    print(s.median()*1.0)
