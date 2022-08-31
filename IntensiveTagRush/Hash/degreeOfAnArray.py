"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
"""

import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, collections.defaultdict(int)
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] += 1

        res = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] == degree:
                res = min(res, right[x] - left[x] + 1)
        return res

# time: O(n)
# space: O(n)