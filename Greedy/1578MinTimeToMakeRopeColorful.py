"""
1578. Minimum Time to Make Rope Colorful
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

# initially thought about dp, use i and last color as state
# it turns out that we only care about local difference so that we can do greedy algo
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        prev = 0

        for curr in range(1, len(colors)):
            if colors[prev] == colors[curr]:
                res += min(neededTime[prev], neededTime[curr])
                if neededTime[curr] > neededTime[prev]:
                    prev = curr
            else:
                prev = curr

        return res








