"""
823. Binary Trees With Factors
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
"""

import collections
class Solution:
    def numFactoredBinaryTrees(self, arr):
        ht = collections.defaultdict(int)  # {key: freq} freq is the number of valid binary trees with root at key
        arr.sort()

        for num in arr:
            temp_count = 0
            for child in ht:
                other_child = num // child
                if num % child == 0 and other_child in ht:
                    temp_count += ht[child] * ht[other_child]
            ht[num] = temp_count + 1

        return sum(ht.values()) % (10 ** 9 + 7)
# time: O(n**2) where n = len(arr)
# space: O(n)