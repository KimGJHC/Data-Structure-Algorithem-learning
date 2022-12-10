"""
1065. Index Pairs of a String
Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

# use a trie to check validity of current string
# might be able to utilize KMP
"""


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        tire = {}
        for word in words:
            current = tire
            for letter in word:
                if letter not in current:
                    current[letter] = {}
                current = current[letter]
            current['END'] = 1

        res = []

        for i in range(len(text)):
            j = i
            current = tire
            while j < len(text) and text[j] in current:
                current = current[text[j]]
                if 'END' in current:
                    res.append([i, j])
                j += 1

        return res