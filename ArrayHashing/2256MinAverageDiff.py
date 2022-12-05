"""
2256. Minimum Average Difference
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

# Compute total sum for O(1) time
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total = sum(nums)
        n = len(nums)
        left_sum = nums[0]
        left_count = 1

        idx = 0
        minn = float('inf')
        while left_count <= n:
            left_avg = left_sum // left_count
            right_avg = ((total - left_sum) // (n - left_count) if (n - left_count) > 0 else 0)
            tmp = abs(left_avg - right_avg)
            if tmp < minn:
                minn = tmp
                idx = left_count - 1
            if left_count == n:
                break
            left_sum += nums[left_count]
            left_count += 1
        return idx