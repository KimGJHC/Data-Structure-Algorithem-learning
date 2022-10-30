"""
487. Max Consecutive Ones II
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

# 2 pointers of sliding window keep track of zeros within the window
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        num_zeros = 0

        while r < len(nums):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros == 2:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res

