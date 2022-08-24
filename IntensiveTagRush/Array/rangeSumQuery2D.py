"""
304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""


class NumMatrix:

    def __init__(self, matrix):
        ROW, COL = len(matrix), len(matrix[0])
        self.memo = [[0 for _ in range(COL)] for _ in range(ROW)]
        self.memo[0][0] = matrix[0][0]

        for col in range(1, COL):
            self.memo[0][col] = matrix[0][col] + self.memo[0][col - 1]

        for row in range(1, ROW):
            rowTotal = 0
            for col in range(COL):
                rowTotal += matrix[row][col]
                self.memo[row][col] = rowTotal + self.memo[row - 1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p1 = self.memo[row2][col2]
        p2 = self.memo[row1 - 1][col1 - 1] if (row1 - 1 >= 0 and col1 - 1 >= 0) else 0
        p3 = self.memo[row2][col1 - 1] if (col1 - 1 >= 0) else 0
        p4 = self.memo[row1 - 1][col2] if (row1 - 1 >= 0) else 0

        return p1 + p2 - p3 - p4

# O(1) time for sumRegion()
# space: O(n*m) size of matrix