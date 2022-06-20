import functools
import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def __init__(self):
        self.board = None
        self.m, self.n = None, None
        self.res = None

    def findWords(self, board, words):
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.res = set()

        # preclude
        letter_in_board = collections.Counter(functools.reduce(lambda a, b: a + b, board))
        ht_words = set(words)
        for word in ht_words.copy():
            letter_in_word = collections.Counter(word)
            for l in letter_in_word.keys():
                if letter_in_word[l] > letter_in_board[l]:
                    ht_words.remove(word)
                    break

        root = TrieNode()
        for word in ht_words:
            root.addWord(word)

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, root, "", set())
        return list(self.res)

    def dfs(self, r, c, node, word, visited):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or self.board[r][c] not in node.children or (r, c) in visited:
            return
        visited.add((r, c))
        word += self.board[r][c]
        node = node.children[self.board[r][c]]
        if node.end:
            self.res.add(word)

        self.dfs(r-1, c, node, word, visited.copy())
        self.dfs(r + 1, c, node, word, visited.copy())
        self.dfs(r, c-1, node, word, visited.copy())
        self.dfs(r, c+1, node, word, visited.copy())




