"""
301. Remove Invalid Parentheses
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # main logic
        l, r = 0, 0

        for char in s:
            if char == '(':
                l += 1
            elif char == ')':
                r = r + 1 if l == 0 else r
                l = l - 1 if l > 0 else l

        res = set()

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            nonlocal res
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    res.add(ans)
            else:
                # s[index] not in resulting valid string
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s,
                            index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'),
                            expr)

                # s[index] in resulting valid string
                expr.append(s[index])

                if s[index] != '(' and s[index] != ')':
                    recurse(s,
                            index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem,
                            expr)
                elif s[index] == '(':
                    recurse(s,
                            index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem,
                            expr)
                elif s[index] == ')' and left_count > right_count:
                    recurse(s,
                            index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem,
                            expr)
                expr.pop()

        recurse(s, 0, 0, 0, l, r, [])
        return list(res)

