"""
317. Shortest Distance from All Buildings
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # get locations of all buildings and bfs to get distance
        self.ROW, self.COL = len(grid), len(grid[0])
        self.land2Distance = {}  # key = (x, y), value = [total_distance, reachable]

        reachable = 0
        for x in range(self.ROW):
            for y in range(self.COL):
                if grid[x][y] == 1:
                    self.bfs(x, y, grid, -reachable)
                    reachable += 1

        res = float('inf')
        for total_dist, reach in self.land2Distance.values():
            if reach == reachable:
                res = min(res, total_dist)

        return res if res != float('inf') else -1

    def bfs(self, x, y, grid, reachable_idx):
        queue = deque([(x, y)])
        visited = set()
        dist = 0

        while queue:
            dist += 1
            for _ in range(len(queue)):
                x_curr, y_curr = queue.popleft()
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_n, y_n = x_curr + d[0], y_curr + d[1]
                    if 0 <= x_n < self.ROW and 0 <= y_n < self.COL and grid[x_n][y_n] == reachable_idx and (
                    x_n, y_n) not in visited:
                        visited.add((x_n, y_n))
                        queue.append((x_n, y_n))
                        grid[x_n][y_n] = reachable_idx - 1
                        self.land2Distance[(x_n, y_n)] = self.land2Distance.get((x_n, y_n), [0, 0])
                        self.land2Distance[(x_n, y_n)][0] += dist
                        self.land2Distance[(x_n, y_n)][1] += 1