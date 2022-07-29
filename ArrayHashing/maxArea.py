"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        return (self.getMaxGap(h, horizontalCuts) * self.getMaxGap(w, verticalCuts)) % (10 ** 9 + 7)

    def getMaxGap(self, width, cuts):
        cuts += [0, width]
        cuts.sort()

        max_gap = 0
        for i in range(len(cuts) - 1):
            max_gap = max(max_gap, cuts[i + 1] - cuts[i])
        return max_gap