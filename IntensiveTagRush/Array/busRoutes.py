"""
815. Bus Routes
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

"""

import collections
class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stopBoard = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBoard[stop].add(bus)

        queue = collections.deque([source])
        res = 0
        visited = set()  # taken buses

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return res
                for bus in stopBoard[current]:
                    if bus not in visited:
                        visited.add(bus)
                        for stop in routes[bus]:
                            queue.append(stop)
            res += 1
        return -1

# solution: create graph with routes + BFS
# time: O(V + E) for adjList
# space: O(V + E)