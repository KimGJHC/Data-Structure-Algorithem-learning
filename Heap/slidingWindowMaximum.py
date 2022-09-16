"""
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= k:
            return [max(nums)]

        maxheap = []
        for i in range(k):
            heapq.heappush(maxheap, (-nums[i], i))

        res = [-maxheap[0][0]]
        for i in range(k, n):
            heapq.heappush(maxheap, (-nums[i], i))
            while maxheap[0][1] < i - k + 1:
                heapq.heappop(maxheap)
            res.append(-maxheap[0][0])
        return res
# time: O(nlogn)
# space: O(n)