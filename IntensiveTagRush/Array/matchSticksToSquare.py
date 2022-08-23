"""
473. Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.
"""


class Solution:
    def makesquare(self, matchsticks):
        if not matchsticks:
            return False

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        side_length = [0] * 4

        def dfs(idx):
            if idx == n:
                return side_length[0] == side_length[1] == side_length[2] == possible_side

            for i in range(4):
                if side_length[i] + matchsticks[idx] <= possible_side:
                    side_length[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    side_length[i] -= matchsticks[idx]
            return False

        return dfs(0)
# time: O(4**n)
# this is NP-complete
    def makesquare_v2(self, matchsticks):
        if not matchsticks:
            return False

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        memo = {}

        def recurse(mask, sides_done):
            total = 0
            for i in range(n - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[n - 1 - i]

            if total > 0 and total % possible_side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            ans = False

            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            for i in range(n - 1, -1, -1):
                if matchsticks[n - 1 - i] <= rem and mask & (1 << i):
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break

            memo[(mask, sides_done)] = ans
            return ans

        return recurse((1 << n) - 1, 0)
# solution 2: dp + bitmask
# time: O(n*2**n)
# space: O(n + 2**n)

