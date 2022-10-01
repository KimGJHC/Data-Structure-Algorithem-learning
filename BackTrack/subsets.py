"""
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(first_idx, length, current):
            nonlocal res
            if len(current) == length:
                res.append(current[:])
                return
            for i in range(first_idx, n):
                current.append(nums[i])
                backtrack(i + 1, length, current)
                current.pop()

        for length in range(n + 1):
            backtrack(0, length, [])

        return res