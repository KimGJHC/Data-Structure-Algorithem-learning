"""
1165. Single-Row Keyboard
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

# simply use a hashmap
"""


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letter2Index = {letter: i for i, letter in enumerate(keyboard)}

        res = 0
        current = 0
        for letter in word:
            nxt = letter2Index[letter]
            res += abs(current - nxt)
            current = nxt
        return res