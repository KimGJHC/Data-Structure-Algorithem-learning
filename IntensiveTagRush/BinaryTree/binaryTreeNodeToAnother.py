"""
2096. Step-By-Step Directions From a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
"""


class Solution:

    def getDirections(self, root, startValue, destValue):

        root = self.getLCA(root, startValue, destValue)

        pathToStart = pathToEnd = ''
        stack = [(root, '')]

        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                pathToStart = path
            elif node.val == destValue:
                pathToEnd = path
            if node.left:
                stack.append((node.left, path + 'L'))
            if node.right:
                stack.append((node.right, path + 'R'))

        return 'U' * len(pathToStart) + pathToEnd

    def getLCA(self, root, startValue, destValue):
        if root == None or root.val == startValue or root.val == destValue:
            return root

        left = self.getLCA(root.left, startValue, destValue)
        right = self.getLCA(root.right, startValue, destValue)

        return root if left and right else left or right

# solution 1: LCA + DFS
# time: O(n) where n is the size of the tree
# Space: O(h) from string concatenation and h is the height of the tree


# solution 2: create graph + BFS