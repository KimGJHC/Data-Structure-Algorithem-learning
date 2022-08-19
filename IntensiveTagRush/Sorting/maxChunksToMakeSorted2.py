"""
768. Max Chunks To Make Sorted II
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
"""

import collections
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        res = 0
        c1, c2 = collections.Counter(), collections.Counter()
        for n1, n2 in zip(arr, sorted(arr)):
            c1[n1] += 1
            c2[n2] += 1
            if c1 == c2:
                res += 1
                c1, c2 = collections.Counter(), collections.Counter()
        return res
# time: O(n**2logn) for worst case where n = len(arr)
# space: O(n)