"""
2272. Substring With Largest Variance

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.
"""

def largestVariance(s):
    def largestVarianceGivenLetter(s, h, l):
        if h == l:
            return 0

        hCount = 0
        hMax = 0
        meet_l = False

        for letter in s:
            if letter == h:
                hCount += 1
            elif letter == l:
                hCount -= 1
                meet_l = True
            else:
                continue

            if meet_l:
                hMax = max(hMax, hCount)

            if hCount < 0:
                hCount = 0
                meet_l = False

        if not meet_l:
            hMax = max(hCount - 1, hMax)
        return hMax

    givenLetters = set(list(s))
    maxVariance = 0

    for h in givenLetters:
        for l in givenLetters:
            maxVariance = max(maxVariance, largestVarianceGivenLetter(s, h, l))
    return maxVariance

# time: O(26*26*n) where n = len(s)
# space: O(1)
