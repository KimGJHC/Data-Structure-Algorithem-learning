"""
1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
"""

class Solution:
    def carPooling(self, trips, capacity):
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])
        timestamp.sort()
        used = 0
        for _, passanger_change in timestamp:
            used += passanger_change
            if used > capacity:
                return False
        return True

# solution 1: timestamp of state + sort
# time: O(nlogn)
# space: O(n)