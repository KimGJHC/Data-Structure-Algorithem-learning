"""
1167. Minimum Cost to Connect Sticks

You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.
"""

class Solution:
    def connectSticks(self, sticks):
        import heapq
        cost = 0

        heapq.heapify(sticks)

        while len(sticks) > 1:
            smallest_stick_1 = heapq.heappop(sticks)
            smallest_stick_2 = heapq.heappop(sticks)
            new_stick = smallest_stick_1 + smallest_stick_2
            cost += new_stick
            heapq.heappush(sticks, new_stick)
        return cost