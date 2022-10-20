"""
41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

# using index for tracking existing positive integers
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0

        while i < n:
            if 1 <= nums[i] <= n:
                one_based_idx = nums[i] - 1
                if nums[i] != nums[one_based_idx]:
                    nums[i], nums[one_based_idx] = nums[one_based_idx], nums[i]
                    if nums[i] < 1 or nums[i] > n or i == nums[i] - 1:
                        i += 1
                else:
                    i += 1
            else:
                i += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1

        return n + 1