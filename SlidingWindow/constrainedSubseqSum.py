"""
1425. Constrained Subsequence Sum
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
"""

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(nums)):
            nums[i] += queue[0] if queue else 0
            while queue and nums[i] > queue[-1]:
                queue.pop()
            if nums[i] > 0:
                queue.append(nums[i])
            if i >= k and queue and queue[0] == nums[i-k]:
                queue.popleft()
        return max(nums)