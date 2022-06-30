"""
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false
"""

def canJump(nums):
    # This is the greedy algorithm
    # The key for greedy algorithm is that we can eliminate in one time. We are keeping pushing the limit
    if len(nums) == 1:
        return True
    start, end = 0, len(nums)-1
    limit = 0 # the furthest we can reach after visiting a cell
    while start <= limit and limit <= end:
        limit = max(limit, start+nums[start])
        start += 1
    return limit >= end

# time: O(n)
# space: O(1)

def test():
    nums = [2, 3, 1, 1, 4]
    assert canJump(nums) == True
    nums = [3,2,1,0,4]
    assert canJump(nums) == False
    print("All tests passed!")
