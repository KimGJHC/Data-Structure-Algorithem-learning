"""
2104. Sum of Subarray Ranges

You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3]
Output: 4

Input: nums = [1,3,3]
Output: 4
"""
from operator import lt, gt
def subArrayRanges(nums):
    # the idea is the record the min and max of each subarray and compute the difference between their respective sum
    def find(operation):
        res = 0
        stack = []
        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or operation(nums[stack[-1]], nums[i])):
                mid = stack.pop()
                ii = stack[-1] if stack else -1
                # number of subarrays with nums[i] as the min/max
                res += nums[mid] * (i-mid) * (mid-ii)
            stack.append(i)
        return res
    return find(lt) - find(gt)

# time: O(n)
# space: O(n)

def test():
    nums = [1, 2, 3]
    assert subArrayRanges(nums) == 4
    nums = [1,3,3]
    assert subArrayRanges(nums) == 4
    print("All tests passed!")


