"""
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float("-inf")

        self.maxPathOfSubtreePassNode(root)

        return self.maxPath

    def maxPathOfSubtreePassNode(self, node):
        """
        return max pathSum that passes node and can be extended in higher layer
        """

        if node.left:
            leftMax = self.maxPathOfSubtreePassNode(node.left)
        else:
            leftMax = 0

        if node.right:
            rightMax = self.maxPathOfSubtreePassNode(node.right)
        else:
            rightMax = 0

        self.maxPath = max(self.maxPath, node.val + leftMax + rightMax)

        return max(0, node.val + leftMax, node.val + rightMax)

# time: O(n)
# space: O(h) to keep the recursion stack