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

def minFlipsMonoIncr(s):
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

def test():
    s = "00110"
    assert minFlipsMonoIncr(s) == 1
    s = "010110"
    assert minFlipsMonoIncr(s) == 2
    s = "00011000"
    assert minFlipsMonoIncr(s) == 2
    print("All tests passed!")