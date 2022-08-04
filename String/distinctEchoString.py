"""
1316. Distinct Echo Substrings

Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).
"""


class Solution:
    def distinctEchoSubstrings(self, text):
        text_length = len(text)
        visited = set()

        for k in range(1, text_length // 2 + 1):
            l = 0
            r = k
            count = 0
            while l < text_length - k:
                if text[l] == text[r]:
                    count += 1
                else:
                    count = 0

                if count == k:
                    visited.add(text[l - k + 1:l + 1])
                    count -= 1

                l += 1
                r += 1
        return len(visited)


# time: O(n**2)
# space: O(n)