"""
523. Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# 1. Compute prefix sum, decide valid subarray along the way
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        memo = {0: 0}  # key = prefix sum, value = index of the last element of the prefix sum
        ps = 0

        for i in range(len(nums)):
            ps += nums[i]
            ps %= k

            if ps not in memo:
                memo[ps] = i + 1  # i + 1 to make sure if we find a ps later, it will have at least 2 values
            elif memo[ps] < i:
                return True
        return False