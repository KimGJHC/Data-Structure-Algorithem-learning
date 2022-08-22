"""
916. Word Subsets
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
"""

import collections
class Solution:
    def wordSubsets(self, words1, words2):
        max_freqs = collections.defaultdict(int)

        for word2 in words2:
            count = collections.Counter(word2)
            for char in count:
                max_freqs[char] = max(max_freqs[char], count[char])

        res = []

        for word1 in words1:
            count = collections.Counter(word1)
            valid = True
            for char in max_freqs:
                if max_freqs[char] > count[char]:
                    valid = False
                    break
            if valid:
                res.append(word1)

        return res

# time: O(n1*l1 + n2*l2)
# space: O(1) because we only have 26 lower case English letters
