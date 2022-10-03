"""
827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.land2size = {}  # key = (x, y) of land 1, value = (identifier, island size)

        n = len(grid)
        identifier = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    self.dfs(x, y, identifier, grid,
                             n)  # 1. add all land of island containing (x, y) in land2size 2. modify the grid of this islands to -1
                    identifier += 1
        if not self.land2size:  # if no island at all
            return 1
        else:
            res = max([size for _, size in self.land2size.values()])
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    res = max(res, self.getSize(x, y, grid, n))

        return res

    def dfs(self, x, y, identifier, grid, n):
        stack = [(x, y)]
        grid[x][y] = -1
        island = []
        size = 0
        while stack:
            x_current, y_current = stack.pop()
            island.append((x_current, y_current))
            size += 1

            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x_n, y_n = x_current + d[0], y_current + d[1]
                if 0 <= x_n < n and 0 <= y_n < n and grid[x_n][y_n] == 1:
                    # one land will enter into stack once
                    grid[x_n][y_n] = -1
                    stack.append((x_n, y_n))
        for x, y in island:
            self.land2size[(x, y)] = (identifier, size)

    def getSize(self, x, y, grid, n):
        size = 1
        visited = set()
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_n, y_n = x + d[0], y + d[1]
            if 0 <= x_n < n and 0 <= y_n < n and grid[x_n][y_n] == -1:
                if self.land2size[(x_n, y_n)][0] not in visited:
                    size += self.land2size[(x_n, y_n)][1]
                    visited.add(self.land2size[(x_n, y_n)][0])
        return size



