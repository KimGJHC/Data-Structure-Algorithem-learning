"""
377. Combination Sum IV
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(n):
            # return number of ways using nums to add up to n
            if n == 0:
                return 1

            if n not in memo:
                count = 0
                for num in nums:
                    if n - num >= 0:
                        count += dp(n - num)
                memo[n] = count

            return memo[n]

        return dp(target)