"""
1325. Delete Leaves With a Given Value
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

# typical postorder dfs problem because we will need leaves' information to determine deletion
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def postorder(node):
            # return 1 if node should be deleted, else return -1
            if not node:
                return 1

            left = postorder(node.left)
            right = postorder(node.right)

            if left == 1 and right == 1:
                node.left = None
                node.right = None
                return 1 if node.val == target else -1
            elif left == 1:
                node.left = None
                return -1
            elif right == 1:
                node.right = None
                return -1
            else:
                return -1

        dummy = TreeNode()
        dummy.right = root
        postorder(dummy)
        return dummy.right