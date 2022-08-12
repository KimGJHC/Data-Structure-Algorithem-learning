"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums):

        def getMajorElement(left, right):
            if right - left == 1:
                return nums[left]

            mid = (left + right) // 2
            left_major = getMajorElement(left, mid)
            right_major = getMajorElement(mid, right)

            if left_major == right_major:
                return left_major

            left_count = 0
            right_count = 0

            for i in range(left, right):
                if nums[i] == left_major:
                    left_count += 1
                elif nums[i] == right_major:
                    right_count += 1

            return left_major if left_count > right_count else right_major

        return getMajorElement(0, len(nums))

# solution 1: typical divide and conquer
# time: O(nlogn)
# space: O(logn) from recursive stack

# solution 2: sort and middle element; (quicksort might be useful)