"""
1244. Design A Leaderboard

Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.
"""
from collections import defaultdict
import heapq
class Leaderboard:

    def __init__(self):
        self.playerToScore = defaultdict(int)

    def addScore(self, playerId, score):
        self.playerToScore[playerId] += score

    def top(self, K):
        scores = [-score for score in self.playerToScore.values()]
        heapq.heapify(scores)
        total = 0
        for _ in range(K):
            total -= heapq.heappop(scores)
        return total

    def reset(self, playerId):
        self.playerToScore[playerId] = 0

# solution 1: heap
# time: O(n + Klogn) for top(), O(1) for others
# space: O(n)

import sortedcontainers
class Leaderboard:
    def __init__(self):
        self.scores = {}
        self.sortedScores = sortedcontainers.sorteddict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1

            newScore = preScore + score;
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1

    def top(self, K: int) -> int:
        count, total = 0, 0;

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times):
                total += -key;
                count += 1;

                # Found top-K scores, break.
                if count == K:
                    break;

            # Found top-K scores, break.
            if count == K:
                break;

        return total

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]
# solution 2: sorted dict (it is a BST)
# time: O(logn) for addScore, ret, O(K) for topK
# space: O(n)