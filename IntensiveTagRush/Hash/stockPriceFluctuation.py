"""
2034. Stock Price Fluctuation
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.
"""

import heapq
class StockPrice:

    def __init__(self):
        self.history = {}  # {timestamp: price}
        self.max_heap = []  # [(price, timestamp)]
        self.min_heap = []
        self.latest_t = -1

    def update(self, timestamp: int, price: int) -> None:
        self.history[timestamp] = price
        self.latest_t = max(self.latest_t, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.history[self.latest_t]

    def maximum(self) -> int:
        while self.max_heap:
            price, timestamp = self.max_heap[0]
            price *= -1
            if self.history[timestamp] == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.history[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)