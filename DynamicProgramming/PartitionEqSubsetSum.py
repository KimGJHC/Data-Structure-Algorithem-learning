"""
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Input: nums = [1,5,11,5]
Output: true

Input: nums = [1,2,3,5]
Output: false
"""
def canPartition_v1(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    else:
        target = total // 2
    # Now the question become find a set in nums that sum up to target
    def sumToTarget(nums, target):
        if target < 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        # include last of nums or not
        includeLoN = sumToTarget(nums[:-1], target - nums[-1])
        notIncludeLoN = sumToTarget(nums[:-1], target)
        return includeLoN or notIncludeLoN
    return sumToTarget(nums, target)
# This does work but it is too slow
# time: O(n^3)

def canPartition_v2(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    else:
        target = total // 2
    cache = {} # stores (idx, target): res
    # Now the question become find a set in nums that sum up to target
    def sumToTarget(end, target):
        if target < 0:
            return False
        if end == 1:
            if nums[end-1] == target:
                return True
            else:
                return False
        if (end, target) in cache:
            return cache[(end, target)]
        # include last of nums or not
        includeLoN = sumToTarget(end-1, target - nums[end-1])
        notIncludeLoN = sumToTarget(end-1, target)
        cache[(end, target)] = includeLoN or notIncludeLoN
        return includeLoN or notIncludeLoN
    return sumToTarget(len(nums), target)
# This consumes too much memory
# space: O(target*n)

def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    else:
        target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]
    return dp[target]

# time: O(target*n)
# space: O(target)

def test():
    nums = [1,5,11,5]
    assert canPartition(nums) == True
    nums = [1,2,3,5]
    assert canPartition(nums) == False
    print("All tests passed!")