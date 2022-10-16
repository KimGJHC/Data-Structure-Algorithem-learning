"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# 1. rolling hash
# 2. iterate through potential first index of needle in haystack
# 3. KMP
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # rolling hash
        p = 23
        n = len(needle)

        if n > len(haystack):
            return -1

        hash_needle = 0
        for i, char in enumerate(needle):
            idx = self.get_index(char)
            hash_needle += (idx * p ** i)

        hash_window = 0
        for i in range(n):
            char = haystack[i]
            idx = self.get_index(char)
            hash_window += (idx * p ** i)

        if hash_needle == hash_window:
            return 0

        i = n
        while i < len(haystack):
            char_add = haystack[i]
            char_delete = haystack[i - n]
            idx_add = self.get_index(char_add)
            idx_delete = self.get_index(char_delete)
            hash_window = (hash_window - idx_delete) // p + idx_add * p ** (n - 1)

            if hash_needle == hash_window:
                return i - n + 1
            i += 1
        return -1

    def get_index(self, char):
        return ord(char) - ord('a') + 1

    def strStr_KMP(self, haystack: str, needle: str) -> int:
        n_h = len(haystack)
        n_n = len(needle)

        LPS = [0] * n_n

        prevLPS, i = 0, 1

        while i < n_n:
            if needle[prevLPS] == needle[i]:
                LPS[i] = prevLPS + 1
                prevLPS = LPS[i]
                i += 1
            elif prevLPS == 0:
                LPS[i] = 0
                i += 1
            else:
                prevLPS = LPS[prevLPS - 1]

        i, j = 0, 0

        while i < n_h:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = LPS[j - 1]
            if j == n_n:
                return i - n_n
        return -1