"""
1066. Campus Bikes II

On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

# backtrack is TLE
# DP + bitmask
"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        res = float('inf')
        n = len(workers)
        m = len(bikes)

        def backtrack(i, unvisited, curr_dist):
            # assign workers[i] to one of bikes[j] where j is unvisited
            nonlocal res
            if curr_dist >= res:
                return

            if i == n:
                res = curr_dist
                return

            for j in unvisited.copy():
                unvisited.remove(j)
                dist = get_dist(workers[i], bikes[j])
                curr_dist += dist
                backtrack(i + 1, unvisited, curr_dist)
                unvisited.add(j)
                curr_dist -= dist

        def get_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        backtrack(0, set(list(range(m))), 0)
        return res

    def assignBikes_v2(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def get_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        n, m = len(workers), len(bikes)

        dp = [[sys.maxsize] * (1 << m) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, worker in enumerate(workers):
            for bit_bike in range((1 << m)):
                for j, bike in enumerate(bikes):
                    _get = bit_bike & (1 << j)
                    _set = bit_bike | (1 << j)
                    if not _get:
                        dp[i + 1][_set] = min(
                            dp[i + 1][_set],
                            dp[i][bit_bike] + get_dist(worker, bike)
                        )
        return min(dp[-1])