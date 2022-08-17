"""
759. Employee Free Time

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
"""


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

from functools import reduce


class Solution:
    def employeeFreeTime(self, schedule):
        schedule = reduce(lambda x, y: x + y, schedule)
        schedule.sort(key=lambda x: x.start)
        res = []

        pre_end = schedule[0].end

        for i in range(1, len(schedule)):
            current_start, current_end = schedule[i].start, schedule[i].end
            if current_start <= pre_end and current_end > pre_end:
                pre_end = current_end
            elif current_start > pre_end:
                res.append(Interval(pre_end, current_start))
                pre_end = current_end

        return res

# solution: sort by interval start and keep track the current consecutive interval
# time: O(nlogn)
# space: O(n) for timSort