"""
1123. Lowest Common Ancestor of Deepest Leaves

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

# first explore info about deepest leaves with bfs, than use postorder dfs
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        queue = deque([root])
        number_deepest = 0
        deepest = 0
        depth = 0

        while queue:
            number_deepest = len(queue)
            deepest = depth
            for _ in range(number_deepest):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        def postorder(node, depth):
            # return current node and number of nodes in deepest layer in subtree rooted at ndoe

            if depth == deepest:
                return node, 1

            if node.left:
                left_node, left_deepest = postorder(node.left, depth + 1)
            else:
                left_node = None
                left_deepest = 0

            if node.right:
                right_node, right_deepest = postorder(node.right, depth + 1)
            else:
                right_node = None
                right_deepest = 0

            if left_deepest == number_deepest:
                return left_node, left_deepest
            elif right_deepest == number_deepest:
                return right_node, right_deepest
            else:
                return node, left_deepest + right_deepest

        res, _ = postorder(root, 0)
        return res

