"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

def setZeros_v1(matrix):
    # The key here is to do things inplace and we need to distinguish original 0 and turned 0
    # The idea is to use other value to represent turned 0
    ROW, COL = len(matrix), len(matrix[0])

    for row in range(ROW):
        for col in range(COL):
            if matrix[row][col] == 0:
                # update current cell
                matrix[row][col] = float('inf')
                # update row
                for c in range(COL):
                    if matrix[row][c] != 0:
                        matrix[row][c] = float('inf')
                # update col
                for r in range(ROW):
                    if matrix[r][col] != 0:
                        matrix[r][col] = float('inf')
    for row in range(ROW):
        for col in range(COL):
            if matrix[row][col] == float('inf'):
                matrix[row][col] = 0

    return matrix

# time: O(n^3)

# obviously there are many repetitions in the above solution
# A better idea will be that we only need to know which row and col to be 0, we can use first row and col to be flag
# note that (0, 0) can only hold for one piece of info (either row or col), we need an extra piece of variable
def setZeros(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    # first decide the 1st row and col
    first_col_zero = False
    for r in range(ROW):
        if matrix[r][0] == 0:
            first_col_zero = True
    for c in range(COL):
        if matrix[0][c] == 0:
            matrix[0][0] = 0
            break
    # decide inner
    for r in range(1, ROW):
        for c in range(1, COL):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # filling inner zeros
    for r in range(1, ROW):
        if matrix[r][0] == 0:
            matrix[r] = [0]*COL
    for c in range(1, COL):
        if matrix[0][c] == 0:
            for r in range(1, ROW):
                matrix[r][c] = 0
    # filling outer zeros
    if matrix[0][0] == 0:
        matrix[0] = [0] * COL
    if first_col_zero:
        for r in range(ROW):
            matrix[r][0] = 0
    return matrix

# time: O(n^2)
# space: O(1)



def test():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert setZeros(matrix) == [[1,0,1],[0,0,0],[1,0,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    assert setZeros(matrix) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print("All tests passed!")

