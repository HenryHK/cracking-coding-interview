#!/usr/bin/python3
import queue
from collections import defaultdict


class Graph():
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, s):
        result = [-1 for i in range(self.n)]
        visited = [False for i in range(self.n)]
        q = [s]
        visited[s] = True
        result[s] = 0
        while len(q) > 0:
            current = q.pop()
            height = result[current]
            for neighbor in self.edges[current]:
                if not visited[neighbor]:
                    result[neighbor] = height + 6
                    q = [neighbor] + q
                    visited[neighbor] = True
        result.pop(s)
        print(" ".join(map(str, result)))
