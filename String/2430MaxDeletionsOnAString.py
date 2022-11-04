"""
2430. Maximum Deletions on a String

Share
You are given a string s consisting of only lowercase English letters. In one operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.

# kmp + find i s.t. lps[i] == i - lps[i] + 1 (prefix and suffix is half half of the string)
"""


class Solution:
    def deleteString(self, s: str) -> int:
        remove = 0
        count = 0
        while s:
            lps = self.getPrefixLen(s)
            for i in range(len(lps)):
                match = lps[i]
                rest = i - match + 1
                if rest == match:
                    remove = rest
            # when len(s) = 1
            if remove == 0:
                count += 1
                break
            s = s[remove:]
            remove = 0
            count += 1
        return count

    def getPrefixLen(self, s):
        lps = [0] * len(s)
        i = 1
        j = 0

        while i < len(s):
            if s[i] == s[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            elif j != 0 and s[i] != s[j]:
                j = lps[j - 1]
            else:
                i += 1
        return lps