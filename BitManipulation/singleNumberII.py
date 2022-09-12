"""
137. Single Number II
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0

        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)
        return once