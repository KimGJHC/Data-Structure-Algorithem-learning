"""
766. Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        for c in range(-ROW + 1, COL):
            constant = -1

            if c < 0:
                r = -c
                c = 0
            else:
                r = 0

            constant = matrix[r][c]
            r += 1
            c += 1

            while r < ROW and c < COL:
                if matrix[r][c] != constant:
                    return False
                r += 1
                c += 1
        return True