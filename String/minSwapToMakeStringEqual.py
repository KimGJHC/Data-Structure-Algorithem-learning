"""
1247. Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
"""


class Solution:
    def minimumSwap(self, s1, s2):
        x_y, y_x = 0, 0

        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                x_y += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1

        res = 0
        res += x_y // 2
        res += y_x // 2

        if x_y % 2 == 1:
            res += 2
        return res

# Solution: think about xx, yy, xy, yx and the swaps need for them
# time: O(n) where n = len(s1)
# space: O(1)