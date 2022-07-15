"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

def isBalanced(root):
    res = True

    def dfs(node):
        if not node:
            return 0
        nonlocal res
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left - right) > 1:
            res = False
        return max(left, right) + 1

    dfs(root)
    return res