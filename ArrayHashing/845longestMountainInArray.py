"""
845. Longest Mountain in Array

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

# consider the shape of mountain, use greedy algorithm
"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        res = 0
        i = 0  # begining index of a potential moutain array
        while i < n:
            j = i
            found = 0
            # find next peak
            while j + 1 < n and arr[j] < arr[j + 1]:
                j += 1
            found += j > i
            tmp = j
            # find next bottom
            while j + 1 < n and arr[j] > arr[j + 1]:
                j += 1
            found += j > tmp

            # update i
            if found == 2:
                res = max(res, j - i + 1)
            i = max(j, i + 1)  # in case of j == i, we want to increment i by 1
        return res
