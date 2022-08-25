"""
1423. Maximum Points You Can Obtain from Cards
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""


class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        res = 0
        for i in range(k):
            res += cardPoints[i]
        range_sum = res

        for i in range(k):
            range_sum += cardPoints[n - 1 - i] - cardPoints[k - 1 - i]
            res = max(res, range_sum)

        return res
# time: O(k)
# space: O(1)