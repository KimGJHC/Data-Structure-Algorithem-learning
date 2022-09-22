"""
1120. Maximum Average Subtree
Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float('-inf')

        def postorder(node):
            nonlocal res

            # return sum of all nodes in the subtree, number of nodes in subtree
            if not node:
                return 0, 0

            left_sum, left_number = postorder(node.left)
            right_sum, right_number = postorder(node.right)

            current_sum = left_sum + right_sum + node.val
            current_number = left_number + right_number + 1

            average = current_sum / current_number
            res = max(res, average)
            return current_sum, current_number

        postorder(root)

        return res