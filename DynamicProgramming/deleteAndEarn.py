"""
740. Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
"""

from functools import cache
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums):
        points = defaultdict(int)
        max_number = 0

        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            return max(dp(num - 1), dp(num - 2) + points[num])

        return dp(max_number)