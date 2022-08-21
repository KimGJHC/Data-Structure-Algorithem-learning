"""
1048. Longest String Chain
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""


class Solution:
    def longestStrChain(self, words):
        memo = {}
        words = set(words)

        def getChain(word):
            if word not in memo:
                maxLength = 1
                for i in range(len(word)):
                    newWord = word[:i] + word[i + 1:]
                    if newWord in words:
                        newLength = 1 + getChain(newWord)
                        maxLength = max(maxLength, newLength)
                memo[word] = maxLength

            return memo[word]

        return max([getChain(word) for word in words])
# solution 1: top-down dp
# time: O(n*maxLength**2)
# space: O(n)