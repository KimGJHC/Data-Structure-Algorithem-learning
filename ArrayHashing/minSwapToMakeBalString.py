"""
1963. Minimum Number of Swaps to Make the String Balanced
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.
"""


class Solution:
    def minSwaps(self, s: str) -> int:

        res = 0

        open_brackets = 0

        for bracket in s:
            if bracket == '[':
                open_brackets += 1
            else:
                open_brackets -= 1
                if open_brackets < 0:
                    res += 1
                    open_brackets = 1
        return res

