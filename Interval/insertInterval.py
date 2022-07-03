"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
"""

def insertInterval(intervals, newInterval):
    # The idea is to compare newInterval with each of the intervals and decide its starting value and end value
    if not intervals:
        return [newInterval]

    res, new = [], newInterval

    for i, interval in enumerate(intervals):
        if interval[1] < new[0]:
            res.append(interval)
        elif interval[0] > new[1]:
            res.append(new)
            return res + intervals[i:]
        else:
            new[0] = min(interval[0], new[0])
            new[1] = max(interval[1], new[1])
    res.append(new)
    return res


def test():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    assert insertInterval(intervals, newInterval) == [[1,5],[6,9]]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    assert insertInterval(intervals, newInterval) == [[1,2],[3,10],[12,16]]
    print("All tests passed!")
