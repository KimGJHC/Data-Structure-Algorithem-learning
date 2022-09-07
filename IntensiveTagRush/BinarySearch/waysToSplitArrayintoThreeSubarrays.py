"""
1712. Ways to Split Array Into Three Subarrays
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.
"""


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] + nums[i - 1]

        first_break = 0
        total = nums[-1]
        res = 0

        while nums[first_break] <= total / 3 and first_break < n - 2:

            # search right most position
            l, r = first_break + 1, n - 1
            target = (total - nums[first_break]) / 2

            while l < r:
                mid = (l + r) // 2
                if nums[mid] - nums[first_break] <= target:
                    l = mid + 1
                else:
                    r = mid
            res += l - first_break

            # search left most position
            l, r = first_break + 1, n - 1
            target = nums[first_break]

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] - nums[first_break] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            res -= l - first_break

            first_break += 1

        MOD = 10 ** 9 + 7
        return res % MOD
# time: O(nlogn)
# space: O(1)

