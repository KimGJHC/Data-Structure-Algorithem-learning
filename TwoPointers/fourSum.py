"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

# solve nSum recursively, with base case of 2Sum
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        return self.nSum(nums, target, 4)

    def nSum(self, nums, target, n):
        res = []
        if len(nums) == 0 or nums[0] * n > target or nums[-1] * n < target:
            return res
        if n == 2:
            return self.twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for s in self.nSum(nums[i + 1:], target - nums[i], n - 1):
                    res.append([nums[i]] + s)
        return res

    def twoSum(self, nums, target):
        res = []
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target or (l > 0 and nums[l] == nums[l - 1]):
                l += 1
            elif nums[l] + nums[r] > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res
