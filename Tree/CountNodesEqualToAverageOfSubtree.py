"""
2265. Count Nodes Equal to Average of Subtree
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postorder(node):
            nonlocal res
            # return sum, number of nodes of subtree
            if not node:
                return 0, 0

            left_sum, left_number = postorder(node.left)
            right_sum, right_number = postorder(node.right)

            total_sum = left_sum + right_sum + node.val
            total_number = right_number + left_number + 1

            if total_sum // total_number == node.val:
                res += 1

            return total_sum, total_number

        postorder(root)
        return res
# time: O(V)
# space: O(h)
