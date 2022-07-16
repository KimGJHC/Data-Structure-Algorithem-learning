"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

# The idea is to traverse the tree like traversing a graph with bfs

from collections import deque

def levelOrder(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        queue_length = len(queue)
        level_res = []
        for _ in range(queue_length):
            current = queue.popleft()
            level_res.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        res.append(level_res)
    return res
