"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

def lengthOfLIS_v1(nums):
    """
    The idea is to consider dp[i] as the len(LIS) in starting at nums[i]
    :param nums:
    :return:
    """
    n = len(nums)
    dp = [1] * n

    for i in range(n-2, -1, -1):
        dp[i] += max([dp[j] for j in range(i+1, n) if nums[j] > nums[i]]+[0])
    return max(dp)
# time: O(n^2)
# space: O(n)

def lengthOfLIS(nums):
    """
    The dp approach is slow, we consider building the subseq
    :param nums:
    :return:
    """
    from bisect import bisect_left
    sub = []
    for num in nums:
        i = bisect_left(sub, num)
        if i == len(sub): # num is greater than all elements in sub
            sub.append(num)
        else:
            sub[i] = num # this is not effective if i < len(sub) - 1, it makes sure if i == len(sub) - 1, it will replace the largest of sub
    return len(sub)

# time: O(nlogn)
# space: O(n)

def test():
    nums = [10,9,2,5,3,7,101,18]
    assert lengthOfLIS(nums) == 4
    nums = [0,1,0,3,2,3]
    assert lengthOfLIS(nums) == 4
    nums = [7,7,7,7,7,7,7]
    assert lengthOfLIS(nums) == 1
    print("All tests passed!")