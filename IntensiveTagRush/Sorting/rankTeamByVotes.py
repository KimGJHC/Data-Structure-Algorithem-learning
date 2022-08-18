"""
1366. Rank Teams by Votes

In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.
"""
class Solution:
    def rankTeams(self, votes):
        n_team = len(votes[0])

        team_vote = {}
        for team in votes[0]:
            team_vote[team] = [0] * n_team + [team]

        for vote in votes:
            for i, team in enumerate(vote):
                team_vote[team][i] += 1

        res = sorted(list(team_vote.values()), key = lambda x: tuple(x[:-1] + [-ord(x[-1])]), reverse = True)
        return ''.join([item[-1] for item in res])

# time: O(n) where n = len(votes)
# space: O(1)
