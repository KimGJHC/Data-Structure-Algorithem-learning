"""
523. Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""


class Solution:
    def checkSubarraySum(self, nums, k):
        track = []

        for num in nums:
            for i in range(len(track)):
                if (track[i] + num) % k == 0:
                    return True
                else:
                    track[i] += num
            track.append(num)

        return False
# time: O(n**2), too slow

# idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k

    def checkSubarraySum_v2(self, nums, k):
        ht = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            total %= k

            if total not in ht:
                ht[total] = i
            else:
                if i - ht[total] >= 2:
                    return True
        return False

# time: O(n)
# space: O(k)