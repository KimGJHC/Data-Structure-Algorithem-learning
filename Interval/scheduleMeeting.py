"""
Lintcode # 920

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        n = len(intervals)
        if n <= 1:
            return True

        intervals.sort(key = lambda x: x.start)
        for i in range(1, n):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

# time: O(nlogn)
# space: O(1)