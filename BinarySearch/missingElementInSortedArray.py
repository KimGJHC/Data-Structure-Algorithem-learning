"""
1060. Missing Element in Sorted Array
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.
"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        # find the largest num in nums less than k missing elements

        while l <= r:
            mid = (l + r) // 2

            missing = nums[mid] - nums[0] - mid
            if missing <= k - 1:
                l = mid + 1
            else:
                r = mid - 1
        missing_r = nums[r] - nums[0] - r
        return nums[r] + k - missing_r