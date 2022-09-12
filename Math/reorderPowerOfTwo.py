"""
869. Reordered Power of 2
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
"""

import collections
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))

        all_cand = [collections.Counter(str(1 << b)) for b in range(31)]
        return any([count == cand for cand in all_cand])

# time:O ((logn) ** 2)
# space: O(logn)