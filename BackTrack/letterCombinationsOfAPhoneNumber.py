"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2Letter = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                        '9': "wxyz"}
        n = len(digits)
        res = []
        if n == 0:
            return res

        def backtrack(i, path):
            nonlocal res
            if len(path) == n:
                res.append(''.join(path))
                return
            else:
                digit = digits[i]
                letters = digit2Letter[digit]
                for letter in letters:
                    path.append(letter)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return res