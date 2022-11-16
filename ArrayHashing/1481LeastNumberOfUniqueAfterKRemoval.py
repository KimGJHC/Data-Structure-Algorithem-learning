"""
1481. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_to_freq = Counter(arr)
        freqs = [freq for freq in num_to_freq.values()]
        freqs.sort()

        i = 0
        while i < len(freqs) and k > 0:
            if freqs[i] <= k:
                k -= freqs[i]
                i += 1
            else:
                break

        return len(freqs) - i