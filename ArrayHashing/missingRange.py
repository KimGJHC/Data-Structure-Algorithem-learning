"""
163. Missing Ranges
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []

        lower -= 1
        upper += 1
        # not inclusive
        nums.append(upper)

        for num in nums:
            diff = num - lower
            if diff <= 1:
                pass
            elif diff == 2:
                res.append(str(lower + 1))
            else:
                res.append(str(lower + 1) + '->' + str(num - 1))
            lower = num

        return res