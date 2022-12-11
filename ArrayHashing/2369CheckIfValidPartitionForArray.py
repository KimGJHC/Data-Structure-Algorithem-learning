"""
2369. Check if There is a Valid Partition For The Array

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

# use backtrack/DP
"""


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def backtrack(i):
            # return True if there is a valid partion for nums[i:]
            # base case
            if i == n:
                return True
            elif i == n - 1:
                return False
            elif i == n - 2:
                return nums[i] == nums[i + 1]
            elif i == n - 3:
                return nums[i] == nums[i + 1] == nums[i + 2] or nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i] == 1
            else:
                if nums[i] == nums[i + 1]:
                    if backtrack(i + 2):
                        return True
                if nums[i] == nums[i + 1] == nums[i + 2] or nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i] == 1:
                    if backtrack(i + 3):
                        return True
            return False

        return backtrack(0)