"""
729. My Calendar I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
"""

import bisect
class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        start_starts = bisect.bisect_right(self.starts, start)
        end_starts = bisect.bisect_left(self.starts, end)
        start_ends = bisect.bisect_right(self.ends, start)

        if len(self.starts) == start_ends:
            self.starts.append(start)
            self.ends.append(end)
            return True
        else:
            if start_starts == end_starts and end_starts == start_ends:
                self.starts = self.starts[:start_starts] + [start] + self.starts[start_starts:]
                self.ends = self.ends[:start_starts] + [end] + self.ends[start_starts:]
                return True
            return False

# solution 1: binary search
# time: O(logn)
# space: O(n)