"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""


class Solution:
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rotation_t = rotation_b = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotation_t += 1
                elif bottoms[i] != x:
                    rotation_b += 1

            return min(rotation_t, rotation_b)

        n = len(tops)

        res = check(tops[0])

        if res != -1 or tops[0] == bottoms[0]:
            return res
        else:
            return check(bottoms[0])

# time: O(n)
# space: O(1)