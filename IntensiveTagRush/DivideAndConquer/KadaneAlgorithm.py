"""
For a given array A, Kadane's algorithm can be used to find the maximum sum of the subarrays of A
"""

# this is a dp question
# where dp[j] means the largest sum of subarray ending at nums[j]

def kadane(nums):
    res = current = 0
    for num in nums:
        current = num + max(current, 0)
        res = max(res, current)
    return res