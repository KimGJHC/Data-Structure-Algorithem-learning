"""
Given string s and pattern p, find all p in s, return list of starting index

"""

class Solution:
    def longestPrefixSuffix(self, p):
        # longestPrefixSuffix
        lps = [0] * len(p)
        i = 1
        j = 0

        while i < len(p):
            if p[i] == p[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            elif j != 0 and p[i] != p[j]:
                j = lps[j-1]
            else:
                i += 1
        return lps

    def findPatterns(self, s, p):
        n_p = len(p)
        n_s = len(s)

        j = 0 # index on pattern
        i = 0 # index on s
        lps = self.longestPrefixSuffix(p)
        res = []
        while n_s - i >= n_p - j:
            if p[j] == s[i]:
                j += 1
                i += 1
            if j == n_p:
                res.append(i-j)
                j = lps[j-1]
            elif i < n_s and p[j] != s[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return res