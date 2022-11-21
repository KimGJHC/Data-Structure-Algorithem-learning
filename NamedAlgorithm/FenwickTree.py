"""
Fenwick tree (Binary Indexed Tree) is a data structure that can efficiently
1. update elements
2. calculate prefix sums in a table of numbers.

Fenwick tree achieves O(logn) time for both of the operations
Alternative solution will be segment tree
"""

class Fenwick:
    def __init__(self, nums):
        self.n = len(nums)
        self.arr = [0] * (self.n+1)

        for i in range(self.n):
            self.modify(i, nums[i])

    def modify(self, i, val):
        i += 1
        while i <= self.n:
            self.arr[i] += val
            # flip the right most 1-bit of i
            # i = 2 ** p + 2 ** (p-1) + ... + 2 ** 1 + 2 ** 0
            # sons of i in the BITree
            # -i is flip all bits and add 1
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.arr[i]
            # parent of i in the BITree
            i -= i & (-i)
        return res