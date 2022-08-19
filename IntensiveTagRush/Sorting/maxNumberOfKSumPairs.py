"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

import collections
class Solution:
    def maxOperations(self, nums, k):
        need = collections.defaultdict(int)
        count = 0
        for num in nums:
            if need[num] > 0:
                count += 1
                need[num] -= 1
            else:
                need[k - num] += 1
        return count

# solution: hashmap + 1 pass
# time: O(n)
# space: O(n)
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums)-1

        res = 0
        while l < r:
            current_cum = nums[l] + nums[r]
            if current_cum > k:
                r -= 1
            elif current_cum < k:
                l += 1
            else:
                res += 1
                r -= 1
                l += 1
        return res
# solution: sorting + 2 pointers
# time: O(nlogn)
# space: O(1)