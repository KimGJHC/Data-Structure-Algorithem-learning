"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

# 2 binary search for left and right bounds, record bound if nums[mid] == target (more intuitive than return l or r index)
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left_bound, right_bound = n, -1

        # find left bound
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target:
                    left_bound = min(left_bound, mid)
                r = mid - 1

        # find right bound
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    right_bound = max(right_bound, mid)
                l = mid + 1
            else:
                r = mid - 1

        return [-1 if left_bound == n else left_bound, right_bound]