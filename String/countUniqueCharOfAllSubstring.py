"""
828. Count Unique Characters of All Substrings of a Given String

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
"""

def uniqueLetterString(s):
    lastOccurance = {}  # a: (i, j), i is the last occurance of one a and j is the last occurance two a in the added string
    res = 0
    previousAdd = 0

    for i, letter in enumerate(s):
        if letter not in lastOccurance:
            lastOccurance[letter] = (None, None)

        lastOneIndex, lastTwoIndex = lastOccurance[letter]

        if lastOneIndex == None:
            Plus = i + 1
            Minus = 0
        elif lastTwoIndex == None:
            Plus = i - lastOneIndex
            Minus = lastOneIndex + 1
        else:
            Plus = i - lastOneIndex
            Minus = lastOneIndex - lastTwoIndex

        res += previousAdd + Plus - Minus
        previousAdd += Plus - Minus

        lastOccurance[letter] = (i, lastOneIndex)

    return res

# time: O(n) where n is len(s)
# space: O(1)

