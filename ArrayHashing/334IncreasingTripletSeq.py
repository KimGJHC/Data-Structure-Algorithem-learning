"""
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i]
< nums[j] < nums[k]. If no such indices exists, return false.

# Thought about monotonic increasing stack, but it lacks sense of overall optimal
# Using if control flow to gate logics
# once we find first num2, we are ready for 2 numbers, later updates for num1 and num2 are for lowering num2 potentially
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1, num2 = float('inf'), float('inf')

        for num in nums:
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            else:
                return True
        return False


