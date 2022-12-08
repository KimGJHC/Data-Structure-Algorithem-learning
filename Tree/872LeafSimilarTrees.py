"""
872. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# Use postorder traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafSeq(node, seq):
            if not node.left and not node.right:
                seq.append(node.val)
                return

            if node.left:
                getLeafSeq(node.left, seq)

            if node.right:
                getLeafSeq(node.right, seq)

        seq1 = []
        seq2 = []
        getLeafSeq(root1, seq1)
        getLeafSeq(root2, seq2)

        if len(seq1) != len(seq2):
            return False

        for a, b in zip(seq1, seq2):
            if a != b:
                return False
        return True