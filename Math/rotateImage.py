"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

def rotate(matrix):
    n = len(matrix)

    for i in range(0, n // 2): # rotate the i-th layer
        layer_size = n - 2*i
        if layer_size > 1:
            for j in range(0, layer_size-1):
                matrix[i][i+j], matrix[i+j][n-i-1], matrix[n-i-1][n-i-j-1], matrix[n-i-j-1][i] = matrix[n-i-j-1][i], matrix[i][i+j], matrix[i+j][n-i-1], matrix[n-i-1][n-i-j-1]

    return matrix

def test():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate(matrix) == [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    assert rotate(matrix) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print("All tests passed!")
