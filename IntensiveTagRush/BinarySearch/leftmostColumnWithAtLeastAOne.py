"""
1428. Leftmost Column with at Least a One
A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.
"""


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROW, COL = binaryMatrix.dimensions()

        min_col = COL

        for row in range(ROW):
            l, r = 0, COL - 1
            while l < r:
                mid = (l + r) // 2
                if binaryMatrix.get(row, mid) == 1:
                    r = mid
                else:
                    l = mid + 1
            if binaryMatrix.get(row, r) == 0:
                r += 1
            min_col = min(min_col, r)

        return min_col if min_col < COL else -1
# solution 1: binary search on each row
# time: O(nlogn)

    def leftMostColumnWithOne_v2(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROW, COL = binaryMatrix.dimensions()

        min_col = COL

        for row in range(ROW):
            l, r = 0, min_col - 1
            while l < r:
                mid = (l + r) // 2
                if binaryMatrix.get(row, mid) == 1:
                    r = mid
                else:
                    l = mid + 1
            if binaryMatrix.get(row, r) == 0:
                r += 1
            min_col = min(min_col, r)
            if min_col == 0:
                return 0

        return min_col if min_col < COL else -1
# solution 2: refine right boundary every binary search