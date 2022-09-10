"""
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []  # store idx
        delete_idx = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    delete_idx.append(i)
        delete_idx += stack

        res = list(s)
        for i in delete_idx:
            res[i] = ''

        res = ''.join(res)
        return res
# time: O(n) where n = len(s)
# space: O(n)