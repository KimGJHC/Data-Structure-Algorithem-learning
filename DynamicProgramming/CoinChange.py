"""
322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""
import collections
class Solution:
    def coinChange_v1(self, coins, amount):
        # The idea is to use dp, consider the state transfer function with the idea of last selected coins
        # if the amount is exactly coin, it only needs 1 coin
        if amount == 0:
            return 0
        self.dp = collections.defaultdict(int)
        for coin in coins:
            self.dp[coin] = 1
        self.minCoin = min(coins)
        self.coins = coins
        res = self.getCoin(amount)
        return -1 if res == float("inf") else res

    def getCoin(self, amount): # recursive function to do top-down dp
        if amount < self.minCoin:
            self.dp[amount] = float("inf")
            return float("inf")
        if amount in self.dp:
            return self.dp[amount]
        else:
            res = 1 + min([self.getCoin(amount - coin) for coin in self.coins])
            self.dp[amount] = res
        return res
# time: O(Amount*Coin)
# space: O(amount)
    def coinChange(self, coins, amount):
        # since resursion uses lots of memory we try bottom-up dp
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                if amt-coin < 0:
                    continue
                else:
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])
        return -1 if dp[amount] == float('inf') else dp[amount]

    def test(self):
        coins = [1, 2, 5]
        amount = 11
        assert self.coinChange(coins, amount) == 3
        coins = [2]
        amount = 3
        assert self.coinChange(coins, amount) == -1
        coins = [1]
        amount = 0
        self.coinChange(coins, amount)
        assert self.coinChange(coins, amount) == 0
        print("All tests passed!")