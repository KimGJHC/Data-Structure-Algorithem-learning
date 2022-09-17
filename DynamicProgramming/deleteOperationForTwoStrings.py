"""
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - 2 * lcs

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We can reduce the space complexity to O(min(n1, n2))
        n1, n2 = len(text1), len(text2)
        if n2 < n1:
            text1, text2 = text2, text1
            n1, n2 = n2, n1
        # text1 will always have smaller length
        dp = [[0] * n1 for _ in range(2)]  # dp[0] is previous, dp[1] is current

        # base case
        first_one_1 = -1
        for t1 in range(n1):
            if text2[0] == text1[t1]:
                first_one_1 = t1
                break
        if first_one_1 != -1:
            for t1 in range(first_one_1, n1):
                dp[0][t1] = 1

        first_one_2 = float("inf")
        for t2 in range(n2):
            if text2[t2] == text1[0]:
                first_one_2 = t2
                break

        # inductive steps
        for t2 in range(1, n2):
            dp[1][0] = 0 if t2 < first_one_2 else 1
            for t1 in range(1, n1):
                if text2[t2] == text1[t1]:
                    dp[1][t1] = dp[0][t1 - 1] + 1
                else:
                    dp[1][t1] = max(dp[0][t1], dp[1][t1 - 1])
            dp[0] = dp[1].copy()
        return dp[1][-1] if n2 > 1 else dp[0][-1]