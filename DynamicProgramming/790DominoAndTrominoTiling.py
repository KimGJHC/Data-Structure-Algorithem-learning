"""
790. Domino and Tromino Tiling
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

# typical DP questions, consider last part to be verticle/hrizontal domino or upward/downward tromino
"""


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [[0 for _ in range(n + 1)] for _ in range(2)]

        dp[1][1] = 1
        dp[0][2] = 2
        dp[1][2] = 2

        for i in range(3, n + 1):
            dp[0][i] = 2 * dp[1][i - 2] + dp[0][i - 1]
            dp[1][i] = dp[1][i - 1] + dp[1][i - 2] + dp[0][i - 1]

        return dp[1][-1] % MOD