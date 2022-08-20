"""
2135. Count Words Obtained After Adding a Letter
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.
"""


class Solution:
    def wordCount(self, startWords, targetWords):
        seen = set()
        for word in startWords:
            m = 0
            for ch in word:
                m ^= 1 << ord(ch) - 97
            seen.add(m)

        ans = 0
        for word in targetWords:
            m = 0
            for ch in word:
                m ^= 1 << ord(ch) - 97
            for ch in word:
                if m ^ (1 << ord(ch) - 97) in seen:
                    ans += 1
                    break
        return ans

# solution 1: bitmask + hashset
# time: O(n*s + m*(t + n*s)) for m = len(targetWords)
# space: O(n) where n = len(startWords)