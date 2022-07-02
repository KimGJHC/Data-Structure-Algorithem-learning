"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Input: s = "()"
Output: true

Input: s = "(*)"
Output: true

Input: s = "(*))"
Output: true
"""

def validParenthesisString(s):
    # Note that when we traverse the valid string (without *), we will always have left Parenthesis more than right Parenthesis
    l, h = 0, 0
    for c in s:
        l += 1 if c == "(" else -1
        h += 1 if c != ")" else -1
        if h < 0:
            break
        l = max(l, 0)
    return l == 0

# time: O(n)
# space: O(1)


def test():
    s = "()"
    assert validParenthesisString(s) == True
    s = "(*)"
    assert validParenthesisString(s) == True
    s = "(*))"
    assert validParenthesisString(s) == True
    s = "((*))))"
    assert validParenthesisString(s) == False
    print("All tests passed!")


