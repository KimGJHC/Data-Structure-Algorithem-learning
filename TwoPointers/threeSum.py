"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
# time: O(n ** 2)
# space: O(1)

# without sorting
    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = set()
        comp = {}

        for i, val1 in enumerate(nums):
            if val1 not in visited:
                visited.add(val1)

                for val2 in nums[i + 1:]:
                    compliment = 0 - val1 - val2
                    if compliment in comp and comp[compliment] == i:
                        res.add(tuple(sorted([val1, compliment, val2])))
                    comp[val2] = i
        return [list(triplet) for triplet in res]

