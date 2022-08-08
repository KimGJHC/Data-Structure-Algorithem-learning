"""
1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



class Solution:
    def lowestCommonAncestor_v1(self, p, q):
        pAncestor = set()
        qAncestor = set()

        while p or q:
            if p != None:
                pAncestor.add(p)
            if q != None:
                qAncestor.add(q)

            if q in pAncestor:
                return q
            if p in qAncestor:
                return p

            if p != None:
                p = p.parent
            if q != None:
                q = q.parent

# time: O(h) where h is the height of tree
# space: O(n) where n is the size of tree
    def lowestCommonAncestor(self, p, q):
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1

# reduce space to O(1)
