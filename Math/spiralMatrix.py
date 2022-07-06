"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

def spiralOrder(matrix):
    res = []
    ROW, COL = len(matrix), len(matrix[0])
    count = ROW * COL
    directions = {'r': (0, 1), 'd':(1, 0), 'l': (0, -1), 'u': (-1, 0)}
    current_direction = 'r'
    switch_direction = {'r': 'd', 'd':'l', 'l':'u', 'u':'r'}
    head = (0, 0)
    BOUND = 101

    while count > 0:
        res.append(matrix[head[0]][head[1]])
        matrix[head[0]][head[1]] = BOUND
        count -= 1
        # check if we can go further
        direction_count = 3
        while direction_count > 0:
            row_candidate, col_candidate = head[0]+directions[current_direction][0], head[1]+directions[current_direction][1]
            if 0 <= row_candidate < ROW and 0 <= col_candidate < COL and matrix[row_candidate][col_candidate] < BOUND:
                head = (row_candidate, col_candidate)
                break
            else:
                current_direction = switch_direction[current_direction]
                direction_count -= 1
        if direction_count == 0:
            break

    return res

def test():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    assert spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("All tests passed!")
