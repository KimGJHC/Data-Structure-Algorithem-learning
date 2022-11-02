"""
2060. Check if an Original String Exists Given Two Encoded Strings

An original string, consisting of lowercase English letters, can be encoded by the following steps:

Arbitrarily split it into a sequence of some number of non-empty substrings.
Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
Concatenate the sequence as the encoded string.
For example, one way to encode an original string "abcdefghijklmnop" might be:

Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes ["ab", "12", "1", "p"].
Concatenate the elements of the sequence to get the encoded string: "ab121p".
Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.
"""


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        def getValidPrefixLength(s, start):
            # return ending index of the numeric substring of s starting at start
            end = start
            while end < len(s) and s[end].isdigit():
                end += 1
            return end

        @lru_cache(None)
        def possibleLengths(s):
            # return all possible lengths represented by numeric string s
            res = {int(s)}
            for i in range(1, len(s)):
                res |= {x + y for x in possibleLengths(s[:i]) for y in possibleLengths(s[i:])}
            return res

        @lru_cache(None)
        def dp(i, j, diff):
            # return True if s1[i:] matches s2[j:] with given differences (+ for s2 leads)

            # 1. both have reached end and return True if no difference
            if i == len(s1) and j == len(s2):
                return diff == 0

            # 2. s1 has not reached end and s1 starts with a digit
            if i < len(s1) and s1[i].isdigit():
                i2 = getValidPrefixLength(s1, i)
                for L in possibleLengths(s1[i:i2]):
                    if dp(i2, j, diff - L):
                        return True

            # 3. s2 has not reached end and s2 starts with a digit
            elif j < len(s2) and s2[j].isdigit():
                j2 = getValidPrefixLength(s2, j)
                for L in possibleLengths(s2[j:j2]):
                    if dp(i, j2, diff + L):
                        return True

            # 4. non of them have integer prefix or is leading
            elif diff == 0:
                if i == len(s1) or j == len(s2) or s1[i] != s2[j]:
                    return False
                return dp(i + 1, j + 1, 0)

            # 5. non of them have integer predix and s1 is leading
            elif diff < 0:
                if j == len(s2):
                    return False
                return dp(i, j + 1, diff + 1)

            # 5. non of them have integer predix and s2 is leading
            elif diff > 0:
                if i == len(s1):
                    return False
                return dp(i + 1, j, diff - 1)

        return dp(0, 0, 0)
