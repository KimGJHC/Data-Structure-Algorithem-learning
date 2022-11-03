"""
16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

# sorting + fix first element and 2 pointers for other 2 elements
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == target:
                    return target
                else:
                    if abs(target - threeSum) < abs(diff):
                        diff = target - threeSum

                    if target > threeSum:
                        l += 1
                    else:
                        r -= 1
        return target - diff