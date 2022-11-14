"""
2471. Minimum Number of Operations to Sort a Binary Tree by Level

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.
"""


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        res = 0
        while queue:
            vals = []
            for _ in range(len(queue)):
                current = queue.popleft()
                vals.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res += self.getOps(vals)
        return res

    def getOps(self, vals):
        mp = {num: i for i, num in enumerate(sorted(vals))}
        res = 0
        visited = set()

        for i in range(len(vals)):
            count = 0
            while i not in visited and i != mp[vals[i]]:
                visited.add(i)
                count += 1
                i = mp[vals[i]]
            res += max(0, count - 1)
        return res