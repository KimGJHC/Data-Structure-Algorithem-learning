"""
1663. Smallest String With A Given Numeric Value
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
"""

import string
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        letters = list(string.ascii_lowercase)

        res = []

        while k > n and n > 0:
            if k - 26 < n:
                idx = k - n
                res.append(letters[idx])
                n -= 1
                break
            else:
                idx = 25
                res.append(letters[idx])
                n -= 1
                k -= 26

        while n > 0:
            res.append('a')
            n -= 1

        return ''.join(res[::-1])
# time: O(n)
# space: O(n)