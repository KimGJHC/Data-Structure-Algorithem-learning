"""
372. Super Pow
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
"""

from functools import reduce
class Solution:
    def superPow(self, a: int, b):
        def mod(p):
            # return a**b mod p
            return pow(a, reduce(lambda e, d: (10*e + d) % (p-1), b, 0), p) if a%p else 0
        return (764 * mod(7) + 574 * mod(191)) % 1337