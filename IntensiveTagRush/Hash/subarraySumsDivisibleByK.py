"""
974. Subarray Sums Divisible by K
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""

import collections
class Solution:
    def subarraysDivByK(self, nums, k):
        prefix_sum = []
        left_sum = 0

        for num in nums:
            left_sum += num
            left_sum %= k
            prefix_sum.append(left_sum)

        count = collections.Counter(prefix_sum)

        res = count[0]

        for key in count:
            if count[key] > 1:
                c = count[key]
                res += c * (c-1) // 2
        return res
# solution 1: prefix sum + hash map
# time: O(n + k)
# space: O(n + k)