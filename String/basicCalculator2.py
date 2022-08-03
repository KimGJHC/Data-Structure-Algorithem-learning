"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


class Solution:
    def calculate_v1(self, s):
        if not s:
            return 0

        stack = []

        op = "+"
        num = ''
        i = 0
        n = len(s)

        while i < n:
            char = s[i]
            if char.isdigit():
                num += char

            if char in ('+', '-', '*', '/') or i == n - 1:
                num = int(num)
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                else:
                    continue
                op = char
                num = ''
            i += 1

        res = 0
        while stack:
            res += stack.pop()
        return res

# time: O(n)
# space: O(n)

# we can get rid of stack
    def calculate(self, s):
        if not s:
            return 0

        current = 0
        last = 0
        res = 0

        n = len(s)
        op = '+'
        i = 0
        while i < n:
            char = s[i]
            if char.isdigit():
                current = current * 10 + int(char)

            if char in ('+', '-', '*', '/') or i == n - 1:
                if op in ("+", "-"):
                    res += last
                    last = current if op == '+' else -current
                elif op == '*':
                    last *= current
                elif op == '/':
                    last = int(last/current)
                op = char
                current = 0
        return res + last