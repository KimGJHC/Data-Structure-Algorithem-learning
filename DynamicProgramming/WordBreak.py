"""
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

def wordBreak(s, wordDict):
    """
    Assume the last word of the string is in wordDict
    """
    ht = set(wordDict)
    max_word_length = max([len(word) for word in wordDict])
    min_word_length = min([len(word) for word in wordDict])
    n = len(s)
    dp = [False] * (n + 1)
    dp[-1] = True

    for i in range(n, n - 1 if min_word_length > n else min_word_length - 1, -1):
        if not dp[i]:
            continue
        for j in range(i - 1, max(-1, i - max_word_length - 1), -1):
            if s[j:i] in ht and dp[i]:
                dp[j] = True
        # add early stop
        if dp[0]:
            return True
    return dp[0]

# time: O(n*2)
# space: O(n)

def test():
    s = "leetcode"
    wordDict = ["leet","code"]
    assert wordBreak(s, wordDict) == True
    s = "applepenapple"
    wordDict = ["apple","pen"]
    assert wordBreak(s, wordDict) == True
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    assert wordBreak(s, wordDict) == False
    print("All tests passed!")