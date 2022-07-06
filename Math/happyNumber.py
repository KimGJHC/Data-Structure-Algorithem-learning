"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true

Input: n = 2
Output: false
"""

def isHappy(n):
    ht = set()

    def getSquareDigitSum(n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res

    while n != 1:
        ht.add(n)
        n = getSquareDigitSum(n)
        if n in ht:
            return False
    return True

# time: O(logn)
# space: O(logn)

def test():
    assert isHappy(19) == True
    assert isHappy(2) == False
    print("All tests passed!")
