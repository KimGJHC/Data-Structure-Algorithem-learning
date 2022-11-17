"""
967. Numbers With Same Consecutive Differences

Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

# use backtrack, be careful about the case when k (difference) is 0
"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(self.getNum(path))
                return

            next_substract = path[-1] - k
            next_add = path[-1] + k
            if next_substract >= 0:
                path.append(next_substract)
                backtrack(path)
                path.pop()

            if next_add <= 9 and next_substract != next_add:
                path.append(next_add)
                backtrack(path)
                path.pop()

        for start in range(1, 10):
            backtrack([start])
        return res

    def getNum(self, path):
        res = path[0]
        for i in range(1, len(path)):
            res *= 10
            res += path[i]
        return res