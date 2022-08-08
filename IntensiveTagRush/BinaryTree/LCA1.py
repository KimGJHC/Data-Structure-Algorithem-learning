"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        res = None

        def dfs(node, p, q):
            # return True if node is ancestor of p or q
            nonlocal res
            if not node:
                return False

            inLeft = dfs(node.left, p, q)
            inRight = dfs(node.right, p, q)

            if node == p:
                if inLeft or inRight:
                    res = node
                return True
            elif node == q:
                if inLeft or inRight:
                    res = node
                return True
            if inLeft and inRight:
                res = node
            return inLeft or inRight

        dfs(root, p, q)
        return res

# time: O(n) where n is the size of tree
# space: O(h) where h is the height of tree, this is from the recursive stack

    def lowestCommonAncestor_v2(self, root, p, q):
        # return the node of lca
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif not left and not right:
            return None
        else:
            return right if not left else left
# The v2 solution removes the use of global variable