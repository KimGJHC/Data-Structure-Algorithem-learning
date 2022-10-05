"""
1216. Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.
"""

from functools import lru_cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # dp[i][j] means the min remove we need to make s[i:j+1] a palindrome
        # base case if dp[i][i] where we already have palindrome with a single letter

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1] <= k

    def isValidPalindrome_v2(self, s: str, k: int) -> bool:

        @lru_cache(maxsize=None)
        def backtrack(l, r, s, k):
            if l >= r and k >= 0:
                return True
            elif k < 0:
                return False
            else:
                if s[l] == s[r]:
                    if backtrack(l + 1, r - 1, s, k):
                        return True
                else:
                    # remove s[l]
                    if backtrack(l + 1, r, s, k - 1):
                        return True

                    # remove s[r]
                    if backtrack(l, r - 1, s, k - 1):
                        return True

                    return False

        return backtrack(0, len(s) - 1, s, k)