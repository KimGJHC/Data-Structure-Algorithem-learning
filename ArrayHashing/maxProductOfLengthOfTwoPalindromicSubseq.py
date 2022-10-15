"""
2002. Maximum Product of the Length of Two Palindromic Subsequences
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        palindrome_mask_to_length = {}
        n = len(s)

        for mask in range(1, 1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]

            if subseq == subseq[::-1]:
                palindrome_mask_to_length[mask] = len(subseq)

        res = 0
        for mask1 in palindrome_mask_to_length:
            for mask2 in palindrome_mask_to_length:
                if mask1 & mask2 == 0:
                    res = max(res, palindrome_mask_to_length[mask1] * palindrome_mask_to_length[mask2])
        return res