"""
1825. Finding MK Average
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.

# We need to efficiently calculate the range sum and update it based on order of stream
# use sorted list or Fenwick tree
"""

from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.sorted_list = SortedList()
        self.total = 0
        self.small_k = 0
        self.large_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.queue.append(num)

        idx = bisect_left(self.sorted_list, num)
        if idx < self.k:
            self.small_k += num
            if len(self.sorted_list) >= self.k:
                self.small_k -= self.sorted_list[self.k - 1]

        if idx >= len(self.sorted_list) - self.k + 1:
            self.large_k += num
            if len(self.sorted_list) >= self.k:
                self.large_k -= self.sorted_list[-self.k]

        self.sorted_list.add(num)

        if len(self.queue) > self.m:
            num = self.queue.popleft()
            self.total -= num
            idx = self.sorted_list.index(num)
            if idx < self.k:
                self.small_k -= num
                self.small_k += self.sorted_list[self.k]
            elif idx >= len(self.sorted_list) - self.k:
                self.large_k -= num
                self.large_k += self.sorted_list[-self.k - 1]
            self.sorted_list.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sorted_list) < self.m:
            return -1
        return int((self.total - self.large_k - self.small_k) / (self.m - 2 * self.k))