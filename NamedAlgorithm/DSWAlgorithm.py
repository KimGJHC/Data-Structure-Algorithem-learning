"""
DSW is an O(1) space algorithm to balance BST
The algorithm contains 2 parts
1. use right rotation to create a vine
2. use left rotation to compress the vine into a BST

1382. Balance a Binary Search Tree
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        grand = TreeNode(0)
        grand.right = root

        size = self.tree_to_vine(grand)
        height = int(math.log2(size + 1))

        m = 2 ** height - 1

        self.compress(grand, size - m)
        m = m // 2
        while m > 0:
            self.compress(grand, m)
            m //= 2
        return grand.right

    # right rotate
    def tree_to_vine(self, grand):
        size = 0

        tmp = grand.right

        while tmp:
            if tmp.left:
                old_tmp = tmp
                tmp = tmp.left
                grand.right = tmp
                old_tmp.left = tmp.right
                tmp.right = old_tmp
            else:
                size += 1
                grand = tmp
                tmp = tmp.right
        return size

    # left rotate
    def compress(self, grand, m):
        tmp = grand.right
        for i in range(m):
            old_tmp = tmp
            tmp = tmp.right
            grand.right = tmp
            old_tmp.right = tmp.left
            tmp.left = old_tmp
            grand = tmp
            tmp = tmp.right
