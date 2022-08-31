"""
496. Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}

        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()
            if not stack:
                next_greater[num] = -1
            else:
                next_greater[num] = stack[-1]
            stack.append(num)

        res = []
        for num in nums1:
            res.append(next_greater[num])
        return res
# time: O(n) where n = len(nums2)
# space: O(n)