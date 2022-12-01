"""
281. Zigzag Iterator
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.

# Simply use two pointers for two vectors
"""


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.idx1 = 0
        self.idx2 = 0
        self.n1 = len(v1)
        self.n2 = len(v2)

    def next(self) -> int:
        if self.hasNextv1() and (not self.hasNextv2() or self.idx1 == self.idx2):
            self.idx1 += 1
            return self.v1[self.idx1 - 1]
        else:
            self.idx2 += 1
            return self.v2[self.idx2 - 1]

    def hasNext(self) -> bool:
        return self.hasNextv1() or self.hasNextv2()

    def hasNextv1(self):
        return self.idx1 < self.n1

    def hasNextv2(self):
        return self.idx2 < self.n2