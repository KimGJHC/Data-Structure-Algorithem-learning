"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n):
        if n not in self.memo:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            self.memo[n] = ans

        return self.memo[n]

# solution 1: use the fact that left and right of full binary tree is also full
# time: O(2**n)
# space: O(2**n)