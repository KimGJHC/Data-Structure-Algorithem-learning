"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input: s1 = "", s2 = "", s3 = ""
Output: true
"""

def isInterleave(s1, s2, s3):
    # dp[i][j] be true if s1[:i] and s2[:j] can form interleave s3[:i+j-1]
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n3 != n1 + n2:
        return False

    dp = [[0] * (n2+1) for _ in range(n1+1)]

    for i1 in range(n1+1):
        for i2 in range(n2+1):
            if i1 == 0 and i2 == 0:
                dp[i1][i2] = True
            elif i1 == 0:
                dp[i1][i2] = dp[i1][i2-1] and s2[i2-1] == s3[i1+i2-1]
            elif i2 == 0:
                dp[i1][i2] = dp[i1-1][i2] and s1[i1-1] == s3[i1+i2-1]
            else:
                dp[i1][i2] = (dp[i1][i2 - 1] and s2[i2 - 1] == s3[i1 + i2 - 1]) or (dp[i1-1][i2] and s1[i1-1] == s3[i1+i2-1])
    return dp[n1][n2]

# time: O(n1*n2)
# space: O(n1*n2)

def test():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert isInterleave(s1, s2, s3) == True
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    assert isInterleave(s1, s2, s3) == False
    s1 = ""
    s2 = ""
    s3 = ""
    assert isInterleave(s1, s2, s3) == True
    print("ALl tests passed!")
