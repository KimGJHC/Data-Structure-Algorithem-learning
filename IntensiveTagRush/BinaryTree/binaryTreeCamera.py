"""
968. Binary Tree Cameras

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root):
        # state of node (-1: needs to be covered, 0: None, 1: covered, 2: has a camera)
        res = 0

        def postorder(node):
            nonlocal res
            # return status of the node
            if not node:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)

            if left == -1 or right == -1:
                res += 1
                return 2
            elif left == 2 or right == 2:
                return 1
            else:
                return -1

        root_status = postorder(root)
        return res + 1 if root_status == -1 else res

# solution 1: this is greedy algorithm where we start to fill camera at leaf, we may sure we do not fill camera at leaf (unless it is a root)
# time: O(n) where n is the size of tree
# space: O(h) where h is the height of tree
