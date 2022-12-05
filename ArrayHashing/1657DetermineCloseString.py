"""
1657. Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# close strings need to have same length, same unique letters and same count of freqs for each letter
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        letters1 = set(list(word1))
        letters2 = set(list(word2))

        if letters1 != letters2:
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        freq2letter1 = Counter()
        freq2letter2 = Counter()

        for freq in count1.values():
            freq2letter1[freq] += 1

        for freq in count2.values():
            freq2letter2[freq] += 1

        return freq2letter1 == freq2letter2