"""
1443. Minimum Time to Collect All Apples in a Tree
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

# consider postorder to know whether we have apples in the subtrees
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        time_spent = 0

        def postorder(node, parent):
            # return if there are apples in subtree
            nonlocal time_spent
            if len(adjList[node]) == 1 and adjList[0] == parent:
                return hasApple[node]

            has_apple = []
            for child in adjList[node]:
                if child == parent:
                    continue
                has_apple.append(postorder(child, node))
            time_spent += sum(has_apple) * 2

            return hasApple[node] or any(has_apple)

        postorder(0, None)
        return time_spent