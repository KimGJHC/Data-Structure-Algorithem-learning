"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        linkHead = Node(0)
        temp = linkHead

        def inorder(root):
            nonlocal temp

            if not root:
                return None

            inorder(root.left)

            node = Node(root.val)
            temp.right = node
            node.left = temp
            temp = temp.right

            inorder(root.right)

        inorder(root)

        firstNode = linkHead.right
        temp.right = firstNode
        firstNode.left = temp

        return firstNode

# solution 1: inorder + global link build
# time: O(n) where n is size of the tree
# space: O(n)