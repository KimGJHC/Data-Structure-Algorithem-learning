"""
1680. Concatenation of Consecutive Binary Numbers
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

# basic bit manipulation
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        MOD = 10 ** 9 + 7

        res = 1
        for num in range(2, n + 1):
            bit_size = len(bin(num)) - 2
            res <<= bit_size
            res += num
            res %= MOD

        return res