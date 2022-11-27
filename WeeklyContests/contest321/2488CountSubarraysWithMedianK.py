"""
2488. Count Subarrays With Median K
You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

Return the number of non-empty subarrays in nums that have a median equal to k.

Note:

The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
A subarray is a contiguous part of an array.


# Consider the window centered at k and the number of vals larger or equal to k and smaller than k
# The following solution v1 is simple but TLE
"""


class Solution:
    def countSubarrays_v1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i, num in enumerate(nums):
            if num == k:
                left_part = Counter()
                right_part = Counter()

                l = i - 1
                left_k_small = 0
                while l >= 0:
                    left_k_small += 1 if nums[l] < k else -1
                    left_part[left_k_small] += 1
                    l -= 1

                r = i + 1
                right_k_small = 0
                while r < n:
                    right_k_small += 1 if nums[r] < k else -1
                    right_part[right_k_small] += 1
                    r += 1

                left_part[0] += 1
                right_part[0] += 1

                for left in left_part:
                    for right in right_part:
                        if left + right == 0 or left + right == -1:
                            res += left_part[left] * right_part[right]
                return res

    def countSubarrays_v2(self, nums: List[int], k: int) -> int:
        count = Counter([0])
        res = 0
        number_k_small = 0
        found = False

        for num in nums:
            if num < k:
                number_k_small += 1
            elif num > k:
                number_k_small -= 1
            else:
                found = True

            # we want number of vals > k  - number of vals < k = 0 or 1
            # count uses the idea of prefix count to record difference of # of larger and smaller values of k
            if found:
                res += count[number_k_small] + count[number_k_small + 1]
            else:
                count[number_k_small] += 1
        return res
