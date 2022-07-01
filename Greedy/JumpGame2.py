"""
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Input: nums = [2,3,1,1,4]
Output: 2

Input: nums = [2,3,0,1,4]
Output: 2
"""

def jump(nums):
    # We are going to push the limit
    n = len(nums)

    start, end = 0, n - 1
    limit = 0
    step = 0
    while limit < end:
        step += 1
        # update limit of current step
        old_limit = limit
        limit = max([i + nums[i] for i in range(start, limit + 1)])
        start = old_limit + 1
    return step

# time: O(n)
# space: O(1)

def test():
    nums = [2, 3, 1, 1, 4]
    assert jump(nums) == 2
    nums = [2,3,0,1,4]
    assert jump(nums) == 2
    print("All tests passed!")



