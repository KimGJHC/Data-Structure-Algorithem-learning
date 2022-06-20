def solution(matrix):
    h, w = len(matrix), len(matrix[0])
    if h == 1:
        return w
    if w == 1:
        return h

    minP = bfs(matrix, 0, 0, h - 1, w - 1)
    for x in range(h):
        for y in range(w):
            if matrix[x][y] == 1:
                matrix[x][y] = 0
                minP = min(minP, bfs(matrix, 0, 0, x, y) + bfs(matrix, x, y, h - 1, w - 1) - 1)
                matrix[x][y] = 1
    return minP


def isValid(x, y, h, w):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    return True


def bfs(matrix, x1, y1, x2, y2):
    # this function returns the shortest path from x1, y1 to x2, y2 without breaking a wall
    # If there is no such path, return infinity
    h, w = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[x1][y1] = 1
    queue = [(x1, y1)]
    count = 1
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        count += 1
        queue_len = len(queue)
        for i in range(queue_len):
            x_cur, y_cur = queue.pop(0)
            for x_neig, y_neig in [(x_cur + x_n, y_cur + y_n) for x_n, y_n in neighbors]:
                if isValid(x_neig, y_neig, h, w) and matrix[x_neig][y_neig] == 0 and visited[x_neig][y_neig] == 0:
                    queue.append((x_neig, y_neig))
                    visited[x_neig][y_neig] = 1
                if x_neig == x2 and y_neig == y2:
                    return count

    return float("inf")