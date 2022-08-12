"""
1008. Construct Binary Search Tree from Preorder Traversal

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            node, child = stack[-1], TreeNode(preorder[i])

            while stack and stack[-1].val < child.val:
                node = stack.pop()

            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root

# solution 1: iteration and stack
# time: O(n) where n is len(preorder)
# space: O(h) where h is the height of BST

    def bstFromPreorder_v2(self, preorder):

        idx = 0
        n = len(preorder)

        def helper(lower=float("-inf"), upper=float("inf")):
            nonlocal idx

            if idx == n:
                return None

            val = preorder[idx]

            if val < lower or val > upper:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        return helper()
# solution 2: use recursion