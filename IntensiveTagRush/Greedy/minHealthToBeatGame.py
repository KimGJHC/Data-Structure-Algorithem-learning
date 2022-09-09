"""
2214. Minimum Health to Beat Game
You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array damage where damage[i] is the amount of health you will lose to complete the ith level.

You are also given an integer armor. You may use your armor ability at most once during the game on any level which will protect you from at most armor damage.

You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

Return the minimum health you need to start with to beat the game.
"""


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        max_dmg = 0
        total_dmg = 0
        for dmg in damage:
            if dmg > max_dmg:
                max_dmg = dmg
            total_dmg += dmg

        total_dmg -= min(armor, max_dmg)
        return total_dmg + 1
# time: O(n) where n = len(damage)
# space: O(1)