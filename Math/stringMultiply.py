"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

def multiply(num1, num2):
    # We will deal with product at each digit level
    if num1 == '0' or num2 == '0':
        return '0'

    n1, n2 = len(num1), len(num2)

    res = [0] * (n1+n2) # the product will not have more than n1+n2 digits
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            product = int(num1[i]) * int(num2[j])
            p1, p2 = i+j+1, i+j
            total = product + res[p1]
            res[p2] += total // 10
            res[p1] = total % 10
    return ''.join([str(r) for r in res]) if res[0] != 0 else ''.join([str(r) for r in res[1:]])

# time: O(n1 + n2)
# space: O(n1 + n2)

def test():
    num1 = "2"
    num2 = "3"
    assert multiply(num1, num2) == '6'
    num1 = "123"
    num2 = "456"
    assert multiply(num1, num2) == '56088'
    print("All tests passed!")
