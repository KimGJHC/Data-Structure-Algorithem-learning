"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""


def kthSmallest(root, k):
    # The idea is using an inorder traversal
    res = 0
    count = 0

    def inorder(node):
        nonlocal res
        nonlocal count
        if not node:
            return

        inorder(node.left)
        count += 1
        if count == k:
            res = node.val
        inorder(node.right)

    inorder(root)
    return res

def kthSmallest_v2(root, k):
    # Using stack for inorder traversal
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
