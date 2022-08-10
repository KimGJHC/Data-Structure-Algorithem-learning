"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root):
        res = current = TreeNode(None)

        def inorder(root):
            nonlocal current
            if root:
                inorder(root.left)
                root.left = None
                current.right = root
                current = current.right
                inorder(root.right)

        inorder(root)

        return res.right

# inorder + tree build. The thing we can optimize is to do it in-place
# time: O(n)
# space: O(h)