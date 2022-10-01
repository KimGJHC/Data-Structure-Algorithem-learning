"""
90. Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(i, path=[]):
            if i == n:
                res.append(path[:])
                return

            # include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            # not include nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path)

        backtrack(0, [])
        return res