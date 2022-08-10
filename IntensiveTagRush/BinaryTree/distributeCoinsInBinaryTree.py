"""
979. Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root):
        res = 0

        def postorder(node):
            nonlocal res
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            res += abs(left) + abs(right)
            return node.val + left + right - 1

        postorder(root)
        return res

# solution 1: postorder, adding moves needed at each node with its children
# time: O(n)
# space: O(h)