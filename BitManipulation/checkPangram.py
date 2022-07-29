"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""
# The idea is to replace set by bit and keep track of the letter visited
def checkIfPangram(sentence):
    pangram_set = int("1" * 26, 2)
    count = 0
    for letter in sentence:
        count |= 1 << ord(letter) - ord('a')
    return count == pangram_set