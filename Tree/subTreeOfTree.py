"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

# the idea is to traverse the trees and check if subtree traversal is in the tree traversal

class Solution:
    def isSubtree(self, root, subRoot):
        tree = self.traverse(root)
        subtree = self.traverse(subRoot)
        if subtree in tree:
            return True
        return False

    def traverse(self, s):
        if s:
            return f"#{s.val}{self.traverse(s.left)}{self.traverse(s.right)}"
        return None
