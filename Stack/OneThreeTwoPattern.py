"""
456. 132 Pattern
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

# use monotonically decreasing stack to find 1 of 2 relations of 3 elements
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n3 = -float('inf')

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num < n3:
                return True
            while stack and stack[-1] < num:
                n3 = max(stack.pop(), n3)
            stack.append(num)
        return False