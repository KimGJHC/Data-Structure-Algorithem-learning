"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


def isValidBST(root):
    res = True

    def dfs(node):
        # we need two variables: dfs will min and max of subtree root at node

        if not node.left:
            left = None
        else:
            left = dfs(node.left)

        if not node.right:
            right = None
        else:
            right = dfs(node.right)

        nonlocal res
        if (left and left[1] >= node.val) or (right and right[0] <= node.val):
            res = False

        if not left and not right:
            return node.val, node.val
        if not left:
            return node.val, right[1]
        if not right:
            return left[0], node.val
        return left[0], right[1]

    dfs(root)
    return res

def isValidBST_v2(root):
    def valid(root, minn, maxx):
        if not root:
            return True
        if minn != None and root.val <= minn:
            return False
        if maxx != None and root.val >= maxx:
            return False

        return valid(root.left, minn, root.val) and valid(root.right, root.val, maxx)

    return valid(root, None, None)
