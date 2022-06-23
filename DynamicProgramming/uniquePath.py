"""
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
"""

def uniquePath(m, n):
    # this is a typical dp question, consider a m*n dp table where dp[i][j] is the number of ways to (i, j) position
    dp = [1] * n
    for row in range(1, m):
        for col in range(1, n):
            dp[col] += dp[col - 1]
    return dp[-1]

def test():
    m = 3
    n = 7
    assert uniquePath(m, n) == 28
    m = 3
    n = 2
    assert uniquePath(m, n) == 3
    print("All tests passed!")