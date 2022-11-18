"""
1239. Maximum Length of a Concatenated String with Unique Characters
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# dp is not applicable since we will not have proper subproblems
# use backtrack
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        strs = []
        for s in arr:
            if len(s) == len(set(list(s))):
                strs.append(s)
        n = len(strs)
        res = 0

        def isValid(s, visited):
            for char in s:
                if char in visited:
                    return False
            return True

        def backtrack(i, visited):
            nonlocal res
            res = max(res, len(visited))

            # early stop / base case
            if res == 26 or i == n:
                return

            for j in range(i + 1, n):
                if isValid(strs[j], visited):
                    for char in strs[j]:
                        visited.add(char)
                    backtrack(j, visited)
                    for char in strs[j]:
                        visited.remove(char)

        for i in range(n):
            backtrack(i, set(list(strs[i])))
        return res