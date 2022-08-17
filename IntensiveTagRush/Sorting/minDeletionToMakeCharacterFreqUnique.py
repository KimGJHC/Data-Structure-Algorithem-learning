"""
1647. Minimum Deletions to Make Character Frequencies Unique

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""


class Solution:
    def minDeletions(self, s):
        import collections
        char_count = collections.Counter(s)
        freqs = sorted(list(char_count.values()))
        max_freq = freqs[-1]
        res = 0

        while freqs and max_freq > 0:
            current_freq = freqs.pop()
            if current_freq >= max_freq:
                res += current_freq - max_freq
                max_freq -= 1
            else:
                max_freq = current_freq - 1

        return res if not freqs else res + sum(freqs)

# solution: sort frequency and iterate from max_freq to 1
# time: O(nlogn) in the worst case
# space: O(m) where m = # of unique char in s