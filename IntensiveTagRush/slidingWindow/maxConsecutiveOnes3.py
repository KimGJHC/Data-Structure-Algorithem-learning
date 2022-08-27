"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

import collections
class Solution:
    def longestOnes(self, nums, k):
        window = collections.deque()
        window_size = 0
        flips = k
        res = 0

        for num in nums:
            if num == 1:
                window.append(num)
                window_size += 1
            elif num == 0:
                if flips <= 0:
                    while window and window[0] != 0:
                        window.popleft()
                        window_size -= 1
                    if window:
                        window.popleft()
                        window_size -= 1
                        flips = min(k, flips + 1)
                if flips > 0:
                    window.append(num)
                    window_size += 1
                    flips -= 1
            res = max(res, window_size)
        return res

# time: O(n)
# space: O(N)
    def longestOnes_v2(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
# solution: keep expanding if possible (K > 0 flip), else keep the range
# time: O(n)
# space: O(1)