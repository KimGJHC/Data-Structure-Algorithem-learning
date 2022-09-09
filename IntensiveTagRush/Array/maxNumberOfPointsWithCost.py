"""
1937. Maximum Number of Points with Cost
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROW, COL = len(points), len(points[0])
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]

        dp[0] = points[0]

        for row in range(1, ROW):
            for col in range(COL):
                maxx = -1
                for col_prev in range(COL):
                    maxx = max(maxx, dp[row - 1][col_prev] - abs(col - col_prev))
                dp[row][col] = maxx + points[row][col]

        return max(dp[-1])
# dp
# time: O(n*m**2), too slow
    def maxPoints_v2(self, points: List[List[int]]) -> int:
        ROW, COL = len(points), len(points[0])
        pre = curr = points[0]

        for row in range(1, ROW):
            curr = [0] * COL
            left_max, right_max = [pre[0]], [pre[-1]]
            for i in range(1, COL):
                left_max.append(max(left_max[-1] - 1, pre[i]))
                right_max.append(max(right_max[-1] - 1, pre[COL - i - 1]))
            right_max.reverse()

            for col in range(COL):
                curr[col] = max(left_max[col], right_max[col]) + points[row][col]

            pre = curr[:]

        return max(curr)
# time: O(n*m)
# space: O(m)
