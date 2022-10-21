"""
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Using monotonically increasing stack, keep track of number of poped elements
corner cases:
1. "1011" k=1, convert "011" to "11"
2. "1" k=1, remove all digits
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        increasing_stack = []
        pops = 0

        for digit in num:
            while increasing_stack and increasing_stack[-1] > digit and pops < k:
                increasing_stack.pop()
                pops += 1
            increasing_stack.append(digit)

        while pops < k:
            increasing_stack.pop()
            pops += 1

        return str(int(''.join(increasing_stack)))