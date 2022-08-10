"""
173. Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root):
        self.current = TreeNode(-1)
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if self.current.val < 0:
            self.current = self.stack[-1]
        else:
            self.current = self.stack.pop()
            if self.current.right:
                self.current = self.current.right
                while self.current:
                    self.stack.append(self.current)
                    self.current = self.current.left
            self.current = self.stack[-1]
        return self.current.val

    def hasNext(self) -> bool:
        return len(self.stack) > 1 or self.current.right or self.current.val < 0

# The solution that do inorder traversal at beginning is trivial
# Solution: inorder + stack with controlled stack growth
# time: O(n)
# space: O(h)