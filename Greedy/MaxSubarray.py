"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
"""

def MaxSubArray(nums):
    # Note that a sub array with max sum will have start and end element positive
    # We are calculating the max sub array sum with nums[i] as the end of subarray
    res = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        if nums[i] > res:
            res = nums[i]
    return res

def test():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert MaxSubArray(nums) == 6
    nums = [1]
    assert MaxSubArray(nums) == 1
    nums = [5,4,-1,7,8]
    assert MaxSubArray(nums) == 23
    print("All tests passed!")