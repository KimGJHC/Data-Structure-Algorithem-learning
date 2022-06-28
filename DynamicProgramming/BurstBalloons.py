"""
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Input: nums = [3,1,5,8]
Output: 167

Input: nums = [1,5]
Output: 10
"""

def maxCoins_v1(nums):
    # we first create a recursive solution that is less efficient
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        res = max([nums[i] * (nums[i-1] if i > 0 else 1) * (nums[i+1] if i < n-1 else 1) + maxCoins(nums[:i] + nums[i+1:]) for i in range(n)])
        return res
# time: O(n!)

# lets add a memory to make it top-bottom dp

from functools import lru_cache

def maxCoins(nums):
    # we first create a recursive solution that is less efficient
    # we could use bitmask to store information
    # also we can use lru_cache
    # special case
    if len(nums) > 1 and len(set(nums)) == 1:
        return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

    # handle edge case
    nums = [1] + nums + [1]

    @lru_cache(None)  # memoization
    def dp(left, right):
        # maximum if we burst all nums[left]...nums[right], inclusive
        if right - left < 0:
            return 0
        result = 0
        # find the last burst one in nums[left]...nums[right]
        for i in range(left, right + 1):
            # nums[i] is the last burst one
            gain = nums[left - 1] * nums[i] * nums[right + 1]
            # nums[i] is fixed, recursively call left side and right side
            remaining = dp(left, i - 1) + dp(i + 1, right)
            # update the result
            result = max(result, remaining + gain)
        return result

    # we can not burst the first one and the last one
    # since they are both fake balloons added by ourselves
    return dp(1, len(nums) - 2)

def test():
    nums = [3, 1, 5, 8]
    assert maxCoins(nums) == 167
    nums = [1, 5]
    assert maxCoins(nums) == 10
    print("All tests passed!")