"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(postorder.pop())
        node = TreeNode(postorder.pop())
        idx = preorder.index(postorder[-1])

        node.right = self.constructFromPrePost(preorder[idx:], postorder)
        node.left = self.constructFromPrePost(preorder[1:idx], postorder)

        return node

# solution 1: recursion
# time: O(n)
# space: O(h)