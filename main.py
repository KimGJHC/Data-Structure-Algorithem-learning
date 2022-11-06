from NamedAlgorithm.KMP import Solution

if __name__ == '__main__':
    solution = Solution()
    p = 'aba'
    s = 'abababbababc'
    res = solution.findPatterns(s, p)
    print(res)

