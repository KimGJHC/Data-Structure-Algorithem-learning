def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []


    from collections import defaultdict

    def isDifferByOne(a, b):
        if len(a) != len(b):
            return False
        diff_count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff_count += 1
                if diff_count > 1:
                    break
        if diff_count == 1:
            return True
        return False
    wordList.append(beginWord)
    word_graph = defaultdict(set)
    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            if isDifferByOne(wordList[i], wordList[j]):
                word_graph[wordList[i]].add(wordList[j])
                word_graph[wordList[j]].add(wordList[i])

    res = []
    min_len = float('inf')

    def backtrack(nxt, path, word_graph, visited):
        nonlocal res
        nonlocal min_len

        if nxt == endWord:
            path_len = len(path) + 1
            if path_len < min_len:
                res = [path+[nxt]]
                min_len = path_len
            elif path_len == min_len:
                res.append(path+[nxt])
        else:
            if nxt in visited:
                return
            else:
                path.append(nxt)
                visited.add(nxt)
                for new in word_graph[nxt]:
                    backtrack(new, path, word_graph, visited)
                path.pop()
                visited.remove(nxt)

    for word in word_graph[beginWord]:
        backtrack(word, [beginWord], word_graph, set([beginWord]))

    return res

def findLadders2(beginWord, endWord, wordList):
    import collections, string
    if endWord not in wordList: return []
    tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)

    found, q, nq = False, {beginWord}, set()
    while q and not found:
        words -= set(q)
        for x in q:
            for y in [x[:i]+c+x[i+1:] for i in range(n) for c in string.ascii_lowercase]:
                if y in words:
                    if y == endWord:
                        found = True
                    else:
                        nq.add(y)
                    tree[x].add(y)
        q, nq = nq, set()
    def bt(x):
        return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
    return bt(beginWord)

def findLadders3(beginWord, endWord, wordList):
    import collections, string
    tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
    if endWord not in wordList:
        return []
    found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
    while bq and not found:
        words -= set(bq)
        for x in bq:
            for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in string.ascii_lowercase]:
                if y in words:
                    if y in eq:
                        found = True
                    else:
                        nq.add(y)
                    tree[y].add(x) if rev else tree[x].add(y)
        bq, nq = nq, set()
        if len(bq) > len(eq):
            bq, eq, rev = eq, bq, not rev

    def bt(x):
        return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]

    return bt(beginWord)