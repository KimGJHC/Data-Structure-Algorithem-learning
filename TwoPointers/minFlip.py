"""
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Input: s = "00110"
Output: 1

Input: s = "010110"
Output: 2

Input: s = "00011000"
Output: 2
"""

def minFlipsMonoIncr_v1(s):
    # We need to preprocess the string and for each possible boundary between 0 and 1, calculate the flips needed
    n = len(s)
    left_one, right_zero = [0] * (n+1), [0] * n
    left_one_count = 0
    for i in range(1, n+1):
        if s[i-1] == '1':
            left_one_count += 1
        left_one[i] = left_one_count
    right_zero_count = 0
    for j in range(n-1, -1, -1):
        if s[j] == '0':
            right_zero_count += 1
        right_zero[j] = right_zero_count
    return min([left_one[i] + right_zero[i] for i in range(n)] + [left_one[n]])

# time: O(n)
# space: O(n)
# We can reduce space by reserving only one array
def minFlipsMonoIncr_v2(s):
    n = len(s)
    carry = [0] * (n+1)
    left_one_count = 0
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            left_one_count += 1
        carry[i] = left_one_count
    right_zero_count = 0
    res = carry[-1]
    for j in range(n - 1, -1, -1):
        if s[j] == '0':
            right_zero_count += 1
        res = min(res, right_zero_count + carry[j])
    return res

# space can be O(1)
# Note that we do not care the element at boundary (it can be either '0' or '1' and still be valid)
def minFlipsMonoIncr(s):
    n = len(s)
    ones = 0
    zeros = s.count('0')
    res = zeros
    for i in range(n):
        if s[i] == '1':
            ones += 1
        if s[i] == '0':
            zeros -= 1

        res = min(res, zeros + ones)
    return res


def test():
    s = "00110"
    assert minFlipsMonoIncr(s) == 1
    s = "010110"
    assert minFlipsMonoIncr(s) == 2
    s = "00011000"
    assert minFlipsMonoIncr(s) == 2
    print("All tests passed!")