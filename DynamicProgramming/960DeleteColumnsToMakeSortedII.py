"""
960. Delete Columns to Make Sorted III
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.

# dp, consider max number of cols to keep at each index
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n # dp[i] = max number of cols to keep for [s[i:] for s in strs], dp[n-1] = 1 since we will keep 1 letter for length 1 str
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if all([s[i] <= s[j] for s in strs]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
# time: O(n*3)
# space: O(n)