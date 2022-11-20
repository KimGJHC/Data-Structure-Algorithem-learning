"""
2477. Minimum Fuel Cost to Report to the Capital
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

# use dfs to return number of people at each node and accumulate fuel cost in each step
"""


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0

        adjList = defaultdict(list)
        for s, d in roads:
            adjList[s].append(d)
            adjList[d].append(s)
        res = 0

        def dfs(node, prev):
            nonlocal res

            if len(adjList[node]) == 1 and adjList[node][0] == prev:
                res += 1
                return 1

            people = 0
            for neighbor in adjList[node]:
                if neighbor != prev:
                    people += dfs(neighbor, node)
            people += 1
            cars = math.ceil(people / seats)
            if node != 0:
                res += cars

            return people

        dfs(0, -1)
        return res
