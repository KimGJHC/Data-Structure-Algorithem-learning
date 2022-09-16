"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
"""

import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = []
        maxheap = []
        res = 0
        j = 0

        for i, num in enumerate(nums):
            heapq.heappush(minheap, (num, i))
            heapq.heappush(maxheap, (-num, i))

            while -maxheap[0][0] - minheap[0][0] > limit:
                j = 1 + min(maxheap[0][1], minheap[0][1])
                while maxheap[0][1] < j:
                    heapq.heappop(maxheap)
                while minheap[0][1] < j:
                    heapq.heappop(minheap)
            res = max(res, i - j + 1)

        return res

# time: O(nlogn) where n = len(nums)
# space: O(n)