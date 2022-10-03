"""
269. Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
"""


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for word in words for char in word}
        n = len(words)
        for i in range(n - 1):
            l1, l2 = self.findOrder(words[i], words[i + 1])
            if l1 == -2:
                return ""
            elif l1 != -1:
                if l2 not in graph[l1]:
                    indegree[l2] += 1
                graph[l1].add(l2)

        stack = deque([key for key in graph if indegree[key] == 0])
        res = []

        graph_size = len(indegree)
        while stack:
            current = stack.pop()
            res.append(current)
            graph_size -= 1

            for nxt in graph[current]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    stack.append(nxt)

        return ''.join(res) if graph_size == 0 else ""

    def findOrder(self, s1, s2):
        # we know s1 < s2 in lexicographical order
        # return letter1, letter2 where letter1 < letter2

        n1, n2 = len(s1), len(s2)

        i, j = 0, 0
        while i < n1 and j < n2:
            if not s1[i] == s2[j]:
                return s1[i], s2[j]
            i += 1
            j += 1
        return (-1, None) if n1 <= n2 else (-2, None)
# use topological sorting

    def alienOrder_v2(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # char not in visited: not visited, visited[char] = False, visisted but not in path, visited[char] = True, visited and in path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        return ''.join(res[::-1])
# topological sorting is reverse of postorder dfs