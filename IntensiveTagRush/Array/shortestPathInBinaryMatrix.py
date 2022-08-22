"""
1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        source = (0, 0)
        target = (n - 1, n - 1)

        queue = collections.deque([source])
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == target:
                return distance
            for newRow, newCol in [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1),
                                   (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]:
                if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 0:
                    grid[newRow][newCol] = distance + 1
                    queue.append((newRow, newCol))
        return -1

# time: O(n**2)
# space: O(n**2)