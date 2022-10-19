"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

# 2D prefix sum
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.matrix = matrix

        for col in range(1, COL):
            self.matrix[0][col] += self.matrix[0][col - 1]

        for row in range(1, ROW):
            self.matrix[row][0] += self.matrix[row - 1][0]
            for col in range(1, COL):
                self.matrix[row][col] += self.matrix[row][col - 1] + self.matrix[row - 1][col] - self.matrix[row - 1][
                    col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p1 = self.matrix[row2][col2]
        p2 = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        p3 = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        p4 = self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return p1 + p4 - p2 - p3