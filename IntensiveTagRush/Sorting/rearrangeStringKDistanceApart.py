"""
358. Rearrange String k Distance Apart
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".
"""

import collections
class Solution:
    def rearrangeString(self, s, k):
        n = len(s)
        if k <= 1:
            return s
        count = collections.Counter(s)
        maxf = max(count.values())
        if (maxf - 1) * k + sum([val == maxf for val in count.values()]) > len(s):
            return ''
        res = list(s)
        i = (n-1) % k
        for c in sorted(count, key = lambda i: -count[i]):
            for j in range(count[c]):
                res[i] = c
                i += k
                if i >= n:
                    i = (i-1) % k
        return ''.join(res)

# time: O(n) where n = len(s)
# space: O(n)
