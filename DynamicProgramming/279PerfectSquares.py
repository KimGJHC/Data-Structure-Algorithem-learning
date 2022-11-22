"""
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# typical dp question, but TLE, possible reason could be too many possible squares comparing to counts
# we restrict counts instead in v2
"""


class Solution:

    def numSquares_v1(self, n: int) -> int:
        squares = [i ** 2 for i in range(math.floor(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)  # dp[i+1] = numSquares(i)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

    def numSquares_v2(self, n: int) -> int:
        squares = set([i ** 2 for i in range(1, math.floor(math.sqrt(n)) + 1)])

        def divisible(n, count):
            # return true if n can be decomposed to 'count' number of square

            if count == 1:
                return n in squares

            for k in squares:
                if divisible(n - k, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count