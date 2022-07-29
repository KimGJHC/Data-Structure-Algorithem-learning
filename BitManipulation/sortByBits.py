"""
1356. Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""

class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (self.getBitOne(x), x))

    def getBitOne(self, num):
        return sum(bit == '1' for bit in bin(num)[2:])