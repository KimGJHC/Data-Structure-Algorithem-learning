"""
1029. Two City Scheduling

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

"""


class Solution:
    def twoCitySchedCost(self, costs):
        a_b_diff = [(a - b, a, b) for a, b in costs]
        a_b_diff.sort()
        mid = len(costs) // 2

        return sum([a for _, a, _ in a_b_diff[:mid]] + [b for _, _, b in a_b_diff[mid:]])

# time: O(nlogn)
# space: O(n)