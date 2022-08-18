"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""

class Solution:
    def lengthOfLIS(self, nums):
        from bisect import bisect_left
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub): # num is greater than all elements in sub
                sub.append(num)
            else:
                sub[i] = num # this is not effective if i < len(sub) - 1, it makes sure if i == len(sub) - 1, it will replace the largest of sub
        return len(sub)

# solution: dp
# time: O(nlogn)
# space: O(n)