"""
513. Find Bottom Left Tree Value
Given the root of a binary tree, return the leftmost value in the last row of the tree.

# bfs
# postorder
"""


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        leftmost_node = root

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            if queue:
                leftmost_node = queue[0]
        return leftmost_node.val