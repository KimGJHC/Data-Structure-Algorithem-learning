"""
791. Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""
import collections

import collections
class Solution:
    def customSortString(self, order, s):
        idx_to_str = {i: char for i, char in enumerate(order)}
        char_freq = collections.Counter(s)

        # convert s to idx
        others = ''

        for char in s:
            others += char

        res = ''
        for i in range(len(order)):
            char = idx_to_str[i]
            res += char * char_freq[char]

        return res + others

# solution: convert string to int and sort int, convert int back to string
# time: O(nlog(n))
# space O(n)