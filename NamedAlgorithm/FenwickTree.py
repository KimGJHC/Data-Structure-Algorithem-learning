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
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.arr[i]
            i -= i & (-i)
        return res