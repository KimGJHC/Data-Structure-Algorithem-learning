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


    def maxChunksToSorted_v2(self, arr):
        stack = []
        stack.append(arr[0])

        for i in range(1, len(arr)):
            if arr[i] >= stack[-1]:
                stack.append(arr[i])
                continue
            temp = stack[-1]
            while stack and arr[i] < stack[-1]:
                stack.pop()
            stack.append(temp)
        return len(stack)

# solution 2: stack to keep track of the upper of each chunk and merge if lower bound meets previous upper bound
# time: O(n)
# space: O(n)