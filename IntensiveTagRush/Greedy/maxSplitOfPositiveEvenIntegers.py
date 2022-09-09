"""
2178. Maximum Split of Positive Even Integers
You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.
"""


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []

        twos = finalSum // 2
        l, r = 0, twos

        while l <= r:
            mid = (l + r) // 2
            total = self.cumsum(mid)
            if total > twos:
                r = mid - 1
            else:
                l = mid + 1
        target = l - 1

        res = [2 * i for i in range(1, target + 1)]
        res[-1] += 2 * (twos - self.cumsum(target))
        return res

    def cumsum(self, n):
        return n * (1 + n) // 2
# solution 1: greedy + binary search
# time: O(log finalSum)

    def maximumEvenSplit_v2(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []

        res = []
        base = 2

        while finalSum:
            if finalSum >= base:
                res.append(base)
                finalSum -= base
                base += 2
            else:
                res[-1] += finalSum
                finalSum = 0
        return res


