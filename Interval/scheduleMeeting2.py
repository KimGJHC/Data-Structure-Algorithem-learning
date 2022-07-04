"""
Lintcode # 919

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def min_meeting_rooms(intervals):
    # The idea is to find the max number of interval intersections in a point of time
    # think about the starts and ends on a single timeline
    start = sorted([interval.start for interval in intervals])
    end = sorted([interval.end for interval in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)

    return res
