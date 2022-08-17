"""
792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""


class Solution:
    def numMatchingSubseq(self, s, words):

        # preprocess
        next_char = {}
        count = 0

        for word in words:
            next_char[word[0]] = next_char.get(word[0], []) + [word[1:]]

        for char in s:
            if char in next_char:
                suffixes = next_char.pop(char)
                for suffix in suffixes:
                    if len(suffix) == 0:
                        count += 1
                        continue
                    else:
                        next_char[suffix[0]] = next_char.get(suffix[0], []) + [suffix[1:]]
        return count

# solution 1: track suffix
# time: O(n+ma) where n = len(s), m = len(words), a is average word length
# space: O(ma)