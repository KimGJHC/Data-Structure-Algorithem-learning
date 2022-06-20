"""
91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Input: s = "12"
Output: 2

Input: s = "226"
Output: 3

Input: s = "06"
Output: 0
"""

def numDecodings(s):
    dp = {len(s): 1}
    for i in range(len(s)-1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]

        if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            dp[i] += dp[i+2]

    return dp[0]

# time: O(n)
# space: O(n)

def test():
    assert numDecodings("12") == 2
    assert numDecodings("226") == 3
    assert numDecodings("06") == 0
    print("All tests passed!")

