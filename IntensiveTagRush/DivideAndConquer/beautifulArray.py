"""
932. Beautiful Array

An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.
"""

class Solution:
    def beautifulArray(self, n):
        memo = {1:[1]}
        def helper(n):
            if n not in memo:
                if n % 2 == 0:
                    even = helper(n//2)
                    memo[n] = [2*x-1 for x in even] + [2*x for x in even]
                else:
                    odd = helper(n//2+1)
                    even = helper(n//2)
                    memo[n] = [2*x-1 for x in odd] + [2*x for x in even]
            return memo[n]
        return helper(n)

# time: O(nlogn)
# O(nlogn)