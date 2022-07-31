"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
        return res

# time: O(n**2)
# space: O(n)