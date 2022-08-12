"""
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
"""


# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k):
        ht = set()

        stack = [root]
        while stack:
            current = stack.pop()
            if current.val in ht:
                return True
            else:
                ht.add(k - current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        return False

# solution: hashmap + dfs
# time: O(n)
# space: O(n)
