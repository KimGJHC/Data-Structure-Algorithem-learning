"""
901. Online Stock Span
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

# use monotonically decreasing stack
"""


class StockSpanner:

    def __init__(self):
        self.decreasing_stack = []
        self.current_index = 0

    def next(self, price: int) -> int:

        while self.decreasing_stack and self.decreasing_stack[-1][1] <= price:
            self.decreasing_stack.pop()

        if self.decreasing_stack:
            last_index = self.decreasing_stack[-1][0]
            span = self.current_index - last_index
        else:
            span = self.current_index + 1

        self.decreasing_stack.append((self.current_index, price))
        self.current_index += 1

        return span