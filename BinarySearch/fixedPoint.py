"""
1064. Fixed Point
Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.
"""


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] > mid:
                r = mid - 1
            elif arr[mid] < mid:
                l = mid + 1
            else:
                r = mid - 1
                res = mid

        return res