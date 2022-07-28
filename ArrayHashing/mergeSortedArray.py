"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1, m: int, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1.copy()

        p1, p2, p3 = 0, 0, 0

        while p3 < m + n:
            if p2 >= n or (p1 < m and nums1Copy[p1] <= nums2[p2]):
                nums1[p3] = nums1Copy[p1]
                p1 += 1
            else:
                nums1[p3] = nums2[p2]
                p2 += 1
            p3 += 1