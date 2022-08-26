"""
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

import collections
class Solution:
    def minSubArrayLen(self, target: int, nums):
        queue = collections.deque()
        total = 0
        res = float('inf')
        for num in nums:
            queue.append(num)
            total += num

            if total >= target:
                while queue and total - queue[0] >= target:
                    total -= queue.popleft()
                res = min(res, len(queue))

        return res if res < float('inf') else 0
# time: O(n)
# space: O(n)