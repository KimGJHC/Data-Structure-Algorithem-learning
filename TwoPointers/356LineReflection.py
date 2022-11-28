"""
356. Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

Note that there can be repeated points.

# observation 1: if 2 points reflect each other, they need to have same y
# observation 2: a proposed line needs to be at the mean of the smallest and the largest x
"""


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        xtoy = defaultdict(set)

        for x, y in points:
            xtoy[x].add(y)

        xvals = list(xtoy.keys())
        xvals.sort()
        nx = len(xvals)

        l, r = 0, nx - 1
        proposed = (xvals[l] + xvals[r]) / 2

        while l <= r:
            xl = xvals[l]
            xr = xvals[r]
            mid = (xl + xr) / 2

            if mid != proposed:
                return False
            if xl == xr:
                l += 1
                r -= 1
                continue
            if len(xtoy[xl]) != len(xtoy[xr]):
                return False

            for yl in xtoy[xl]:
                if yl not in xtoy[xr]:
                    return False
            l += 1
            r -= 1

        return True