"""
939. Minimum Area Rectangle

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
"""

import collections
class Solution:
    def minAreaRect(self, points):
        ht = collections.defaultdict(list)
        for x, y in points:
            ht[x].append(y)
        lastx = {}
        res = float('inf')

        for x in sorted(ht):
            column = ht[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[(y1, y2)]) * (y2 - y1))
                    lastx[(y1, y2)] = x
        return res if res < float('inf') else 0

# solution: hashmap + sorting
# time: O(n**2) where n = len(points)
# space: O(n)