"""
2330. Valid Palindrome IV
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.
"""


class Solution:
    def makePalindrome(self, s) :
        # a palindrome is always a palindrome after 2 operations

        n = len(s)

        l, r = 0, n - 1

        count_diff = 0
        while l < r:
            if s[l] != s[r]:
                count_diff += 1
            if count_diff > 2:
                return False
            l += 1
            r -= 1
        return True
# time: O(n) for n = len(s)
# space: O(1)