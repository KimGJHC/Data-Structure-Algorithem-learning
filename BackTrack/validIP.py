def restoreIP(s):
    def backtrack(s, idx, path, res):
        if idx > 4:
            return
        if idx == 4 and not s:
            res.append(path[:-1])
            return
        for i in range(1, min(len(s) + 1, 4)):
            if s[:i] == '0' or (s[:i] != '0' and int(s[:i]) <= 256):
                backtrack(s[i:], idx + 1, path + s[:i] + '.', res)

    res = []
    backtrack(s, 0, '', res)

    return res
