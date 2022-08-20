"""
769. Max Chunks To Make Sorted
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
"""


class Solution:
    def maxChunksToSorted(self, arr):
        res = 0
        min_end_idx = arr[0]
        for i in range(len(arr)):
            min_end_idx = max(arr[i], min_end_idx)
            if i == min_end_idx:
                res += 1
        return res
# time: O(n)
# space: O(1)