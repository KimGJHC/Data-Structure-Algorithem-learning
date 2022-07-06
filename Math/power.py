"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
"""

def myPow(x, n):
    if n < 0:
        x = 1 / x
        n *= -1
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

def test():
    x = 2.00000
    n = 10
    assert myPow(x, n) == 1024
    x = 2.10000
    n = 3
    assert myPow(x, n) == 2.1**3
    x = 2
    n = -2
    assert myPow(x, n) == 2**(-2)
    print("All tests passed!")

