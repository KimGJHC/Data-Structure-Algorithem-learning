"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
"""

def invertTree(root):
    if not root:
        return None

    if not root.left and not root.right:
        return root

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root