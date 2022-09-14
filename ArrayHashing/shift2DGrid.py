"""
1260. Shift 2D Grid
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""

from functools import reduce
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROW, COL = len(grid), len(grid[0])
        total = ROW * COL
        flatten = reduce(lambda x, y: x + y, grid)
        k %= total

        new_flatten = flatten[total - k:] + flatten[:total - k]

        for r in range(ROW):
            for c in range(COL):
                grid[r][c] = new_flatten[COL * r + c]
        return grid
