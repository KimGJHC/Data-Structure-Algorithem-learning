"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:1 + root_idx], inorder[:root_idx])
    root.right = buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])
    return root