"""
472. Concatenated Words

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105
"""
from functools import lru_cache
def findAllConcatenatedWordsInADict_v1(words):
    ht = set(words)

    @lru_cache()
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in ht and suffix in ht:
                return True
            if prefix in ht and dfs(suffix):
                return True
            if suffix in ht and dfs(prefix):
                return True
        return False

    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res


def findAllConcatenatedWordsInADict(words):
    ht = set(words)
    cache = {}

    def dfs(word):
        if word not in cache:
            cache[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in ht and suffix in ht:
                    cache[word] = True
                    break
                if prefix in ht and dfs(suffix):
                    cache[word] = True
                    break
                if suffix in ht and dfs(prefix):
                    cache[word] = True
                    break
        return cache[word]

    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res

# time: O(n * len(word))
# space: O(n))


def test():
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    assert findAllConcatenatedWordsInADict(words) == ["catsdogcats","dogcatsdog","ratcatdogcat"]
    words = ["cat","dog","catdog"]
    assert findAllConcatenatedWordsInADict(words) == ["catdog"]
    print("All tests passed!")

