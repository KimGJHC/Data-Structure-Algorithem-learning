"""
2486. Append Characters to String to Make Subsequence
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        ns = len(s)
        nt = len(t)

        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return nt - j