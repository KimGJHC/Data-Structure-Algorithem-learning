"""
991. Broken Calculator
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
"""

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        res = 0
        while target > startValue:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
            res += 1
        return res + startValue - target

# solution 1: odd target can be only reach by -1
# time: O(log target)
# space: O(1)