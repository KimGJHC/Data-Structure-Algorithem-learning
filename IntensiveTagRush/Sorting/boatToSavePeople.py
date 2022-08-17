"""
881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

import collections
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        people = collections.deque(people)

        count = 0
        while people:
            first_weight = people.pop()
            weight_left = limit - first_weight
            if people and people[0] <= weight_left:
                people.popleft()
            count += 1
        return count
# solution: sort + greedy
# time: O(nlogn)
# space: O(n)