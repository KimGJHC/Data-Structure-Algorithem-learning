"""
81. Search in Rotated Sorted Array II

Search target in sorted array rotated at an unknown pivot, duplicated elements are possible

# binary search, increase l by 1 if we cannot reduce search space with binary search
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[l]:
                l += 1
                continue
            elif nums[mid] > nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[l] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False