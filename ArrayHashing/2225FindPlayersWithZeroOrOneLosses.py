"""
2225. Find Players With Zero or One Losses
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

# Basically use the help of hash map to keep track of the number of losses of players
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        nolose = set()
        onelose = set()
        multilose = set()

        for winner, loser in matches:
            if winner not in onelose and winner not in multilose:
                nolose.add(winner)
            if loser not in onelose and loser not in multilose:
                if loser in nolose:
                    nolose.remove(loser)
                onelose.add(loser)
            elif loser in onelose:
                onelose.remove(loser)
                multilose.add(loser)

        nolose = sorted(list(nolose))
        onelose = sorted(list(onelose))

        return [nolose, onelose]