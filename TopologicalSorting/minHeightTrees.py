"""
310. Minimum Height Trees
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = defaultdict(int)

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # topological sorting
        queue = deque()
        for node in degree:
            if degree[node] == 1:
                queue.append(node)

        while len(degree) > 2:
            for _ in range(len(queue)):
                deleted_node = queue.popleft()
                degree.pop(deleted_node)

                for neighbor in graph[deleted_node]:
                    if neighbor in degree:
                        degree[neighbor] -= 1
                        if degree[neighbor] == 1:
                            queue.append(neighbor)
        return list(degree.keys())
# time: O(n)
# space: O(n)