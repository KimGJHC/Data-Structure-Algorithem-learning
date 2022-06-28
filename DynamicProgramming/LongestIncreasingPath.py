"""
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4

Input: matrix = [[1]]
Output: 1
"""
from collections import deque

def longestIncreasingPath_v1(matrix):
    '''
    The idea is to maintain a dp table such that dp[i][j] is the longest distance starting at matrix[i][j]
    The transition function will be dp[i][j] = max(its neighbors with matrix[x][y] > matrix[i][j])
    cells with smaller value depends on neighbors with larger value, we need to proceed neighbor with larger value first
    We could decide the process order with topological order. We create a graph and let the cell be vertices and create a forward edge to neighbor if its value is larger than the neighbors value
    :param matrix:
    :return:
    '''

    ROW, COL = len(matrix), len(matrix[0])
    # topological order
    graph = {(row, col): [] for row in range(ROW) for col in range(COL)}
    indegree = {(row, col): 0 for row in range(ROW) for col in range(COL)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row in range(ROW):
        for col in range(COL):
            for d in directions:
                row_neighbor, col_neighbor = row+d[0], col+d[1]
                if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and matrix[row][col] > matrix[row_neighbor][col_neighbor]:
                    graph[(row, col)].append((row_neighbor, col_neighbor))
                    indegree[(row_neighbor, col_neighbor)] += 1
    queue = deque([(row, col) for row in range(ROW) for col in range(COL) if indegree[(row, col)] == 0])
    order = []
    while queue:
        row, col = queue.popleft()
        for row_neighbor, col_neighbor in graph[(row, col)]:
            indegree[(row_neighbor, col_neighbor)] -= 1
            if indegree[(row_neighbor, col_neighbor)] == 0:
                queue.append((row_neighbor, col_neighbor))
        order.append((row, col))

    # dp
    dp = [[0]*COL for _ in range(ROW)]
    for row, col in order:
        for d in directions:
            row_neighbor, col_neighbor = row + d[0], col + d[1]
            if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and matrix[row][col] < matrix[row_neighbor][col_neighbor]:
                dp[row][col] = max(dp[row][col], dp[row_neighbor][col_neighbor])
        dp[row][col] += 1

    # find max length
    res = 0
    for row in range(ROW):
        for col in range(COL):
            if res < dp[row][col]:
                res = dp[row][col]
    return res
# time: O(m*n)
# Space: O(m*n)

def longestIncreasingPath(matrix):
    # its time complexity is good, but it is slow because of implementation
    # we do not need to explicitly track the graph
    ROW, COL = len(matrix), len(matrix[0])
    outdegree = [[0] * COL for _ in range(ROW)] # number of neighbors larger than the cell
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row in range(ROW):
        for col in range(COL):
            for d in directions:
                row_neighbor, col_neighbor = row + d[0], col + d[1]
                if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and matrix[row][col] < matrix[row_neighbor][col_neighbor]:
                    outdegree[row][col] += 1
    depth = 0
    queue = deque([(row, col) for row in range(ROW) for col in range(COL) if outdegree[row][col] == 0])
    while queue:
        depth += 1
        queue_length = len(queue)
        for _ in range(queue_length):
            row, col = queue.popleft()
            for d in directions:
                row_neighbor, col_neighbor = row + d[0], col + d[1]
                if 0 <= row_neighbor < ROW and 0 <= col_neighbor < COL and matrix[row][col] > matrix[row_neighbor][col_neighbor]:
                    outdegree[row_neighbor][col_neighbor] -= 1
                    if outdegree[row_neighbor][col_neighbor] == 0:
                        queue.append((row_neighbor, col_neighbor))
    return depth


def test():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert longestIncreasingPath(matrix) == 4
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    assert longestIncreasingPath(matrix) == 4
    matrix = [[1]]
    assert longestIncreasingPath(matrix) == 1
    print("All tests passed!")

