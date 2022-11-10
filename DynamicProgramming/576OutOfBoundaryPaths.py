"""
576. Out of Boundary Paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

# consider top-down dp with cache
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.ROW, self.COL = m, n
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def helper(Move, startRow, startColumn):
            # number of ways to get out of the board with exactly Move steps with particular starting point

            if startRow < 0 or startRow >= self.ROW or startColumn < 0 or startColumn >= self.COL:
                if Move == 0:
                    return 1
                return 0

            if Move <= 0:
                return 0

            res = 0
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_startRow, new_startColumn = startRow + d[0], startColumn + d[1]
                res += helper(Move - 1, new_startRow, new_startColumn)
            return res

        res = 0
        for Move in range(1, maxMove + 1):
            res += helper(Move, startRow, startColumn)
        return res % MOD

# time: O(maxMove * m * n)
# space: O(maxMove * m * n)