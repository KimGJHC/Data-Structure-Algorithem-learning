"""
545. Boundary of Binary Tree

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Input: root = [1,null,2,3,4]
Output: [1,3,4,2]

Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
"""

def boundaryOfBinaryTree(root):
    # Let's do pre-order traversal
    if not root:
        return []
    res = [root.val]
    def preorder(node, isLeft, isRight):
        if not node:
            return None
        # left boundary or leaves
        if (not node.left and not node.right) or isLeft:
            res.append(node.val)

        if node.left and node.right:
            preorder(node.left, isLeft, False)
            preorder(node.right, False, isRight)
        else:
            preorder(node.left, isLeft, isRight)
            preorder(node.right, isLeft, isRight)
        # right boundary (post order to make it start from bottom)
        if (node.left or node.right) and isRight:
            res.append(node.val)

    preorder(root.left, True, False)
    preorder(root.right, False, True)
    return res