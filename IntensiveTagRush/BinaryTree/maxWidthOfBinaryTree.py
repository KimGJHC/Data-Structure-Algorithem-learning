"""
662. Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        import collections
        if not root:
            return 0

        max_width = 0

        queue = collections.deque([(root, 0)])

        while queue:
            _, level_head_index = queue[0]

            for i in range(len(queue)):
                current, idx = queue.popleft()
                if current.left:
                    queue.append((current.left, 2 * idx))
                if current.right:
                    queue.append((current.right, 2 * idx + 1))
            max_width = max(max_width, idx - level_head_index + 1)

        return max_width

# solution 1: bfs + index
# time: O(n)
# space: O(2**h) in the worst case