"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def backtrack(i, last_is_palindrome, path):
            nonlocal res
            if i == n:
                if last_is_palindrome:
                    res.append(path[:])
                return
            else:
                current = s[i]

                # include the next char in last string of path
                if path:
                    path[-1] += current
                    new_last_is_palindrome = isValidPalindrome(path[-1])
                    backtrack(i + 1, new_last_is_palindrome, path)
                    path[-1] = path[-1][:-1]

                # include the next char as a new partition, a.k.a being a new last string of the path
                if not path or last_is_palindrome:
                    path.append(current)
                    backtrack(i + 1, True, path)
                    path.pop()

        def isValidPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        backtrack(0, None, [])
        return res