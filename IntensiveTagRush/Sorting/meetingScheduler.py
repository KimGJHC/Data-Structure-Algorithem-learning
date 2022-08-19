"""
1229. Meeting Scheduler
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
"""

import heapq
class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        timestamps = []
        for start, end in slots1:
            timestamps.append((start, 1))
            timestamps.append((end, -1))
        for start, end in slots2:
            timestamps.append((start, 1))
            timestamps.append((end, -1))
        heapq.heapify(timestamps)

        previous, available = heapq.heappop(timestamps)

        while timestamps:
            current = heapq.heappop(timestamps)
            if available == 2 and current[0] - previous >= duration:
                return [previous, previous + duration]
            available += current[1]
            previous = current[0]
        return []
# solution 1: timestamp + heapq
# time: O(nlogn) in the worst case
# space: O(n + m) where n = len(slots1) and m = len(slots2)

    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()
        pointer1 = pointer2 = 0

        while pointer1 < len(slots1) and pointer2 < len(slots2):
            # find the boundaries of the intersection, or the common slot
            intersect_right = min(slots1[pointer1][1], slots2[pointer2][1])
            intersect_left = max(slots1[pointer1][0], slots2[pointer2][0])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            # always move the one that ends earlier
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return []
# solution 2: two pointers
# space: O(1)