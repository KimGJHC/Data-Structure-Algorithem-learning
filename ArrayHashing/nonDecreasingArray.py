"""
665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# consider which element to change when the decrease comes
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = 0

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                if changed == 1:
                    return False
                else:
                    if i < 1 or nums[i - 1] <= nums[i + 1]:
                        pass
                    else:
                        nums[i + 1] = nums[i]
                    changed += 1

        return True