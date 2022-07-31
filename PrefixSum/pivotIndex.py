"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""



def pivotIndex(nums):
    n = len(nums)
    res = [0] * n

    left_sum = 0
    for i in range(n - 1, -1, -1):
        res[i] = left_sum
        left_sum += nums[i]

    right_sum = 0
    for i in range(n):
        if right_sum == res[i]:
            return i
        right_sum += nums[i]
    return -1

# tims: O(n)
# space: O(n)

def pivotIndex_v2(self, nums):
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == (total - left_sum - num):
            return i
        left_sum += num
    return -1

# time: O(n)
# space: O(1)