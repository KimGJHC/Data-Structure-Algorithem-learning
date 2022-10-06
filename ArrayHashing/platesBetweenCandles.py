"""
2055. Plates Between Candles

There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        # reprocess
        n = len(s)
        right_cloeset = [-1] * n  # position of cloest right | to s[i] inclusive
        left_cloeset = [-1] * n

        right_dash = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                right_dash = i
            right_cloeset[i] = right_dash

        left_dash = -1
        for i in range(n):
            if s[i] == '|':
                left_dash = i
            left_cloeset[i] = left_dash

        prefixCount = {}  # key = index of |, value = # of * in s[:key]
        currentCount = 0
        for i, char in enumerate(s):
            if char == '*':
                currentCount += 1
            else:
                prefixCount[i] = currentCount

        # solve queries
        res = []
        for l, r in queries:
            right_closest2l = right_cloeset[l]
            left_closest2r = left_cloeset[r]
            if right_closest2l == -1 or left_closest2r == -1 or right_closest2l >= left_closest2r:
                res.append(0)
            else:
                res.append(prefixCount[left_closest2r] - prefixCount[right_closest2l])