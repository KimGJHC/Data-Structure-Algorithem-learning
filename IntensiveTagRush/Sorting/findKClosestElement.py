"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""

from collections import deque
class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        if n <= k:
            return arr
        res = deque(arr[:k])

        i = k
        while i < n:
            num = arr[i]
            if abs(x - num) <= abs(x - res[0]):
                res.popleft()
                res.append(num)
            else:
                break
            i += 1
        # the above is going to work for duplicates value, we need to slide back because of duplicates

        i = i - k - 1
        while i >= 0:
            num = arr[i]
            if abs(x - num) <= abs(x - res[-1]):
                res.pop()
                res.appendleft(num)
            else:
                break
            i -= 1

        return list(res)

# time: O(n)
# space: O(k)
