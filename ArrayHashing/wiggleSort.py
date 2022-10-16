"""
280. Wiggle Sort
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

1. think about locality and greedy
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        alternative = -1  # -1 for i >= i-1, 1 for i <= i-1

        n = len(nums)
        if n <= 1:
            return nums

        i = 1

        while i < n:
            if alternative == -1:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            alternative *= -1
            i += 1