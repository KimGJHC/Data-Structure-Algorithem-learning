"""
526. Beautiful Arrangement

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

# Do not have a good idea of DP solution because the index of later number will affect the index of exsiting numbers,
# which means we are not going to have exact sub problems
# Use brute force/backtrack instead
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        self.n = n
        self.res = 0
        self.backtrack(1, set())

        return self.res

    def backtrack(self, idx, visited):
        if idx > self.n:
            self.res += 1

        for i in range(1, self.n + 1):
            if i not in visited and (idx % i == 0 or i % idx == 0):
                visited.add(i)
                self.backtrack(idx + 1, visited)
                visited.remove(i)