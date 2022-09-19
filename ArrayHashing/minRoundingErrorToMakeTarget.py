"""
1058. Minimize Rounding Error to Meet Target
Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string "-1" if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.
"""

import math
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        prices = [float(price) for price in prices]

        non_integer_prices = []

        for price in prices:
            if price == int(price):
                target -= price
                continue
            else:
                non_integer_prices.append(price)

        # calculate error
        ceil_sum = sum([math.ceil(price) for price in non_integer_prices])
        floor_sum = sum([math.floor(price) for price in non_integer_prices])

        if target < floor_sum or target > ceil_sum:
            return '-1'

        ceil_needed = int(target - floor_sum)
        ceil_error = [math.ceil(price) - price for price in non_integer_prices]
        ceil_error.sort()

        res = sum(ceil_error[:ceil_needed]) + sum([1 - error for error in ceil_error[ceil_needed:]])
        return '{:.3f}'.format(res)
# time: O(nlogn)
# space: O(n)

