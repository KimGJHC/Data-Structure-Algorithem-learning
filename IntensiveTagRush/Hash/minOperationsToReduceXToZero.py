"""
1658. Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
"""
import collections

import collections
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1

        prefix_sum = collections.defaultdict(int)
        left_sum = 0
        for i, num in enumerate(nums):
            left_sum += num
            if left_sum > x:
                break

            prefix_sum[left_sum] = i

        suffix_sum = collections.defaultdict(int)
        right_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            right_sum += num
            if right_sum > x:
                break
            suffix_sum[right_sum] = i

        res = float('inf')
        n = len(nums)
        for ps in prefix_sum:
            need = x - ps
            if need in suffix_sum:
                res = min(res, prefix_sum[ps] + 1 + n - suffix_sum[need])

        if x in prefix_sum:
            res = min(res, prefix_sum[x] + 1)
        if x in suffix_sum:
            res = min(res, n - suffix_sum[x])
        return res if res < float('inf') else -1
# hashmap
# time: O(n)
# space: O(n)

    def minOperations_v2(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        l = 0
        n = len(nums)

        current = 0
        max_lr = -1
        diff = total - x

        for r in range(n):
            current += nums[r]
            while current > diff and l <= r:
                current -= nums[l]
                l += 1
            if current == diff:
                max_lr = max(max_lr, r - l + 1)
        return n - max_lr if max_lr != -1 else -1
# 2 pointers
# space: O(1)
