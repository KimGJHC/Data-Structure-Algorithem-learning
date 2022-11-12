"""
2466. Count Ways To Build Good Strings
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

# use top-down dp where dp[i] is the number of good strings with length i
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        MOD = 10 ** 9 + 7

        self.dp = defaultdict(int)

        for length in range(high, low - 1, -1):
            res += self.countStringWithLength(zero, one, length)
        return res % MOD

    def countStringWithLength(self, zero, one, length):
        # return number of ways to get exactly length
        if length not in self.dp:
            # base case
            if length == 0:
                return 1
            elif length < 0:
                return 0
            elif length < zero and length < one:
                return 0
            elif length >= zero and length < one:
                if length % zero == 0:
                    return 1
                else:
                    return 0
            elif length >= one and length < zero:
                if length % one == 0:
                    return 1
                else:
                    return 0

            last_one = self.countStringWithLength(zero, one, length - one)
            last_zero = self.countStringWithLength(zero, one, length - zero)
            self.dp[length] = last_one + last_zero

        return self.dp[length]