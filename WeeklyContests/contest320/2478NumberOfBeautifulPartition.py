"""
2478. Number of Beautiful Partitions
You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.

# typical DP problem with states i and k, dp(i, k) is number of valid k-partitions in s[i:]
# used top-down dp but TLE, need to practice for bottom-up dp
"""


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = "2357"
        if s[-1] in primes:
            return 0
        if s[0] not in primes:
            return 0
        n = len(s)
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, k):
            # return number of valid partition in s[i:] with k partition
            if k == 0 and i == n:
                return 1
            if k == 0:
                return 0
            if n - i < minLength or n - i < 2 * k:
                return 0
            if s[i] not in primes:
                return 0

            total = 0
            for j in range(i + minLength - 1, n):
                if s[j] not in primes:
                    total += dp(j + 1, k - 1)
            return total

        res = dp(0, k)
        return res % MOD