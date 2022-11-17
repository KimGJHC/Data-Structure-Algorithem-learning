"""
223. Rectangle Area
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = self.getRectArea(ax1, ay1, ax2, ay2)
        b = self.getRectArea(bx1, by1, bx2, by2)

        # get intersection
        if ax1 > bx1:
            ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = bx1, by1, bx2, by2, ax1, ay1, ax2, ay2

        if bx1 >= ax2 or by1 >= ay2 or by2 <= ay1:
            intersect = 0
        else:
            ix1 = bx1
            iy1 = max(ay1, by1)
            ix2 = min(ax2, bx2)
            iy2 = min(ay2, by2)
            intersect = self.getRectArea(ix1, iy1, ix2, iy2)

        return a + b - intersect

    def getRectArea(self, ax1, ay1, ax2, ay2):
        return (ax2 - ax1) * (ay2 - ay1)