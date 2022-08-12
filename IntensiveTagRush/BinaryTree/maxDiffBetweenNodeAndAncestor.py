"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        max_diff = 0

        def postorder(node):
            # return max, min of nodes in subtree rooted at node
            nonlocal max_diff

            if not node:
                return None, None

            left_max, left_min = postorder(node.left)
            right_max, right_min = postorder(node.right)

            max_diff = max(max_diff,
                           abs(node.val - left_max) if left_max != None else 0,
                           abs(node.val - left_min) if left_min != None else 0,
                           abs(node.val - right_max) if right_max != None else 0,
                           abs(node.val - right_min) if right_min != None else 0, )

            return max(left_max if left_max != None else 0, right_max if right_max != None else 0, node.val), min(
                left_min if left_min != None else float('inf'), right_min if right_min != None else float('inf'),
                node.val)

        postorder(root)
        return max_diff

# solution 1: postorder + globle variable
# time: O(n)
# space: O(h)
    def maxAncestorDiff_v2(self, root):

        def helper(node, current_max, current_min):
            if not node:
                return current_max - current_min

            current_max = max(current_max, node.val)
            current_min = min(current_min, node.val)
            left = helper(node.left, current_max, current_min)
            right = helper(node.right, current_max, current_min)
            return max(left, right)

        return helper(root, root.val, root.val)
# solution 2: preorder + pass in historical values