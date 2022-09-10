"""
1155. Number of Dice Rolls With Target Sum
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
"""

class Solution:
    def __init__(self):
        self.memo = {}
        self.MOD = 10 ** 9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            if target > k or target < 1:
                return 0
            else:
                return 1
        else:
            sol = (n, target)
            if sol not in self.memo:
                total = 0
                for i in range(1, k + 1):
                    total += self.numRollsToTarget(n - 1, k, target - i)
                self.memo[sol] = total
            return self.memo[sol] % self.MOD