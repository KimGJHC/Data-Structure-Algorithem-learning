"""
820. Short Encoding of Words
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
"""


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)

        suffix = set()
        res = 0
        for word in words:
            if word in suffix:
                continue
            else:
                for i in range(len(word)):
                    suffix.add(word[i:])
                res += len(word) + 1
        return res
# time: O(n*m) where n = len(words) and m = word length
# space: O(nm**2)
    def minimumLengthEncoding_v2(self, words: List[str]) -> int:
        trie, res = {}, 0
        for word in words:
            node = trie
            for c in reversed(word):
                if '$' in node:
                    res -= node.pop('$')
                node = node.setdefault(c, {})
            if not node:
                node['$'] = len(word) + 1
                res += node['$']
        return res
# solution 2: trie