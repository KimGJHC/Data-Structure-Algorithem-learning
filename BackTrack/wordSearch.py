"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        n = len(word)

        def dfs(i, row, col, visited):
            if i == n:
                return True
            else:
                lookup = word[i]
                visited.add((row, col))
                for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    row_neig, col_neig = row + direction[0], col + direction[1]
                    if 0 <= row_neig < ROW and 0 <= col_neig < COL and (row_neig, col_neig) not in visited and \
                            board[row_neig][col_neig] == lookup:
                        if dfs(i + 1, row_neig, col_neig, visited):
                            return True
                visited.remove((row, col))
                return False

        lookup = word[0]
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == lookup:
                    if dfs(1, row, col, set()):
                        return True
        return False
