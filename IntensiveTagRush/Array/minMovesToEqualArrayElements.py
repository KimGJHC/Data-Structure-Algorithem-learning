"""
453. Minimum Moves to Equal Array Elements

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.
"""


class Solution:
    def minMoves(self, nums):
        smallest = min(nums)

        return sum([num - smallest for num in nums])

# time: O(n)
# space: O(1)