"""
528. Random Pick with Weight
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
"""


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] = self.w[i - 1] + self.w[i]
        self.maxx = self.w[-1]

    def pickIndex(self) -> int:
        target = self.maxx * random.random()
        l, r = 0, len(self.w)

        while l < r:
            mid = (l + r) // 2
            if self.w[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l
# solution: prefix sum + binary search
# time: O(n) for constructor, O(logn) for pickIndex
# space: O(n)