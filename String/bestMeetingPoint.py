"""
296. Best Meeting Point
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# think about 1D case, where median (numbers of points on left and on right are the same) is the best meeting location
"""


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        ROW, COL = len(grid), len(grid[0])

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    rows.append(row)
                    cols.append(col)
        row = rows[len(rows) // 2]
        cols.sort()
        col = cols[len(cols) // 2]
        return self.get_min_distance_1D(rows, row) + self.get_min_distance_1D(cols, col)

    def get_min_distance_1D(self, points, origin):
        res = 0

        for point in points:
            res += abs(point - origin)
        return res