"""
135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""


class Solution:
    def candy(self, ratings):
        def cumsum(n):
            return (n + 1) * n // 2

        res = 0
        up = 0
        down = 0
        oldSlope = 0

        for i in range(1, len(ratings)):
            newSlope = 1 if ratings[i] > ratings[i - 1] else (-1 if ratings[i] < ratings[i - 1] else 0)

            if (oldSlope > 0 and newSlope == 0) or (oldSlope < 0 and newSlope >= 0):
                res += cumsum(up) + cumsum(down) + max(up, down)
                up = 0
                down = 0

            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                res += 1

            oldSlope = newSlope

        res += cumsum(up) + cumsum(down) + max(up, down) + 1
        return res
# solution 1: think about slopes
# time: O(n)
# space: O(1)