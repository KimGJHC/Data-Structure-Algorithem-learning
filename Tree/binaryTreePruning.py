"""
814. Binary Tree Pruning
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def ContainOne(node):
            # return False is subtree not contain 1
            if not node:
                return False

            left_contain_one = ContainOne(node.left)
            right_contain_one = ContainOne(node.right)

            if not left_contain_one:
                node.left = None
            if not right_contain_one:
                node.right = None

            return left_contain_one or right_contain_one or node.val != 0

        root_contain_one = ContainOne(root)
        return root if root_contain_one else None