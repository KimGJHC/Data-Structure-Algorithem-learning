"""
918. Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""


class Solution:
    def maxSubarraySumCircular(self, nums):

        # O(n)
        total = sum(nums)
        # use kdadane for geting max and min sum of subarray

        # O(n)
        maxi = float('-inf')
        current = 0
        for num in nums:
            current = num + max(current, 0)
            maxi = max(maxi, current)

        # O(n)
        mini = float('inf')
        current = 0
        for num in nums:
            current = num + min(current, 0)
            mini = min(mini, current)

        return max(maxi, total - mini if total != mini else float('-inf'))
# use Kadane for calculating max sum and min sum of substrings
# time: O(n)
# space: O(1)


