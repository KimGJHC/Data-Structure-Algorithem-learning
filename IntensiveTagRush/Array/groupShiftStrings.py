"""
249. Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

import collections
class Solution:
    def groupStrings(self, strings):
        ht = collections.defaultdict(list)
        for string in strings:
            integer = self.getInt(string)
            ht[integer].append(string)

        return [group for group in ht.values()]

    def getInt(self, string):
        if len(string) == 1:
            return (-1)

        integer = []
        for i in range(1, len(string)):
            integer.append((ord(string[i]) - ord(string[i - 1]) + 26) % 26)
        return tuple(integer)

# solutions: get integer representation of strings in the same group
# time: O(n * m) where n = len(strings), m = max(len of strings)
# space: O(n * m)