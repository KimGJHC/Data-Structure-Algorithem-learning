"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

import bisect
class Solution:
    def sortedSquares(self, nums):
        first_non_negative = bisect.bisect_left(nums, 0)
        i, j = first_non_negative - 1, first_non_negative

        res = []
        while i >= 0 and j < len(nums):
            if abs(nums[i]) >= abs(nums[j]):
                res.append(nums[j] ** 2)
                j += 1
            else:
                res.append(nums[i] ** 2)
                i -= 1

        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1
        return res
# time: O(n)
# space: O(1) if we do not count space for res