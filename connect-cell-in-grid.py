#!/usr/bin/python3

positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]


def DFS(grid, cor):
    counter = 0
    s = []
    s = [cor] + s
    while len(s) > 0:
        cur = s.pop(0)
        if (grid[cur[0]][cur[1]] == 1):
            grid[cur[0]][cur[1]] = 0
            for pos in positions:
                if cur[0]+pos[0] in range(n) and cur[1]+pos[1] in range(m):
                    s = [(cur[0]+pos[0], cur[1]+pos[1])] + s
            counter += 1
    return counter


def getBiggestRegion(grid):
    max_region = 0
    for i in range(n):
        for j in range(m):
            max_region = max(max_region, DFS(grid, (i, j)))
    return max_region


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
