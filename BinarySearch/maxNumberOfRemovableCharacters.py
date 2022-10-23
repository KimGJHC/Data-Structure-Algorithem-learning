"""
1898. Maximum Number of Removable Characters
You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# binary search with relatively efficient validation function
"""


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        l, r = 0, len(removable)

        while l <= r:
            mid = (l + r) // 2
            s_masked = self.mask(s, removable[:mid])
            isValid = self.validSubseq(s_masked, p)

            if isValid:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def validSubseq(self, s, p):
        # check if p is a subseq of s
        np = len(p)
        i = 0

        set_s = set(list(s))
        set_p = set(list(p))
        for letter in set_p:
            if letter not in set_s:
                return False

        for char in s:
            if char == p[i]:
                i += 1
            if i == np:
                return True
        return False

    def mask(self, s, removal):
        s = list(s)
        removal = set(removal)
        res = []

        for i in range(len(s)):
            if i not in removal:
                res.append(s[i])
        return ''.join(res)


