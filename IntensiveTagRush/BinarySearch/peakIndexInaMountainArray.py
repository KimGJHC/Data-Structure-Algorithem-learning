"""
852. Peak Index in a Mountain Array
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            l_small = arr[mid] > arr[mid - 1] if mid > 0 else True
            r_small = arr[mid] > arr[mid + 1] if mid < n - 1 else True

            if l_small and r_small:
                return mid
            elif l_small:
                l = mid + 1
            else:
                r = mid - 1
# time: O(logn)
# space: O(1)