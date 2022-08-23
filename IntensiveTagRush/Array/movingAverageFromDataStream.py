"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
"""
import collections
class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.size = size
        self.total = 0
        self.len = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.len += 1
        self.total += val
        while self.len > self.size:
            self.total -= self.queue.popleft()
            self.len -= 1
        return self.total / self.len
    