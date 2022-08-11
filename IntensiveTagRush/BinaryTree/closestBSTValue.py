"""
270. Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root, target):

        diff = float("inf")
        res = None

        def inorder(node):
            nonlocal res
            nonlocal diff
            if node:
                if node.val > target:
                    inorder(node.left)
                new_diff = abs(target - node.val)
                if new_diff < diff:
                    res = node.val
                    diff = new_diff
                if node.val < target:
                    inorder(node.right)

        inorder(root)
        return res

# solution: inorder + globle variable, need to selectively do inorder on children
# time: O(logn) where n is size of the BST, this is like binary search and every recursive call we discard half of the BST
# space: O(h)