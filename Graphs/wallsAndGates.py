"""
286. Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
"""

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        EMPTY = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # find all gates
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque([])
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append([r, c])

        # bfs starting from gates
        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if rooms[row][col] == EMPTY:
                    rooms[row][col] = distance
                for d in directions:
                    row_neighbor, col_neighbor = row + d[0], col + d[1]
                    if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and rooms[row_neighbor][
                        col_neighbor] == EMPTY:
                        queue.append([row_neighbor, col_neighbor])
            distance += 1
# time: O(nm)
# space: O(nm)
    def wallsAndGates_v1(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        EMPTY = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # find all gates
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque([])
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))

        # bfs starting from gates
        neigbors = set()
        while queue:
            row, col, distance = queue.popleft()
            if rooms[row][col] == EMPTY:
                rooms[row][col] = distance
            for d in directions:
                row_neighbor, col_neighbor = row + d[0], col + d[1]
                if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and rooms[row_neighbor][
                    col_neighbor] == EMPTY and (row_neighbor, col_neighbor) not in neigbors:
                    queue.append((row_neighbor, col_neighbor, distance + 1))
                    neigbors.add((row_neighbor, col_neighbor))
