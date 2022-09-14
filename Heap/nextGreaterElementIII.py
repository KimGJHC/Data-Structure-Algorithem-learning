"""
556. Next Greater Element III
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
"""

import heapq
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        num = [int(i) for i in num]
        length = len(num)
        if length < 2:
            return -1

        heap = [(-num[length - 1], length - 1)]

        for i in range(length - 2, -1, -1):
            if num[i] < -heap[0][0]:
                while heap and num[i] < -heap[0][0]:
                    idx = heapq.heappop(heap)[1]

                num[i], num[idx] = num[idx], num[i]
                num[i + 1:] = sorted(num[i + 1:])
                num = [str(i) for i in num]
                res = int(''.join(num))
                return res if res <= (1 << 31) - 1 else -1
            else:
                heapq.heappush(heap, (-num[i], i))
        return -1
# time: O(logn)
# space: O(logn)