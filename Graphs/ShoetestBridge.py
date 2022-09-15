"""
934. Shortest Bridge
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
"""

from collections import deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)

        # get one point from any island
        def getFirst():
            for i, row in enumerate(A):
                for j, point in enumerate(row):
                    if point == 1:
                        return (i, j)

        islandA = []
        boundaries = set()
        # DFS first to find the boundary of first island
        stack = [getFirst()]
        while stack:
            i, j = stack.pop()
            # label it
            A[i][j] = -1
            islandA.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 0:
                        boundaries.add((i, j))
                    elif A[x][y] == 1:
                        stack.append((x, y))

        # all the points on island A is stored in islandA now
        # BFS to expend it
        step = 0
        boundaries = deque(list(boundaries))
        while boundaries:
            for _ in range(len(boundaries)):
                i, j = boundaries.popleft()
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            boundaries.append((x, y))
            step += 1
# time: O(n ** 2)
# space: O(n ** 2)