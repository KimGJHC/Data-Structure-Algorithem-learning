"""
862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
"""
import collections
class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)

        prefix_sums = [0] # prefix[i] = sum(nums[:i])
        for i in range(n):
            prefix_sums.append(prefix_sums[-1] + nums[i])

        res = n + 1
        queue = collections.deque()

        for l, y in enumerate(prefix_sums):
            while queue and y <= prefix_sums[queue[-1]]:
                queue.pop()

            while queue and y - prefix_sums[queue[0]] >= k:
                res = min(res, l - queue.popleft())

            queue.append(l)
        return res if res < n+ 1 else -1