"""
498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""


class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        N, M = len(mat), len(mat[0])

        row, col = 0, 0
        direction = 1
        res = []

        while row < N and col < M:
            res.append(mat[row][col])

            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)

            if new_row < 0 or new_row == N or new_col < 0 or new_col == M:
                if direction == 1:
                    row += (col == M - 1)
                    col += (col < M - 1)
                else:
                    col += (row == N - 1)
                    row += (row < N - 1)

                direction = 1 - direction
            else:
                row = new_row
                col = new_col

        return res

# time: O(N*M)
# space: O(1)
