"""
930. Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""

import collections
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        window_sum = 0
        queue = collections.deque()
        res = 0
        n = len(nums)

        if goal == 0:
            zeros = []
            zero_block = 0
            for num in nums:
                if num == 1 and zero_block > 0:
                    zeros.append(zero_block)
                    zero_block = 0
                elif num == 0:
                    zero_block += 1
            if zero_block > 0:
                zeros.append(zero_block)

            for number in zeros:
                res += ((1 + number) * number) // 2
            return res
        else:
            i = 0
            while i < n:
                num = nums[i]
                window_sum += num
                queue.append(num)

                if window_sum == goal:
                    left = 1
                    right = 1

                    while queue and queue[0] != 1:
                        queue.popleft()
                        left += 1
                    window_sum -= queue.popleft()

                    while i + 1 < n and nums[i + 1] != 1:
                        i += 1
                        queue.append(nums[i])
                        right += 1
                    res += left * right
                i += 1
        return res
# time: O(n)
# space: O(n)

    def numSubarraysWithSum(self, nums, goal):
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        count = collections.Counter()

        res = 0
        for x in P:
            res += count[x]
            count[x + goal] += 1
        return res

# prefix sum
# time: O(n)
# space: O(n)