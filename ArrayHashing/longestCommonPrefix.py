"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix_v1(strs):
    strs.sort(key = lambda x: -len(x))

    current = strs.pop()
    while strs:
        nxt = strs.pop()
        for i in range(len(current)):
            if current[i] != nxt[i]:
                current = current[:i]
                break
        if len(current) == 0:
            break
    return current

# time: O(S) S = number of all letters in strs
# space: O(1)

from functools import reduce
def longestCommonPrefix(strs):
    # horizontal scan
    def lcp(s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return s1[:i]
    if not strs:
        return ""
    else:
        return reduce(lcp, strs)

def test():
    strs = ["flower", "flow", "flight"]
    assert longestCommonPrefix(strs) == "fl"
    strs = ["dog", "racecar", "car"]
    assert longestCommonPrefix(strs) == ""
    print("All tests passed!")
