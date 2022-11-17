"""
1444. Number of Ways of Cutting a Pizza
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

# when we need to quickly get some numbers/counts within an area, use prefix sum
# I first thought about 2 ordered hashmap/heaps with order of row and col seperately,
# but it will need lazy deletion and maintaining/modifying hashmap is awkward
"""

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        ROW, COL, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        prefix_sum = [[0 for _ in range(COL+1)] for _ in range(ROW+1)]
        for r in range(ROW - 1, -1, -1):
            for c in range(COL - 1, -1, -1):
                prefix_sum[r][c] = prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - prefix_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, r, c):
            if prefix_sum[r][c] == 0:
                return 0
            if k == 1:
                return 1
            res = 0
            # cut horizontally
            for r_cut in range(r + 1, ROW):
                if prefix_sum[r][c] - prefix_sum[r_cut][c] > 0:
                    res += dp(k - 1, r_cut, c)
                    res %= MOD
            # cut vertically
            for c_cut in range(c + 1, COL):
                if prefix_sum[r][c] - prefix_sum[r][c_cut] > 0:
                    res += dp(k - 1, r, c_cut)
                    res %= MOD
            return res

        return dp(k, 0, 0)