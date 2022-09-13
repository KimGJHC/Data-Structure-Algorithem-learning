"""
856. Score of Parentheses
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        stack = []

        for char in s:
            if char == '(':
                stack.append(None)
            else:
                if stack[-1] == None:
                    stack.pop()
                    stack.append(1)
                else:
                    while len(stack) > 1 and stack[-2] != None:
                        val = stack.pop()
                        stack[-1] += val
                    val = stack.pop()
                    if stack and stack[-1] == None:
                        stack.pop()
                        val *= 2
                    stack.append(val)
        return sum(stack)

# time: O(n) where n = len(s)
# space: O(n)