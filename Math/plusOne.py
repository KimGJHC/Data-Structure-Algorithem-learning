"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Input: digits = [9]
Output: [1,0]
"""

def plusOne(digits):
    carrier = 1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += carrier
            carrier = 0
            break
        else:
            digits[i] = 0
    if carrier == 1:
        digits = [1] + digits
    return digits

# time: O(n)
# space: O(1)

def test():
    digits = [1, 2, 3]
    assert plusOne(digits) == [1,2,4]
    digits = [4, 3, 2, 1]
    assert plusOne(digits) == [4, 3, 2, 2]
    digits = [9]
    assert plusOne(digits) == [1, 0]
    print("All tests passed!")