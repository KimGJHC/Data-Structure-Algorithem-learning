"""
1461. Check If a String Contains All Binary Codes of Size K

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

1. rolling hash (string slicing method will be O(nk))
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # rolling hash
        n = len(s)
        possible = 2 ** k
        if n < k + possible - 1:
            return False

        visited = set()
        count = 0

        window_hash = 0

        for start in range(n - k + 1):
            if start != 0:
                window_hash = window_hash * 2 - int(s[start - 1]) * possible + int(s[start + k - 1])
            else:
                for i in range(k):
                    window_hash = 2 * window_hash + int(s[i])

            if window_hash not in visited:
                count += 1
                visited.add(window_hash)

            if count == possible:
                return True

        return False