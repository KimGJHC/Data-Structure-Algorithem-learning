"""
2001. Number of Pairs of Interchangeable Rectangles
You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.
"""

from collections import defaultdict
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_to_count = defaultdict(int)

        for width, height in rectangles:
            ratio = width / height
            ratio_to_count[ratio] += 1

        res = 0
        for ratio_count in ratio_to_count.values():
            if ratio_count > 1:
                res += ratio_count * (ratio_count - 1) // 2
        return res