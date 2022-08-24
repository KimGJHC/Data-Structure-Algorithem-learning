"""
890. Find and Replace Pattern
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        pattern_int = self.getInt(pattern)

        res = []
        for word in words:
            if self.getInt(word) == pattern_int:
                res.append(word)
        return res

    def getInt(self, word):
        i = 0
        ht = {}
        res = []

        for char in word:
            if char not in ht:
                ht[char] = i
                i += 1
            res.append(ht[char])
        return tuple(res)
# solution 1: integer representation
# time: O(n*m) where n = len(words) and m = max(len of words)
# space: O(m)
    def findAndReplacePattern_v2(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
# solution 2: 2 maps, check bijection
    def findAndReplacePattern_v3(self, words, pattern):
        def match(word):
            m1 = {}
            for p, w in zip(pattern, word):
                if m1.setdefault(p, w) != w:
                    return False
            return len(set(m1.values())) == len(m1.values())

        return filter(match, words)
# solution 2: 2 maps, check injection + domain

