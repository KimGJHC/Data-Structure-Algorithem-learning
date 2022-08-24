"""
1146. Snapshot Array
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

import bisect
class SnapshotArray:

    def __init__(self, length): # space O(length + n)
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val): # time O(1)
        self.arr[index].append([self.snap_id, val])

    def snap(self): # time: O(1)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id): # time O(logn)
        i = bisect.bisect(self.arr[index], [snap_id + 1]) - 1
        return self.arr[index][i][1]

