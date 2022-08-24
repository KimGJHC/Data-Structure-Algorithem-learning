"""
529. Minesweeper
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
"""

import collections
class Solution:
    def updateBoard(self, board, click):
        x_limit, y_limit = len(board), len(board[0])

        x_click, y_click = click
        if board[x_click][y_click] == 'M':
            board[x_click][y_click] = 'X'
            return board

        queue = collections.deque([click])
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if board[x][y] != 'E':
                    continue

                mine_count = 0
                for d in directions:
                    x_new, y_new = x + d[0], y + d[1]
                    if 0 <= x_new < x_limit and 0 <= y_new < y_limit and board[x_new][y_new] == 'M':
                        mine_count += 1

                if mine_count == 0:
                    board[x][y] = 'B'
                else:
                    board[x][y] = str(mine_count)

                for d in directions:
                    x_new, y_new = x + d[0], y + d[1]
                    if 0 <= x_new < x_limit and 0 <= y_new < y_limit and board[x_new][y_new] == 'E' and board[x][
                        y] == 'B':
                        queue.append([x_new, y_new])

        return board


# bfs + flow control (recursion only happens at 'B')
# time: O(x_limit * y_limit)
# space: O(1)