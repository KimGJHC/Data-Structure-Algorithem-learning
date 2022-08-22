"""
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
"""
import collections
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = collections.Counter(arr)
        visited = set()
        for i in count:
            if count[i] in visited:
                return False
            visited.add(count[i])
        return True