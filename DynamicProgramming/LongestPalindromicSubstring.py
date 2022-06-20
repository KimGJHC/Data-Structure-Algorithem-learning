"""
5.

Given a string s, return the longest palindromic substring in s.
1 <= s.length <= 1000
s consist of only digits and English letters.

Input: s = "babad"
Output: "bab"

Input: s = "cbbd"
Output: "bb"

"""

def longestPalindrome_v1(s):
    n = len(s)
    if n == 0:
        return ''
    if n == 1:
        return s
    if n == 2:
        return s if s[0] == s[1] else s[0]

    res_start, res_end, max_len = 0, 0, 1

    dp = [[True] * n for _ in range(n)]
    for start in range(n - 1):
        dp[start][start + 1] = s[start] == s[start + 1]
        if max_len < 2 and dp[start][start + 1]:
            res_start, res_end = start, start + 1
            max_len = 2

    for col_index in range(2, n):
        for row in range(n - col_index):
            col = row + col_index
            dp[row][col] = dp[row + 1][col - 1] and s[row] == s[col]
            if dp[row][col] and max_len < col + 1 - row:
                res_start, res_end = row, col
                max_len = col + 1 - row
    return s[res_start:res_end + 1]

# time: O(n^2)
# space: O(n^2)


def longestPalindrome(s):
    start, end = 0, -1
    resLen = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > resLen:
                start, end = l, r
                resLen = r-l+1
            l -= 1
            r += 1
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > resLen:
                start, end = l, r
                resLen = r-l+1
            l -= 1
            r += 1
    return s[start:end+1]

# time: O(n^2)
# space: O(1)


def test():
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") in ["bb"]




