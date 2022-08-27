"""
992. Subarrays with K Different Integers
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""

import collections
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.unique = 0

    def add(self, num):
        if num not in self.count:
            self.unique += 1
        self.count[num] += 1

    def remove(self, num):
        self.count[num] -= 1
        if self.count[num] <= 0:
            self.count.pop(num)
            self.unique -= 1


class Solution:
    def subarraysWithKDistinct(self, nums, k):
        window1, window2 = Window(), Window()
        res = 0
        l1, l2 = 0, 0

        for num in nums:
            window1.add(num)
            window2.add(num)

            while window1.unique > k:
                window1.remove(nums[l1])
                l1 += 1

            while window2.unique >= k:
                window2.remove(nums[l2])
                l2 += 1

            res += l2 - l1
        return res

# time: O(n)
# space: O(n)