"""

"""


class Solution:
    def minMoves2(self, nums):
        # find median
        median = sorted(nums)[len(nums) // 2]

        res = 0
        for num in nums:
            res += abs(num - median)

        return res

# solution 1: find median + sum up difference of each num to median
# time: O(nlogn)
# space: O(n)

# we should use quickselect to find median, which has time O(n) on average
    def minMoves2_v2(self, nums):
        def getMedian(nums):

