"""
2198. Number of Single Divisor Triplets
You are given a 0-indexed array of positive integers nums. A triplet of three distinct indices (i, j, k) is called a single divisor triplet of nums if nums[i] + nums[j] + nums[k] is divisible by exactly one of nums[i], nums[j], or nums[k].

Return the number of single divisor triplets of nums.

# The key in this kind of question is not duplicate counting. For this reason, we need to fix certain value inorder to distinguish between different triplets
"""


class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:

        def divisible(a, b):
            return a % b == 0

        def validTriplet(a, b, c):
            total = a + b + c
            return divisible(total, a) + divisible(total, b) + divisible(total, c) == 1

        def nC2(n):
            return n * (n - 1) // 2

        count = Counter(nums)
        keys = list(count.keys())
        n = len(keys)

        res = 0
        for i in range(n):
            # take 2 keys[i]
            if count[keys[i]] >= 2:
                for j in range(i + 1, n):
                    if validTriplet(keys[i], keys[i], keys[j]):
                        res += nC2(count[keys[i]]) * count[keys[j]]
            for j in range(i + 1, n):
                if count[keys[j]] >= 2:
                    if validTriplet(keys[i], keys[j], keys[j]):
                        res += nC2(count[keys[j]]) * count[keys[i]]
                for k in range(j + 1, n):
                    if validTriplet(keys[i], keys[j], keys[k]):
                        res += count[keys[i]] * count[keys[j]] * count[keys[k]]
        return res * 6