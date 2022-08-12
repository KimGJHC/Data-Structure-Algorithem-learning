"""
449. Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ''

        # get preorder
        preorder = []
        stack = [root]

        while stack:
            current = stack.pop()
            preorder.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return ','.join([str(val) for val in preorder])

    def deserialize(self, data):
        if not data:
            return None

        preorder = [int(val) for val in data.split(',')]
        idx = 0
        n = len(preorder)

        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx == n:
                return None

            val = preorder[idx]

            if val > upper or val < lower:
                return None

            idx += 1
            node = TreeNode(val)
            node.left = helper(lower, val)
            node.right = helper(val, upper)

            return node

        return helper()

# solution 1: using inorder