"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false

Input: s = "aa", p = "a*"
Output: true

Input: s = "ab", p = ".*"
Output: true
"""

def isMatch_v1(s, p):
    # do with recursion
    if not p:
         return not s
    match = s and p[0] in ['.', s[0]]
    if len(p) >= 2 and p[1] == '*':
        return isMatch_v1(s, p[2:]) or (match and isMatch_v1(s[1:], p))
    else:
        return match and isMatch_v1(s[1:], p[1:])

# Use the recursion create dp solution
def isMatch(s, p):
    cache = {}
    ns, np = len(s), len(p)

    def dp(i, j):
        # True if s[i:] matches p[j:]
        if (i, j) not in cache:
            if j == np:
                cache[(i, j)] = i == ns
            else:
                match = i < ns and p[j] in ['.', s[i]]
                if j+1 < np and p[j+1] == '*':
                    cache[(i, j)] = dp(i, j+2) or (match and dp(i+1, j))
                else:
                    cache[(i, j)] = match and dp(i+1, j+1)
        return cache[(i, j)]

    return dp(0, 0)

# time: O(ns*np)
# space: O(ns*np)

def test():
    s = "aa"
    p = "a"
    assert isMatch(s, p) == False
    s = "aa"
    p = "a*"
    assert isMatch(s, p) == True
    s = "ab"
    p = ".*"
    assert isMatch(s, p) == True
    print("All tests passed!")