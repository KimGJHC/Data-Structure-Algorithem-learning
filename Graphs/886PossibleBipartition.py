"""
886. Possible Bipartition
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

# dfs + memorization
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            # return False if there is conflict
            color[node] = node_color
            for neig in adj[node]:
                if color[neig] == color[node]:
                    return False
                if color[neig] == -1:
                    if not dfs(neig, 1 - node_color):
                        return False
            return True

        adj = [[] for _ in range(n + 1)]
        for ai, bi in dislikes:
            adj[ai].append(bi)
            adj[bi].append(ai)

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True