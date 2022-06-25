"""
518. Coin Change 2

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Input: amount = 5, coins = [1,2,5]
Output: 4

Input: amount = 3, coins = [2]
Output: 0

Input: amount = 10, coins = [10]
Output: 1
"""

def change(amount, coins):
    dp = [0]*(amount+1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount+1):
            dp[a] += dp[a-coin]
    return dp[-1]

#time: O(amount*n)
#space: O(amount)

def test():
    amount = 5
    coins = [1, 2, 5]
    assert change(amount, coins) == 4
    amount = 3
    coins = [2]
    assert change(amount, coins) == 0
    amount = 10
    coins = [10]
    assert change(amount, coins) == 1
    print("All tests passed")
