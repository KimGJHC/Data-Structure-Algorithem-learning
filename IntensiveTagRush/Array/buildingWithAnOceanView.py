"""
1762. Buildings With an Ocean View
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
"""

import collections
class Solution:
    def findBuildings(self, heights):
        res = collections.deque()
        right_max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > right_max_height:
                res.appendleft(i)
                right_max_height = heights[i]

        return res

# time: O(n)
# space: O(1)