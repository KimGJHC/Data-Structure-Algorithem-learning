"""
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root):
        import collections

        queue = collections.deque([root])
        have_null = False

        while queue:
            current = queue.popleft()
            if not current:
                have_null = True
                continue
            if have_null:
                return False
            queue.append(current.left)
            queue.append(current.right)
        return True

# solution: Regard a complete binary tree as an array without None in middle if we scan the tree from left to right, top to bottom
# time: O(n)
# space: O(n) in the worst case