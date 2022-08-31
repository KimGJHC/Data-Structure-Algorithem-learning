"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bit = 0
        res = []

        for num in nums:
            position = num - 1
            # check if the bit position is 1
            if bit & (1 << position) != 0:
                res.append(num)
            else:
                bit |= 1 << position
        return res

# solution 1: bit mask
# time: O(n)
# space: O(1)
    def findDuplicates_v2(self, nums: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):
            num = nums[i]
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] *= -1
        return res
# solution 2: +-1 for state + index info