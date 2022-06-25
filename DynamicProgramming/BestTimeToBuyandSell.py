"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [1,2,3,0,2]
Output: 3

Input: prices = [1]
Output: 0
"""

def maxProfit_v1(prices):
    # The are 3 states: reset (between sell and held), sell and hold
    n = len(prices)
    reset, sell, hold = [0] * (n+1), [0] * (n+1), [0] * (n+1) # Each of the element means the max profit at the specific point and specific state
    # set base case
    sell[0], hold[0] = -float('inf'), -float('inf')

    for i, price in enumerate(prices):
        j = i+1
        sell[j] = hold[j-1] + price
        hold[j] = max(hold[j-1], reset[j-1] - price)
        reset[j] = max(reset[j-1], sell[j-1])
    return max(reset[-1], sell[-1])
# time: O(n)
# space: O(n)

def maxProfit(prices):
    # since j iteration only depends on j-1 iteration, we can do space reduction
    reset, sell, hold = 0, -float('inf'), -float('inf')
    for price in prices:
        temp_sell = sell
        sell = hold + price
        hold = max(hold, reset - price)
        reset = max(reset, temp_sell)
    return max(reset, sell)

# space: O(1)


def test():
    prices = [1,2,3,0,2]
    assert maxProfit(prices) == 3
    prices = [1]
    assert maxProfit(prices) == 0
    print("All tests passed!")