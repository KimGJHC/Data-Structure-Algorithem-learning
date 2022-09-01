"""
1405. Longest Happy String
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
"""

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for freq, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if freq > 0:
                heapq.heappush(heap, (-freq, char))

        res = []

        while heap:
            freq1, char1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if heap:
                    freq2, char2 = heapq.heappop(heap)
                    res.append(char2)
                    freq2 += 1
                    if freq2 < 0:
                        heapq.heappush(heap, (freq2, char2))
                    heapq.heappush(heap, (freq1, char1))
            else:
                res.append(char1)
                freq1 += 1
                if freq1 < 0:
                    heapq.heappush(heap, (freq1, char1))

        return '' if not res else ''.join(res)
# time: O(a+b+c)
# space: O(a+b+c)