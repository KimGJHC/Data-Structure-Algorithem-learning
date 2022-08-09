"""
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""

import collections


class Solution:
    def verticalTraversal(self, root):
        colInfo = collections.defaultdict(list)

        stack = [(root, 0, 0)]  # stack stores node and it's coordinates

        while stack:
            node, row, col = stack.pop()
            colInfo[col].append((row, node.val))

            if node.left:
                stack.append((node.left, row + 1, col - 1))
            if node.right:
                stack.append((node.right, row + 1, col + 1))
        orderedCol = sorted(colInfo.keys())

        res = []
        for col in orderedCol:
            res.append([val for _, val in sorted(colInfo[col], key=lambda x: (x[0], x[1]))])

        return res

# time: O(nlog(n)) where n is the size of tree
# space: O(n)