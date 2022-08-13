"""
427. Construct Quad Tree

Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.
"""

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        if not grid:
            return None
        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid)
        return Node(1,
                    False,
                    self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    self.construct([row[n // 2:] for row in grid[n // 2:]]))

    def isLeaf(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != grid[0][0]:
                    return False
        return True

# solution: recursion
# time: O(n**2 logn)
# space: O(n**2) where n is len(grid)

    def construct_v2(self, grid):

        def helper(grid, x, y, length):
            if length == 1:
                return Node(grid[x][y], True, None, None, None, None)
            node = Node(1, False)
            node_TL = helper(grid, x, y, length//2)
            node_TR = helper(grid, x, y + length // 2, length // 2)
            node_BL = helper(grid, x + length // 2, y, length // 2)
            node_BR = helper(grid, x + length // 2, y + length // 2, length // 2)
            if node_TL.isLeaf and node_TR.isLeaf and node_BR.isLeaf and node_BL.isLeaf and node_BR.val == node_TL.val and node_BR.val == node_BL.val and node_BR.val == node_TR.val:
                node.isLeaf = True
                node.val = node_TL.val
            else:
                node.topLeft = node_TL
                node.topRight = node_TR
                node.bottomLeft = node_BL
                node.bottomRight = node_BR
            return node

        return helper(grid, 0, 0, len(grid))
# time: O(n ** 2) where n is len(grid) by postorder traversal


