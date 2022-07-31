"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
class Solution:
    def getRow(self, rowIndex):
        prev = [1]

        for i in range(1, rowIndex + 1):
            current = [1]
            for j in range(1, i):
                current.append(prev[j - 1] + prev[j])
            current.append(1)
            prev = current
        return prev