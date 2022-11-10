"""
2462. Total Cost to Hire K Workers
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

# consider using heap to keep track of cost and index
"""


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        left_heap = []
        right_heap = []
        hired = set()  # index of workers being hired

        i = 0
        j = len(costs) - 1

        while i < candidates:
            heapq.heappush(left_heap, (costs[i], i))
            i += 1
        while j > len(costs) - candidates - 1:
            heapq.heappush(right_heap, (costs[j], j))
            j -= 1

        while len(hired) < k:
            if left_heap[0][0] <= right_heap[0][0]:
                c, idx = heapq.heappop(left_heap)
                if i < len(costs):
                    heapq.heappush(left_heap, (costs[i], i))
                    i += 1
            else:
                c, idx = heapq.heappop(right_heap)
                if j >= 0:
                    heapq.heappush(right_heap, (costs[j], j))
                    j -= 1

            if idx not in hired:
                hired.add(idx)
                cost += c
            else:
                continue
        return cost