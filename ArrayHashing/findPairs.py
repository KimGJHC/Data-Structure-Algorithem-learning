"""
532. K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.
"""

import collections
def findPairs(nums, k: int):
    nums_count = collections.Counter(nums)
    res = 0

    if k == 0:
        for num in nums_count:
            if nums_count[num] > 1:
                res += 1
    else:
        for num in nums_count:
            if nums_count[num + k] > 0:
                res += 1
    return res

# time: O(n)
# space: O(n)