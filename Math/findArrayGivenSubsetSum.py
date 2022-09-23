"""
1982. Find Array Given Subset Sums
You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).

Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at least one correct answer.
"""

import collections
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        res = []
        inclusive = []
        exclusive = []

        sums.sort()
        numberCount = collections.Counter(sums)

        while len(res) < n:
            if len(sums) == 2:
                sums.remove(0)
                res.append(sums[0])
                break

            # candidate of number
            diff = sums[-1] - sums[-2]

            for subsum in sums:
                if numberCount[subsum] > 0:
                    exclusive.append(subsum)
                    inclusive.append(subsum + diff)
                    numberCount[subsum] -= 1
                    numberCount[subsum + diff] -= 1

            if 0 not in exclusive:
                exclusive = inclusive
                diff *= -1

            res.append(diff)
            sums = sorted(exclusive)
            numberCount = collections.Counter(sums)
            inclusive = []
            exclusive = []

        return res
# time: O(slogs**2)
# space: O(s)
