"""
1302. Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        import collections
        queue = collections.deque([root])

        while queue:
            sum_current_level = 0
            for _ in range(len(queue)):
                current = queue.popleft()
                sum_current_level += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return sum_current_level

# solution: bfs
# time: O(n)
# space: O(n) in worst case for number of leaves