"""
419. Battleships in a Board
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
"""


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROW, COL = len(board), len(board[0])
        res = 0

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'X':
                    stack = [(r, c)]
                    while stack:
                        r_current, c_current = stack.pop()
                        board[r_current][c_current] = '.'
                        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            r_neig, c_neig = r_current + d[0], c_current + d[1]
                            if 0 <= r_neig < ROW and 0 <= c_neig < COL and board[r_neig][c_neig] == 'X':
                                stack.append((r_neig, c_neig))
                    res += 1
        return res