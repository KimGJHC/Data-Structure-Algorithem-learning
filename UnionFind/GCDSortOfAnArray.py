"""
1998. GCD Sort of an Array
You are given an integer array nums, and you can perform the following operation any number of times on nums:

Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.
"""


class Solution:
    def gcdSort(self, nums):

        UF = {}

        def find(x):
            if x not in UF:
                UF[x] = x
            while x != UF[x]:
                UF[x] = UF[UF[x]]
                x = UF[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            UF[x] = y

        for x in nums:
            p = 2
            y = x
            while y not in UF and p * p <= y:
                if y % p == 0:
                    union(x, p)
                    while y % p == 0:
                        y //= p
                p += 1
            if y != 1:
                union(x, y)

        return all(find(x) == find(y) for x, y in zip(sorted(nums), nums))

# time: O(n sqrt(max(nums))) where n = len(nums)
# space: O(max(nums))