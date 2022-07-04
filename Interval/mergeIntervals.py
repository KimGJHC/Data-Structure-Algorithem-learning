"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
"""

from collections import deque
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    intervals = deque(intervals)
    res = []
    current = intervals.popleft()

    while intervals:
        next = intervals.popleft()
        if next[0] > current[1]:
            res.append(current)
            current = next
        else:
            current[1] = max(current[1], next[1])
    res.append(current)
    return res

# time: O(nlog(n))
# space: O(n)

def test():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert mergeIntervals(intervals) == [[1,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    assert mergeIntervals(intervals) == [[1,5]]
    print("All tests passed!")
