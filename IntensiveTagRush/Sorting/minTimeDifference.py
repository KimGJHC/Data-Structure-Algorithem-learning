"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
"""


class Solution:
    def findMinDifference(self, timePoints):

        def toMin(time):
            time = time.split(':')
            res = 60 * int(time[0]) + int(time[1])
            return res

        for i, time in enumerate(timePoints):
            timePoints[i] = toMin(time)

        res = float("inf")
        timePoints.sort()
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])

        res = min(res, 60 * 24 - timePoints[-1] + timePoints[0])
        return res

# time: O(nlogn)
# space: O(1)