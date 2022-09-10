"""
336. Palindrome Pairs
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def valid_prefix(word):
            res = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    res.append(word[:i])
            return res

        def valid_suffix(word):
            res = []
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]:
                    res.append(word[i + 1:])
            return res

        word_idx = {word: i for i, word in enumerate(words)}
        res = []

        for idx, word in enumerate(words):
            reverse_word = word[::-1]

            if reverse_word in word_idx and idx != word_idx[reverse_word]:
                res.append([idx, word_idx[reverse_word]])

            for suffix in valid_suffix(word):
                reverse_suffix = suffix[::-1]
                if reverse_suffix in word_idx:
                    res.append([word_idx[reverse_suffix], idx])

            for prefix in valid_prefix(word):
                reverse_prefix = prefix[::-1]
                if reverse_prefix in word_idx:
                    res.append([idx, word_idx[reverse_prefix]])
        return res
# time: O(nk**2)
# space: O((n+k) ** 2)