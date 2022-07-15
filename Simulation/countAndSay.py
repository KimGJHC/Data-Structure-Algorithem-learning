"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        iterations = n - 1
        s = "1"
        while iterations > 0:
            s = self.countAndSayString(s)
            iterations -= 1

        return s

    def countAndSayString(self, s):
        current = s[0]
        count = 1
        res = ""
        for letter in s[1:]:
            if letter == current:
                count += 1
            else:
                res += str(count) + current
                count = 1
                current = letter
        res += str(count) + current
        return res

# time: O(nlogn)
# space: O(n)

