"""
2221. Find Triangular Sum of an Array
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.
"""


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for j in range(n - 1):
            for i in range(n - j - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]
# time: O(n!)
# space: O(1)

    def triangularSum_v2(self, nums: List[int]) -> int:
        result = 0
        m = len(nums) - 1
        mCk = 1
        for k, num in enumerate(nums):
            result = (result + mCk * num) % 10
            mCk *= m - k
            mCk //= k + 1
        return result
# the frequency of each element is binomial coefficients