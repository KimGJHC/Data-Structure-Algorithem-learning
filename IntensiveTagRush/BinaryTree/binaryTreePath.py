"""
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        res = []
        path = []

        def dfs(node, path):
            nonlocal res
            if node:
                path.append(str(node.val))
                if not node.left and not node.right:
                    res.append('->'.join(path))
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
                path.pop()

        dfs(root, path)
        return res

# solution: recursion + globle variable. Be careful that do not pass in list pointer in recursion but copy of it, otherwise do backtrack and add + delete
# time: O(n)
# space: O(nh)