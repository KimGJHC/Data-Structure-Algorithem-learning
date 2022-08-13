"""
1763. Longest Nice Substring

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
"""


class Solution:
    def longestNiceSubstring(self, s):
        if not s:
            return ""
        ht = set(s)
        for i, char in enumerate(s):
            if char.swapcase() not in ht:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return max(left, right, key = len)
        return s

# solution: hash set + recursion
# time: O(n logn) for n = len(s)
# space: O(n) for duplicates of s