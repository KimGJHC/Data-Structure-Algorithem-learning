"""
1968. Array With Elements Not Equal to Average of Neighbors
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.

# zig-zag order fits the requirements
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # create a zig-zag order array
        sign = 1  # 1: <, -1: >

        for i in range(len(nums) - 1):
            if sign == 1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            sign *= -1
        return nums