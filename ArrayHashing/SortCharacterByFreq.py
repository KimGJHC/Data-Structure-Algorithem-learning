"""
451. Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

# Counter + Hashmap
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []
        for letter, freq in count.most_common():
            res.append(letter*freq)
        return ''.join(res)