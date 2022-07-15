"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

def diameterOfBinaryTree(root):
    res = 0

    def dfs(node):
        # return the longest depth of node
        if not node:
            return 0
        nonlocal res
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)
        return max(left, right) + 1
    dfs(root)
    return res

