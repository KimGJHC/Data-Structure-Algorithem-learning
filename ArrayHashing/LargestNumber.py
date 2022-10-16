"""
179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

1. customize sorting order
"""

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = sorted([str(num) for num in nums], key=LargerNumKey)

        return ''.join(res) if res[0] != '0' else '0'