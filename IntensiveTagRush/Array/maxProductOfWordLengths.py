"""
318. Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
"""


class Solution:
    def maxProduct(self, words):
        words_rep = [(self.getBitRep(word), len(word)) for word in words]
        max_val = 0
        for i in range(len(words_rep)):
            for j in range(i + 1, len(words_rep)):
                bit_i, len_i = words_rep[i]
                bit_j, len_j = words_rep[j]
                if bit_i & bit_j == 0:
                    max_val = max(max_val, len_i * len_j)
        return max_val

    def getBitRep(self, word):
        res = 0
        for char in word:
            idx = ord(char) - ord('a')
            res |= 1 << idx
            if res == self.ContainAllBitRep:
                break
        return res
# solution 1: bitmasking
# time: O(n*m + n**2) where n = len(words) and m = max(len of words)
# space: O(n)

    def maxProduct_v2(self, words):
        import collections
        self.ContainAllBitRep = (1 << 26) - 1
        ht = collections.defaultdict(int)

        for word in words:
            bitRep = self.getBitRep(word)
            ht[bitRep] = max(ht[bitRep], len(word))

        max_val = 0
        for x in ht:
            for y in ht:
                if x & y == 0:
                    max_val = max(max_val, ht[x] * ht[y])
        return max_val
# solution 2: bitmask + hashmap