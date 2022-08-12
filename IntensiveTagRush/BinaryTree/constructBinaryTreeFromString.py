"""
536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s):
        if not s:
            return None

        stack = []
        current = TreeNode()
        sign = 1

        for char in s:
            if char.isdigit():
                current.val = 10 * current.val + sign * int(char)
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(current)
                current = TreeNode()
                sign = 1
            elif char == ')':
                pre = stack.pop()
                if pre.left == None:
                    pre.left = current
                else:
                    pre.right = current
                current = pre
        return current
# time: O(n) where n = len(s)
# space: O(h)