"""
1696. Jump Game VI

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
"""

import heapq
class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n  # dp[i] is the max score we can get by ending at index i
        dp[0] = nums[0]
        heap = []

        heapq.heappush(heap, (-dp[0], 0))

        for i in range(1, n):
            while heap[0][1] < i - k:
                heapq.heappop(heap)

            dp[i] = nums[i] - heap[0][0]
            heapq.heappush(heap, (-dp[i], i))

        return dp[-1]

# solution: dp + heap (to quick access nax dp in range)
# time: O(nlogn)
# space: O(n)