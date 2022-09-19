"""
1558. Minimum Numbers of Function Calls to Make Target Array
You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:


You want to use the modify function to covert arr to nums using the minimum number of calls.

Return the minimum number of function calls to make nums from arr.

The test cases are generated so that the answer fits in a 32-bit signed integer.
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        res = 0
        maxLen = 1

        for num in nums:
            bits = 0
            while num > 0:
                res += num & 1
                bits += 1
                num >>= 1
            maxLen = max(maxLen, bits)
        return res + maxLen - 1
