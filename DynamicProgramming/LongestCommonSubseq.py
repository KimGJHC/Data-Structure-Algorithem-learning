"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Input: text1 = "abcde", text2 = "ace"
Output: 3

Input: text1 = "abc", text2 = "abc"
Output: 3

Input: text1 = "abc", text2 = "def"
Output: 0
"""

def longestComSubseq_v1(text1, text2):
    n1, n2 = len(text1), len(text2)
    dp = [[0] * n1 for _ in range(n2)]

    # base case
    first_one = -1
    for row in range(n1):
        if text2[0] == text1[row]:
            first_one = row
            break
    if first_one != -1:
        for row in range(first_one, n1):
            dp[0][row] = 1

    first_one = -1
    for col in range(n2):
        if text2[col] == text1[0]:
            first_one = col
            break
    if first_one != -1:
        for col in range(first_one, n2):
            dp[col][0] = 1
    # inductive steps
    for t2 in range(1, n2):
        for t1 in range(1, n1):
            if text2[t2] == text1[t1]:
                dp[t2][t1] = 1 + dp[t2-1][t1-1]
            else:
                dp[t2][t1] = max(dp[t2-1][t1], dp[t2][t1-1])
    return dp[-1][-1]

# time: O(n1 * n2)
# space: O(n1 * n2)

def longestComSubseq(text1, text2):
    # We can reduce the space complexity to O(min(n1, n2))
    n1, n2 = len(text1), len(text2)
    if n2 < n1:
        text1, text2 = text2, text1
        n1, n2 = n2, n1
    # text1 will always have smaller length
    dp = [[0] * n1 for _ in range(2)]  # dp[0] is previous, dp[1] is current

    # base case
    first_one_1 = -1
    for t1 in range(n1):
        if text2[0] == text1[t1]:
            first_one_1 = t1
            break
    if first_one_1 != -1:
        for t1 in range(first_one_1, n1):
            dp[0][t1] = 1

    first_one_2 = float("inf")
    for t2 in range(n2):
        if text2[t2] == text1[0]:
            first_one_2 = t2
            break

    # inductive steps
    for t2 in range(1, n2):
        dp[1][0] = 0 if t2 < first_one_2 else 1
        for t1 in range(1, n1):
            if text2[t2] == text1[t1]:
                dp[1][t1] = dp[0][t1 - 1] + 1
            else:
                dp[1][t1] = max(dp[0][t1], dp[1][t1 - 1])
        dp[0] = dp[1].copy()
    return dp[1][-1] if n2 > 1 else dp[0][-1]

def test():
    text1 = "abcde"
    text2 = "ace"
    assert longestComSubseq(text1, text2) == 3
    text1 = "abc"
    text2 = "abc"
    assert longestComSubseq(text1, text2) == 3
    text1 = "abc"
    text2 = "def"
    assert longestComSubseq(text1, text2) == 0
    print("All tests passed!")
