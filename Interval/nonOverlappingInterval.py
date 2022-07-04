"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Input: intervals = [[1,2],[2,3]]
Output: 0
"""

from collections import deque
def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    intervals = deque(intervals)
    res = 0

    _, limit = intervals.popleft()
    while intervals:
        next = intervals.popleft()
        if next[0] >= limit:
            limit = next[1]
            continue
        else:
            res += 1
            limit = min(limit, next[1])
    return res

# time: O(nlogn)
# space: O(n)




def test():
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    assert eraseOverlapIntervals(intervals) == 1
    intervals = [[1,2],[1,2],[1,2]]
    assert eraseOverlapIntervals(intervals) == 2
    intervals = [[1,2],[2,3]]
    assert eraseOverlapIntervals(intervals) == 0
    print("All tests passed!")
