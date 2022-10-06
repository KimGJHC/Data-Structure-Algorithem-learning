"""
2222. Number of Ways to Select Buildings
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.
"""

class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        left_ones = sum([char == '1' for char in s])
        left_zeros = sum([char == '0' for char in s])

        res = 0
        right_ones = 0
        right_zeros = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                left_zeros -= 1
                right_zeros += 1
                res += left_ones * right_ones
            else:
                left_ones -= 1
                right_ones += 1
                res += left_zeros * right_zeros
        return res

