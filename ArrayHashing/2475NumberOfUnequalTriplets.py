"""
2475. Number of Unequal Triplets in Array

You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.

# we should notice that the order of number does not affect the results
# thus we can think of it as bunch of chucks of the same number
# to avoid duplicate counts, we fix the middle value when we are adding count
"""

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = Counter(nums)
        l, r = 0, len(nums)
        res = 0
        for num in count:
            r -= count[num]
            res += l * count[num] * r
            l += count[num]
        return res