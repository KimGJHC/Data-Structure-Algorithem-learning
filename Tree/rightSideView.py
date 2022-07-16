"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

"""

from collections import deque
class Solution:
    def rightSideView(root):
        if not root:
            return []
        res = []
        queue = deque([root])

        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return res
