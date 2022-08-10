"""
510. Inorder Successor in BST II

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

"""

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node):
        res = None

        temp = node
        temp = temp.right

        while temp:
            res = temp
            temp = temp.left

        if res:
            return res

        while node.parent:
            if node.val < node.parent.val:
                return node.parent
            node = node.parent

        return None

# solution 1: think about how we find successor in iterative method of inorder traversal
# time: O(h) in the worst case
# space: O(1)