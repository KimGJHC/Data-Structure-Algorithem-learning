"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6

Input: nums = [-2,0,-1]
Output: 0
"""
def maxProduct(nums):
    """
    The idea is to keep track of the max and min of
    1. current value (last num is 0)
    2. maximum * current (previous 0 to current-1 is positive)
    3. minimum * current (previous 0 to current-1 is negative)
    Note that we keep track of minimum because we want to flip it to maximum if current is negative
    """

    maximum = nums[0]
    minimum = nums[0]
    res = maximum

    for current in nums[1:]:
        temp_maximum = max(current, maximum * current, minimum * current)
        minimum = min(current, maximum * current, minimum * current)
        maximum = temp_maximum
        res = max(res, maximum)
    return res



def test():
    input = [2,3,-2,4]
    output = 6
    assert maxProduct(input) == output
    input = [-2,0,-1]
    output = 0
    assert maxProduct(input) == output
    print("All tests passed")