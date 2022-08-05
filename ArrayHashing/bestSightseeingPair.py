"""
1014. Best Sightseeing Pair

You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
"""
class Solution:
    def maxScoreSightseeingPair(self, values):
        best_i = 0
        res = 0

        for j, val in enumerate(values):
            res = max(res, val - j + best_i)
            best_i = max(best_i, val -j)

        return res

# time: O(n)
# space: O(1)