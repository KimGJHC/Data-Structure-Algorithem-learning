"""
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # returns length of longest satisfied substring

        def longestSubstringUtil(s, start, end, k):
            if end - start < k:
                return 0

            countMap = [0] * 26
            for i in range(start, end):
                countMap[ord(s[i]) - ord('a')] += 1
            for mid in range(start, end):
                if countMap[ord(s[mid]) - ord('a')] >= k:
                    continue
                midNext = mid + 1
                while midNext < end and countMap[ord(s[midNext]) - ord('a')] < k:
                    midNext += 1
                return max(longestSubstringUtil(s, start, mid, k), longestSubstringUtil(s, midNext, end, k))
            return end - start

        return longestSubstringUtil(s, 0, len(s), k)

# solution: hashmap + recursion
# time: O(n**2) where n = len(s) for n recursion and O(n) for countMap
# space: O(n) for worst case