"""
540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            left_eq = nums[mid] == nums[mid - 1] if mid - 1 >= 0 else False
            right_eq = nums[mid] == nums[mid + 1] if mid + 1 < n else False

            if not left_eq and not right_eq:
                return nums[mid]
            else:
                if mid % 2 == 0:
                    if right_eq:
                        l = mid + 2
                    else:
                        r = mid - 2
                else:
                    if right_eq:
                        r = mid - 1
                    else:
                        l = mid + 1