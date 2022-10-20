"""
1498. Number of Subsequences That Satisfy the Given Sum Condition
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        res = 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, MOD)
                l += 1

        return res % MOD