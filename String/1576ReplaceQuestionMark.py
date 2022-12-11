"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters

Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
"""

class Solution:
    def modifyString(self, s: str) -> str:
        self.letters = set(list(string.ascii_lowercase))
        s = list(s)
        for i, letter in enumerate(s):
            if letter == '?':
                not_equal = [s[max(0, i - 1)], s[min(len(s) - 1, i + 1)]]
                new_letter = self.getLetter(not_equal)
                s[i] = new_letter
        return ''.join(s)

    def getLetter(self, not_equal):
        for letter in self.letters:
            if letter not in not_equal:
                return letter