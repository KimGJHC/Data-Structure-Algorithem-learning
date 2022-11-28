"""
446. Arithmetic Slices II - Subsequence
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

# The idea is to keep track of the last element of the subseq and the common difference
# since min length allowed is 3, we do not add count[i][diff] directly (count[i][diff] is # of all arithmetic subseq
# with at least 2 elements end at nums[i] with common difference diff)
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0
        count = {}
        for i in range(n):
            count[i] = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                total = count[j].get(diff, 0)
                origin = count[i].get(diff, 0)
                count[i][diff] = total + origin + 1
                res += total
        return res
