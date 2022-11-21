"""
1926. Nearest Exit from Entrance in Maze
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

# simple bfs with cornor case of entrance at the border
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROW, COL = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            r, c, step = queue.popleft()
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r_new, c_new = r + d[0], c + d[1]

                if 0 <= r_new < ROW and 0 <= c_new < COL:
                    if maze[r_new][c_new] == '.':
                        maze[r_new][c_new] = '+'
                        queue.append((r_new, c_new, step + 1))
                else:
                    if step != 0:
                        return step

        return -1