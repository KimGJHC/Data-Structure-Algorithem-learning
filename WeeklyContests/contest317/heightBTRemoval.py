"""
2458. Height of Binary Tree After Subtree Removal Queries
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

# consider depth and heights (obtained from dfs), with max heap
"""


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths, heights = defaultdict(int), defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            heights[node.val] = cur
            return cur

        dfs(root, 0)

        cousins = {}  # key = depth, val = max heap of heights

        for val, depth in depths.items():
            if depth not in cousins:
                cousins[depth] = []
            heapq.heappush(cousins[depth], (-heights[val], val))

        res = []

        for q in queries:
            depth = depths[q]

            if len(cousins[depth]) == 1:
                res.append(depth - 1)
            elif cousins[depth][0][1] == q:
                temp = heapq.heappop(cousins[depth])
                res.append(-cousins[depth][0][0] + depth)
                heapq.heappush(cousins[depth], temp)
            else:
                res.append(-cousins[depth][0][0] + depth)
        return res