"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        need, window = {}, {}

        for letter in p:
            need[letter] = need.get(letter, 0)
            need[letter] += 1
            window[letter] = 0

        n_need = len(need)
        l, r = 0, 0
        valid = 0

        while r < len(s):
            letter = s[r]
            r += 1

            if letter in need:
                window[letter] += 1
                if window[letter] == need[letter]:
                    valid += 1

            while r - l >= len(p):
                if valid == n_need:
                    res.append(l)
                letter_d = s[l]
                l += 1
                if letter_d in need:
                    if window[letter_d] == need[letter_d]:
                        valid -= 1
                    window[letter_d] -= 1
        return res