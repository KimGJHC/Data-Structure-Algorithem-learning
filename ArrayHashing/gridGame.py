"""
2017. Grid Game
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
"""


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        if n <= 1:
            return 0
        elif n == 2:
            return min(grid[0][1], grid[1][0])

        row_one_prefix = [0] * n
        row_zero_suffix = [0] * n
        grid[0][0] = grid[-1][-1] = 0

        row_one_prefix[0] = grid[1][0]
        for i in range(1, n):
            row_one_prefix[i] = row_one_prefix[i - 1] + grid[1][i]

        row_zero_suffix[-1] = grid[0][-1]
        for i in range(n - 2, -1, -1):
            row_zero_suffix[i] = row_zero_suffix[i + 1] + grid[0][i]

        res = float('inf')
        for desc in range(n):
            res = min(res, max(row_zero_suffix[desc] - grid[0][desc], row_one_prefix[desc] - grid[1][desc]))

        return res
