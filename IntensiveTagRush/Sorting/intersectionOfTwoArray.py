"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

class Solution:
    def intersection(self, nums1, nums2):
        nums1, nums2 = list(set(nums1)), list(set(nums2))
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        res = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res