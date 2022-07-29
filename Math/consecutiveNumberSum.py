"""
829. Consecutive Numbers Sum

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

"""
def consecutiveNumbersSum_v1(n):
    m = 2
    summation_to_m = 3
    res = 1

    while summation_to_m <= n:
        if (n - summation_to_m) % m == 0:
            res += 1
        m += 1
        summation_to_m += m
    return res

# time: O(n)
# space: O(1)

from math import ceil
def consecutiveNumbersSum(n):
    count = 0
    upper_limit = ceil((2 * n + 0.25) ** 0.5 - 0.5) + 1
    for k in range(1, upper_limit):
        if (n - k * (k + 1) // 2) % k == 0:
            count += 1
    return count

# time: O(sqrt(n))
