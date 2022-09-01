"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n < 3:
            return False

        current = colors[0]
        count = 1
        AB = [0, 0]

        i = 1
        while i < n:
            if colors[i] == colors[i - 1]:
                count += 1
            else:
                if count > 2:
                    if current == 'A':
                        AB[0] += count - 2
                    else:
                        AB[1] += count - 2
                count = 1
                current = colors[i]
            i += 1

        if count > 2:
            if current == 'A':
                AB[0] += count - 2
            else:
                AB[1] += count - 2
        return AB[0] > AB[1]
# time: O(n) where n = len(colors)
# space: O(1)