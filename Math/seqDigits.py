"""
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Input: low = 100, high = 300
Output: [123,234]

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

def sequentialDigits_v1(low, high):
    # The major question is to find the smallest seq digits larger than low
    # We will use a dfs to find such seq digits
    def NumberToDigits(number):
        res = []
        while number:
            res.append(number % 10)
            number = number // 10
        return res[::-1]

    def DigitsToNumber(digits):
        res = 0
        level = 0
        while digits:
            res += digits.pop() * 10 ** level
            level += 1
        return res

    def findNext(lower):
        # find the smallest seq digit strictly larger than lower
        lower = NumberToDigits(lower)
        n = len(lower)
        anchor = 0
        same_anchor = False
        for i in range(n):
            if i > 0:
                if anchor == lower[i] - (i+1):
                    same_anchor = True
            anchor = max(anchor, lower[i] - (i+1))
        if anchor == 0 and not same_anchor:
            return DigitsToNumber([j+1 for j in range(n)])
        if same_anchor:
            anchor += 1
        for i in range(n):
            if i + 1 + anchor > 9 - n + i + 1:
                return DigitsToNumber([j+1 for j in range(n+1)])
        return DigitsToNumber([j+1+anchor for j in range(n)])

    res = []
    current = findNext(low-1)
    while current <= high:
        res.append(current)
        current = findNext(current)
    return res

# The above code is correct but it is too slow
def sequentialDigits(low, high):
    sample = '123456789'
    n = 10
    res = []

    for length in range(len(str(low)), len(str(high)) + 1):
        for start in range(n - length):
            num = int(sample[start:start+length])
            if num > high:
                break
            if num >= low:
                res.append(num)
    return res

# time: O(1)
# space: O(1)

def test():
    low = 100
    high = 300
    assert sequentialDigits(low, high) == [123,234]
    low = 1000
    high = 13000
    assert sequentialDigits(low, high) == [1234,2345,3456,4567,5678,6789,12345]
    print("All tests passed!")
