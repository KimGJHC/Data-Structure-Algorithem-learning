from NamedAlgorithm.KMP import Solution

if __name__ == '__main__':
    solution = Solution()
    p = 'sdsasd'
    print(solution.longestPrefixSuffix(p))
    s = 'abcabababccsdfababc'
    res = solution.findPatterns(s, p)
    print(res)

